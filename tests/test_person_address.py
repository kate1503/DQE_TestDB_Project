from src.db import tables
from tests.conftest import get_db_session
import pytest
from sqlalchemy import func, or_
from src.errors.global_enums import GlobalErrorMessages as Error


@pytest.mark.smoke
def test_is_complete_address_line1(get_db_session):
    """
    Completeness test - Check Not nullable column AddressLine1 doesn't contain NULL or empty values
    """
    count_nulls_address_line1 = (get_db_session.query(
        func.count()).filter(or_(tables.Address.AddressLine1.is_(None),
                                 tables.Address.AddressLine1 == '')).scalar())
    assert count_nulls_address_line1 == 0, Error.WRONG_NULL_VALUE.value


@pytest.mark.smoke
def test_format_address_postalcode(get_db_session):
    """
    Validity test - Check that PostalCode attribute values follow to correct format
    """
    invalid_postal_code = (get_db_session.query(func.count()).filter(
        tables.Address.PostalCode.not_like('%[A-Za-z0-9- ]%', escape='\\')
    ).scalar())
    assert invalid_postal_code == 0, Error.WRONG_VALUE_FORMAT.value
