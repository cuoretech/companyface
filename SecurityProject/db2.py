import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )
 
Base = declarative_base()
 

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    last_name = Column(VARCHAR(255))
    first_name = Column(VARCHAR(255))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    validation_code = Column(VARCHAR(255))
    authorization_flag = Column(Integer)

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

class PaymentInfo(Base):
    __tablename__ = 'paymentInfo'

    piid = Column(Integer, primary_key=True)
    aid = Column(Integer, ForeignKey('addressInfo.aid'))
    addressInfo = relationship(AddressInfo)
    type = Column(String(250), nullable=False)
    exp_date = Column(String(250), nullable=False)
    cvv = Column(Integer, nullable=False)
    number = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship(Users)

class Product(Base):
    __tablename__ = 'product'

    pid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    category = Column(String(250), nullable=False)
    options = Column(String(250), nullable=True)
    price = Column(Integer)

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
    # opid = Column(Integer, ForeignKey('options.pid'))
    # options = relationship(Product)
    oid = Column(Integer, ForeignKey('order.oid'))
    order = relationship(Order)
    qtd = Column(Integer)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///database.sqlite')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# new_person = Users(last_name='Bharathi', first_name='Vivek', email='vivek.bharathi@gmail.com', password='91963')
# session.add(new_person)
# new_product = Product()
# new_product = Product(name='ALAN', description='Server', category='Web Software', price='3000')
# session.add(new_product)
# new_product = Product(name='Television', description='TV', category='Entertainment', price='650')
# session.add(new_product)
new_product = Product(name='Laptop', description='MobilePC', category='PC', price='800')
session.add(new_product)
new_product = Product(name='Phone', description='Cellphone', category='Communication', price='450')
session.add(new_product)
new_product = Product(name='Speakers', description='SoundUnit', category='Entertainment', price='500')
session.add(new_product)
new_product = Product(name='Accessories', description='Addon', category='Electronics', price='200')
session.add(new_product)
# session.add(new_product)
session.commit()

p = session.query(Product).all()
for i in p:
    print i.name


