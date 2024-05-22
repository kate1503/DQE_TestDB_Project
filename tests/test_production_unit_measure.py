from sqlalchemy import func
from src.db import tables as tbl
import pytest
from tests.conftest import get_db_session
from src.errors.global_enums import GlobalErrorMessages as Error


def test_is_unique_unit_measure_name(get_db_session):
    """
    Uniqueness test - Check measure Name attribute contains unique values (no duplicates present)
    """
    duplicated_unit_measure_name = (get_db_session.query(
        tbl.UnitMeasure.Name, func.count()).
                                    group_by(tbl.UnitMeasure.Name).
                                    having(func.count() > 1).all())
    assert len(duplicated_unit_measure_name) == 0, Error.DUPLICATE_VALUES_FOUND.value


@pytest.mark.smoke
def test_uppercase_unit_measure_code(get_db_session):
    """
    Validity test - Check measure Code attribute values are in uppercase
    """
    count_code_not_uppercase = (get_db_session.query(
        func.count()).where(
        func.upper(tbl.UnitMeasure.UnitMeasureCode) != tbl.UnitMeasure.UnitMeasureCode
    ).scalar())
    assert count_code_not_uppercase == 0, Error.WRONG_VALUE_FORMAT.value
