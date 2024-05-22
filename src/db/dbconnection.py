from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from settings import USERID, PASSWORD, SERVER_PORT

DRIVER_NAME = 'SQL Server'
SERVER_HOST = 'host.docker.internal'
DATABASE = 'AdventureWorks2012'
PORT = SERVER_PORT
USER_ID = USERID
USER_PASSWORD = PASSWORD

CONNECTION_ROW = f'mssql+pymssql://{USER_ID}:{USER_PASSWORD}@{SERVER_HOST}:{PORT}/{DATABASE}'

Model = declarative_base(name='Model')

engine = create_engine(
    CONNECTION_ROW
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

session = Session()
