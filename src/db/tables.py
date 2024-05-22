from sqlalchemy import Column
from sqlalchemy import Integer, NVARCHAR, SmallInteger, BINARY, DATETIME, NCHAR
from dbconnection import Model


class Address(Model):

    __tablename__ = 'Address'
    __table_args__ = {'schema': 'Person'}

    AddressID = Column(Integer, primary_key=True)
    AddressLine1 = Column(NVARCHAR)
    PostalCode = Column(NVARCHAR)


class Document(Model):
    __tablename__ = 'Document'
    __table_args__ = {'schema': 'Production'}

    DocumentNode = Column(BINARY, primary_key=True)
    Title = Column(NVARCHAR)
    DocumentSummary = Column(NVARCHAR)
    Status = Column(SmallInteger)


class UnitMeasure(Model):
    __tablename__ = 'UnitMeasure'
    __table_args__ = {'schema': 'Production'}

    UnitMeasureCode = Column(NCHAR, primary_key=True)
    Name = Column(NVARCHAR)
    ModifiedDate = Column(DATETIME)