from datetime import datetime
from sqlalchemy import Column, String, Text, PrimaryKeyConstraint, Index
from sqlalchemy.dialects.mysql import SMALLINT, TIMESTAMP, DATE, DECIMAL
from base import BASE


class SakilaProducts(BASE):
    __tablename__ = 'sakila.film'

    film_id = Column(SMALLINT(unsigned=True), nullable=False, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    release_year = Column(SMALLINT(unsigned=True), nullable=False)
    language_id = Column(String(255), nullable=True)
    original_language_id = Column(String(255), nullable=True)
    rental_duration = Column(SMALLINT(unsigned=True), nullable=False)
    rental_rate = Column(DECIMAL(unsigned=True), nullable=False)
    length = Column(SMALLINT(unsigned=True), nullable=False)
    replacement_cost = Column(DECIMAL(unsigned=True), nullable=False)
    rating = Column(String(255), nullable=True)
    special_features = Column(String(255), nullable=True)
    last_update = Column(TIMESTAMP, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('film_id', name='PRIMARY'),
        Index('idx_title', 'title'),)

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
