import pytest
import sys
import os


def set_project_path():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(project_root)
    sys.path.append(os.path.join(project_root, 'src'))
    sys.path.append(os.path.join(project_root, 'src', 'db'))
    sys.path.append(os.path.join(project_root, 'src', 'errors'))
    sys.path.append(os.path.join(project_root, 'tests'))


set_project_path()

from src.db.dbconnection import Session


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
