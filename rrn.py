import itertools
import re
from datetime import datetime


HYPHEN = re.compile('[-–]')

BIRTH = 0, 6
MONTH_OF_BIRTH = 0, 4
MONTH_OF_BIRTH_FORMAT = '%y%m'
DAY_OF_BIRTH_FORMAT = '%y%m%d'

LOC = 7, 9
MAX_LOC = 97

HASH = 12
HASH_BASE = 11


def _validate_month_of_birth(rrn: str) -> bool:
    try:
        return datetime.strptime(
            rrn[slice(*MONTH_OF_BIRTH)].ljust(MONTH_OF_BIRTH[1], '1'),
            MONTH_OF_BIRTH_FORMAT
        ) is not None if len(rrn) >= 3 else True
    except ValueError:
        return False


def _validate_day_of_birth(rrn: str) -> bool:
    try:
        return datetime.strptime(
            rrn[slice(*BIRTH)].ljust(BIRTH[1], '0'),
            DAY_OF_BIRTH_FORMAT
        ) is not None if len(rrn) >= 5 else True
    except ValueError:
        return False


def _validate_birth(rrn: str) -> bool:
    return _validate_month_of_birth(rrn) and _validate_day_of_birth(rrn)


def _validate_location(rrn: str) -> bool:
    try:
        return int(rrn[slice(*LOC)]) < MAX_LOC
    except (TypeError, ValueError):
        return True


def _validate_hash(rrn: str) -> bool:
    try:
        h = int(rrn[HASH])
        s = sum(
            a * int(b) for a, b in zip(
                itertools.cycle(range(2, 10)),
                rrn[:HASH]
            )
        )
        expected = (HASH_BASE - (s % HASH_BASE)) % 10
        return h == expected
    except IndexError:
        return True


def is_valid_rrn(rrn: str) -> bool:
    """
    Validate given RRN and returns if it might be valid or not.

    :param rrn: RRN string
    :type rrn: str
    :return: validity
    :rtype: bool
    """
    try:
        rrn = HYPHEN.sub('', rrn)
        return (
            rrn.isdigit() and
            _validate_birth(rrn) and
            _validate_location(rrn) and
            _validate_hash(rrn)
        )
    except TypeError:
        return False


def is_corresponding_rrn(rrn: str) -> bool:
    pass
