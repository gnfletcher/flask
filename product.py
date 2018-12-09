from datetime import datetime
from sqlalchemy import Column, String, Text, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
from base import BASE


class Product(BASE):
    __tablename__ = 'product'

    productID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    name = Column(String(255), nullable=False, index=True)
    productNumber = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    description = Column(Text())
    quantity_per_unit = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    unitprice = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    standard_cost = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    minimum_stock_level = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    weight = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    color = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    supplierID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    categoryID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    last_update = Column(TIMESTAMP, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('productID', name='PRIMARY'),
        Index('idx_name', 'name'),)

    # The constructor
    def __init__(self, name, description, unitprice, standard_cost, weight, color):
        self.name = name
        self.description = description
        self.unitprice = unitprice
        self.standard_cost = standard_cost
        self.weight = weight
        self.color = color
        self.last_update = datetime.today()

    def __repr__(self):
        return "\nProduct(productID = {self.productID}, " \
               "\n\tname = {self.name}," \
               "\n\tunitprice = {self.unitprice}," \
               "\n\tlast_update = {self.last_update})".format(self=self)
