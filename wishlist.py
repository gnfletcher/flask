from datetime import datetime
from sqlalchemy import Column, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
from base import BASE


class Wishlist(BASE):
    __tablename__ = 'wishlist'

    wishlistID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    customerID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    productID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    last_update = Column(TIMESTAMP, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('wishlistID', name='PRIMARY'),
        Index('idx_customerID', 'customerID'),)

    # The constructor
    def __init__(self, customerid, productid):
        self.customerid = customerid
        self.productid = productid
        self.last_update = datetime.today()

    def __repr__(self):
        return "\nCustomer = (customerid = {self.customerid}, " \
               "\n\tproduct = {self.productid}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
