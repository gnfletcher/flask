from datetime import datetime
from sqlalchemy import Column, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP, DATE
from base import BASE


class ShoppingCart(BASE):
    __tablename__ = 'shoppingcart'

    shoppingCartID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    quantity = Column(SMALLINT(unsigned=True), nullable=False)
    createdDate = Column(DATE)
    customerID = Column(SMALLINT(unsigned=True), nullable=False)
    productID = Column(SMALLINT(unsigned=True), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('shoppingCartID', name='PRIMARY'),
        Index('idx_customerID', 'customerID'),)

    # The constructor
    def __init__(self, customerid, createddate, quantity, productid):
        self.customerid = customerid
        self.createddate = createddate
        self.quantity = quantity
        self.productid = productid
        self.last_update = datetime.today()

    def __repr__(self):
        return "\nCustomer = (customerid = {self.customerid}, " \
               "\n\tquantity = {self.quantity}," \
               "\n\tproduct = {self.productid}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
