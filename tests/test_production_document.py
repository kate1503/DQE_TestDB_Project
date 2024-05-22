import pytest
from src.db import tables as tbl
from tests.conftest import get_db_session
from sqlalchemy import func
from src.errors.global_enums import GlobalErrorMessages as Error


@pytest.mark.smoke
def test_allowed_values_document_status(get_db_session):
    """
    Validity test - Check Status attribute contains allowed values
    """
    allowed_status_values = [1, 2, 3]
    incorrect_status = (get_db_session.query(tbl.Document).
                        filter(tbl.Document.Status.notin_(allowed_status_values)).all())
    assert len(incorrect_status) == 0, Error.NOT_ALLOWED_VALUE.value


@pytest.mark.smoke
def test_max_len_document_title(get_db_session):
    """
    Completeness test - Check Title attribute value with MAX length is not truncated
    """
    max_length = (get_db_session.query(func.max(func.length(tbl.Document.Title))).scalar())
    max_length_title = (get_db_session.query(
        tbl.Document.Title).filter(
        func.length(tbl.Document.Title) == max_length).first())
    assert max_length_title[0] == 'Front Reflector Bracket and Reflector Assembly 3', Error.WRONG_MAX_LEN_STRING.value
