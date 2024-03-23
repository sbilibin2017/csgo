import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID


class ClickhouseNullValues(Enum):
    UUID = UUID('00000000-0000-0000-0000-000000000000')
    STR = ''
    DATE = datetime.date(datetime.strptime('1970-01-01', '%Y-%m-%d'))
    DATETIME = datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    INT = 0
    FLOAT = 0.0
    DECIMAL = Decimal(0.0)
