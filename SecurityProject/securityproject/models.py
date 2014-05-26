from sqlalchemy import (
    Column,
    Index,
    Integer,
    VARCHAR,
    Text,
    String,
    ForeignKey,
    Date,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension
import hashlib
import re

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class ValidationError(Exception):
    pass

def validateEmail(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError("Error: Please enter a valid email")
    return email

def validatePassword(password):
    if(len(password) < 8):
        raise ValidationError("Error: Passwords must be 8 more or characters")
    return hashlib.sha512(password).hexdigest()

def validateName(name):
    #if not re.match(r"[a-z][A-Z] ", name):
     #   raise ValidationError("Error: Please enter a valid first/last name")
    return name

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    first_name = Column(VARCHAR(255))
    last_name = Column(VARCHAR(255))
    validation_code = Column(VARCHAR(255))
    authorization_flag = Column(Integer)

    def __init__(self, email, password, first_name, last_name):
        self.user_id = None
        self.email = validateEmail(email)
        self.password = validatePassword(password)
        self.first_name = validateName(first_name)
        self.last_name = validateName(last_name)
        self.authorization_flag = 0

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class AddressInfo(Base):
    __tablename__ = 'addressInfo'

    aid = Column(Integer, primary_key=True)
    address = Column(String(250))
    address2 = Column(String(250))
    state = Column(String(250))
    city = Column(String(250))
    country = Column(String(250))
    zipcode = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship(Users)

    def __init__(self, address, address2, state, city, zipcode, country, user_id):
        self.aid = None
        self.address = address
        self.address2 = address2
        self.state = state
        self.city = city
        self.country = country
        self.zipcode = zipcode
        self.user_id = user_id


class PaymentInfo(Base):
    __tablename__ = 'paymentInfo'

    piid = Column(Integer, primary_key=True)
    aid = Column(Integer, ForeignKey('addressInfo.aid'))
    addressInfo = relationship(AddressInfo)
    type = Column(String(250), nullable=False)
    exp_date = Column(String(250), nullable=False)
    cvv = Column(Integer, nullable=False)
    card_number = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship(Users)

    def __init__(self, aid, type, exp_date, cvv, card_number, user_id):
        self.piid = None
        self.aid = aid
        self.type = type
        self.exp_date = exp_date
        self.cvv = cvv
        self.card_number = card_number
        self.user_id = user_id


class Product(Base):
    __tablename__ = 'product'

    pid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    category = Column(String(250), nullable=False)
    options = Column(String(250), nullable=True)
    price = Column(Integer)

    def __init__(self, name, description, category, options, price):
        self.pid = None
        self.name = name
        self.description = description
        self.category = category
        self.options = options
        self.price = price

class Images(Base):
    __tablename__ = 'images'

    iid = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('product.pid'))
    product = relationship(Product)
    url = Column(String(250), nullable=False)
    title = Column(String(250), nullable=True)
    caption = Column(String(250), nullable=True)



class Order(Base):
    __tablename__ = 'order'

    oid = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship(Users)
    aid = Column(Integer, ForeignKey('addressInfo.aid'))
    addressInfo = relationship(AddressInfo)
    pid = Column(Integer, ForeignKey('paymentInfo.piid'))
    paymentInfo = relationship(PaymentInfo)
    date = Column(Date)

class Options(Base):
    __tablename__ = 'options'

    opid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    price = Column(Integer)

class OrderItem(Base):
    __tablename__ = 'orderItem'

    oiid = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('product.pid'))
    product = relationship(Product)
    oid = Column(Integer, ForeignKey('order.oid'))
    order = relationship(Order)
    qtd = Column(Integer)
