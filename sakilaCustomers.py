from datetime import datetime
from sqlalchemy import Column, String, Text, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP, DATE
from base import BASE


class SakilaCustomers(BASE):
    __tablename__ = 'sakila.customer'

    customer_id = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    store_id = Column(SMALLINT(unsigned=True), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    address_id = Column(String(255), nullable=True)
    active = Column(SMALLINT(unsigned=True), nullable=True)
    create_date = Column(TIMESTAMP, nullable=True)
    last_update = Column(TIMESTAMP, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('customer_id', name='PRIMARY'),
        Index('idx_email', 'email'),)

    # The constructor
    def __init__(self, customerid, first_name, last_name, email, username, password):
        self.customerid = customerid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.last_update = datetime.today()

    def __repr__(self):
        return "\nCustomer = (customerid = {self.customerid}, " \
               "\n\tFirst name = {self.first_name}," \
               "\n\tLast name = {self.last_name}," \
               "\n\temail = {self.email}," \
               "\n\tusername = {self.username}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
