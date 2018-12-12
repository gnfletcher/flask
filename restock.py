from datetime import datetime
from sqlalchemy import Column, String, Text, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP
from base import BASE


class Restock(BASE):
    __tablename__ = 'restock'

    RestockID = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    Name = Column(String(255), nullable=False, index=True)
    ProductNumber = Column(SMALLINT(unsigned=True), nullable=False)
    description = Column(Text())
    quantity_per_unit = Column(SMALLINT(unsigned=True), nullable=False)
    unitprice = Column(SMALLINT(unsigned=True), nullable=True)
    standard_cost = Column(SMALLINT(unsigned=True), nullable=True)
    minimum_stock_level = Column(SMALLINT(unsigned=True), nullable=False)
    weight = Column(SMALLINT(unsigned=True), nullable=True)
    color = Column(SMALLINT(unsigned=True), nullable=True)
    SupplierID = Column(SMALLINT(unsigned=True), nullable=False)
    CategoryID = Column(SMALLINT(unsigned=True), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('ProductID', name='PRIMARY'),
        Index('idx_name', 'Name'),)

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
        return "Product"
