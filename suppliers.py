from datetime import datetime
from sqlalchemy import Column, String, Text, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP, DATE
from base import BASE


class Suppliers(BASE):
    __tablename__ = 'supplier'

    supplierID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    companyname = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(SMALLINT(unsigned=True), nullable=True)
    address = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    zipcode = Column(SMALLINT(unsigned=True), nullable=True)
    country = Column(String(255), nullable=True)
    username = Column(String(255), nullable=False, index=True)
    password = Column(String(255), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('customerID', name='PRIMARY'),
        Index('idx_companyname', 'companyname'),)

    # The constructor
    def __init__(self, supplierID, companyname, email):
        self.supplierID = supplierID
        self.companyname = companyname
        self.email = email

    def __repr__(self):
        return "\nCustomer = (customerid = {self.customerid}, " \
               "\n\tFirst name = {self.first_name}," \
               "\n\tLast name = {self.last_name}," \
               "\n\temail = {self.email}," \
               "\n\tusername = {self.username}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
