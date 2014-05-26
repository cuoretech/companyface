from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import remember
from pyramid.security import forget
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import random
import string
import hashlib
import transaction

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Users,
    Product,
    AddressInfo,
    ValidationError
    )

def addProduct(controls, productName, session):
    found = False
    if 'cart' in session:
        for item in session['cart']:
            if productName == item[0]:
                qty = int(item[1])
                qty  += 1
                item[1] = str(qty)
                found = True 
        if not found:
            session['cart'].append([productName, "1"])
    else:
        session['cart'] = [[productName, "1"]]

    return session



def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generateEmail(email, first_name, last_name):
    code = id_generator()
    messageBody = "Hello " + first_name + " " + last_name + ",\n\nThank you for registering for our site! Please click the following link to complete your registration:\n"
    messageBody += "https://dev.cuore.io/validate?c=" + code
    DBSession.query(Users).filter(Users.email == email).update({Users.validation_code: code})
    return Message(subject="Welcome to Cuore", sender="noreply@dev.cuore.io", recipients = [email], body=messageBody)
    
@view_config(route_name='logout', renderer='CompanyFace/logout.pt')
def logout(request):
    headers = forget(request)
    response = render_to_response('templates/logout.pt',{}) 
    response.headerlist.extend(headers)
    return response


@view_config(route_name='home', renderer='CompanyFace/mytemplate.pt')
def my_view(request):
    logged_in = request.authenticated_userid is not None
    headers=[]
    session = request.session
    print logged_in
    message = ""
    error_occured = False
    try:
        if request.POST:
            print request.POST
        if logged_in:
            if request.POST and "stripeToken" in request.POST:
                print "doing payment"
                user_id = request.authenticated_userid
                if 'cart' in session:
                    messagebody = ""
                    for item in session['cart']:
                        product = DBSession.query(Product).filter(Product.name == item[0]).first()
                        messagebody += "\nItem: " + item[0] + ", Quantity: " + item[1] + "Total Price: "+ str(product.price*int(item[1]))
                        messagebody += "\n\t Description: " + product.description
                    addrInfo = DBSession.query(AddressInfo).filter(AddressInfo.user_id == user_id).first()
                    user = DBSession.query(Users).filter(Users.user_id == user_id).first()
                    messagebody+="\n\nShipping to:\n " + user.first_name + " " + user.last_name
                    messagebody+="\n" + addrInfo.address
                    if addrInfo.address2 != "":
                        messagebody += "\n" + addrInfo.address2
                    messagebody+="\n" + addrInfo.city + ", " + addrInfo.state + " " + addrInfo.zipcode
                    msg = Message(subject="Your purchase with Tech Store", sender="noreply@dev.cuore.io", recipients = [user.email], body=messagebody)
                    mailer = request.registry['mailer']
                    mailer.send_immediately(msg)
                    session['cart'] = []
                    error_occured = True
                    message = "Payment successful! Check your email for an invoice."
                else:
                    error_occured = True
                    message = "Cart is empty!"
        if not logged_in:
            if 'login' in request.params:
                user = DBSession.query(Users).filter(Users.email == request.POST['email'], Users.password == hashlib.sha512(request.POST['password']).hexdigest()).first()
                if not user:
                    message = "Invalid username/password"
                    error_occured = True
                elif user.authorization_flag == 0:
                    message = "Account not verified, please check your email"
                    error_occured = True
                else:
                    headers = remember(request, user.user_id)
                    logged_in=True
                    message = "Successfully logged in"
            elif 'register' in request.params:
                print "register"
                controls = request.POST
                if controls['Password'] == controls['Password2']:
                    try:
                        user = DBSession.query(Users).filter(Users.email == controls['Email']).first()
                        if user:
                            message = "User Already Exists"
                            error_occured=True
                        else:
                            DBSession.add(Users(controls['Email'], controls['Password'], controls['First Name'], controls['Last Name']))
                            emailMessage = generateEmail(controls['Email'], controls['First Name'], controls['Last Name'])
                            user = DBSession.query(Users).filter(Users.email == controls['Email']).first()
                            DBSession.add(AddressInfo(controls['Address Line 1'], controls['Address Line 1'], controls['State'], controls['City'], controls['Post Code'], controls['Country'], user.user_id))
                            mailer = request.registry['mailer']
                            mailer.send_immediately(emailMessage)
                            message = "User sucessfully created"
                    except ValidationError as e:
                        print "validation error"
                        error_occured = True
                        message = str(e)
                else:
                    message = "Error: Passwords must match!"
                    error_occured = True

        if 'Laptop' in request.params:
            session = addProduct(request.POST, 'Laptop', session)
        if 'Phone' in request.params:
            session = addProduct(request.POST, 'Phone', session)
        if 'Speakers' in request.params:
            session = addProduct(request.POST, 'Speakers', session)
        if 'Accessories' in request.params:
            session = addProduct(request.POST, 'Accessories', session)
        if 'clear' in request.params:
            if 'cart' in session:
                session['cart'] = []

                # if 'Laptop' in session:
                #     session['cart'].append ('Laptop', 200, 2)
                #     # productAdded.price, productAdded.description, productAdded.name, session['Laptop']['qtd']+1
                # else:
                #     session['cart'].append ('Laptop', 200, 2)

                # # session['Laptop'] = {'price': productAdded.price, 'description': productAdded.description, 'name': productAdded.name, 'qtd': 1}

    except KeyError:
        message = "Error: Bad POST request: " 
        error_occured = True
    except DBAPIError, (instance): 
        message = "Error: Database Error: " + str(instance.statement) + ", params: " + str(instance.params)
    print message
    print session
    cart = []
    total = 0.0
    if 'cart' in session:
        for item in session['cart']:
            product = DBSession.query(Product).filter(Product.name == item[0]).first()
            cart.append([item[0], item[1], product.description, product.price])
            total += product.price * int(item[1])

    response = render_to_response('CompanyFace/mytemplate.pt',{'logged_in':logged_in, 'message':message, 'cart':cart, 'error_occured': error_occured, "total":total},request=request)
    if headers:
        response.headerlist.extend(headers)

    return response

@view_config(route_name='validate', renderer='templates/validate.pt')
def validate(request):
    if 'c' in request.params:
        code = request.GET['c']
        user = DBSession.query(Users).filter(code == Users.validation_code).one()
        if user:
            DBSession.query(Users).filter(code == Users.validation_code).update({Users.authorization_flag: 1})
            return {"success":True}
    return {"success":False}

@view_config(route_name='login')#, renderer='templates/login.pt')
def login(request):
    if 'login' in request.params:
        user = DBSession.query(Users).filter(Users.email == request.POST['email'], Users.password == request.POST['password']).first()
        if not user:
            return render_to_response('templates/login.pt', {'message':'Invalid Email/Password'})
        return render_to_response('templates/welcome.pt', {'email':request.POST['email'],'user_id':user.user_id}, request=request)
    else:
        return render_to_response('templates/login.pt', {'message':''})

@view_config(route_name='register', renderer='templates/register.pt')
def register(request):
    #return {'message': str(request)}    
    if 'register' in request.params:
        controls = request.POST
        if 'password' in controls and controls['password'] == controls['password2']:
            DBSession.add(Users(controls['email'], controls['password']))
            #DBSession.commit()
            return {'message':'User sucessfully created'}
        else:
            return {'message':'Error: Passwords must match!'}
    return {'message':''} 

@view_config(route_name='db', renderer='templates/database.pt')
def db(request):
    try:
        one = DBSession.query(Users).filter(Users.email == 'one').all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one[3], 'project': 'SecurityProject'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_database_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


