from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_NULL_VALUE = "Not nullable column contains NULL or empty values"
    WRONG_ROWS_COUNT = "Rows count doesn't match to expected result"
    WRONG_VALUE_FORMAT = "Values do not conform to the expected format"
    WRONG_DATE_ACCURACY = "Date values do not conform to the required accuracy"
    OUT_OF_RANGE = "Column contains value(s) outside the allowed range"
    NOT_ALLOWED_VALUE = "Column contains not allowed value(s)"
    WRONG_MIN_VALUE = "The minimum value constraint is violated"
    WRONG_MAX_VALUE = "The maximum value constraint is violated"
    DUPLICATE_VALUES_FOUND = "Duplicate values found in the unique constraint field(s)"
    WRONG_MAX_LEN_STRING = "The maximum len string doesn't match to expected result"

