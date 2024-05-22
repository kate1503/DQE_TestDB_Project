from sqlalchemy import Column
from sqlalchemy import Integer, NVARCHAR
from dbconnection import Model


class Address(Model):

    __tablename__ = 'Address'
    __table_args__ = {'schema': 'Person'}

    AddressID = Column(Integer, primary_key=True)
    AddressLine1 = Column(NVARCHAR)
    PostalCode = Column(NVARCHAR)