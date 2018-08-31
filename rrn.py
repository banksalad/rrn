import itertools
import re
from datetime import date, datetime
from typing import Optional


__version__ = '0.0.1'


HYPHEN = re.compile('[-–]')

BIRTH = 0, 6
MONTH_OF_BIRTH = 0, 4
MONTH_OF_BIRTH_FORMAT = '%y%m'
DAY_OF_BIRTH_FORMAT = '%y%m%d'

SEX = 6

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


def _is_birthday_corresponding(rrn: str, birthday: date) -> Optional[bool]:
    try:
        return datetime.strptime(
            rrn[slice(*BIRTH)],
            DAY_OF_BIRTH_FORMAT
        ).date() == birthday
    except (TypeError, ValueError):
        return None


def _is_sex_corresponding(rrn: str, female: bool) -> Optional[bool]:
    try:
        return (int(rrn[SEX]) % 2 == 0) == female
    except IndexError:
        return None


def _is_foreignness_corresponding(rrn: str, foreign: bool) -> Optional[bool]:
    try:
        return (5 <= int(rrn[SEX]) <= 8) == foreign
    except IndexError:
        return None


def is_corresponding_rrn(
    rrn: str,
    *,
    birthday: Optional[date]=None,
    foreign: Optional[bool]=None,
    female: Optional[bool]=None
) -> Optional[bool]:
    """
    Check given RRN if it corresponds with given information or not.
    It returns None if correspondence is undecidable.
    For example, 6-digit RRN string does not contain any information about sex.

    :param rrn: RRN string
    :param birthday: expected date of birth
    :param foreign: expected to be foreigner or not
    :param female: expected to be female or not
    :return: correspondence (None if it's undecidable)
    """
    try:
        rrn = HYPHEN.sub('', rrn)
        assert rrn.isdigit()
        return (
            (
                birthday is None or _is_birthday_corresponding(rrn, birthday)
            ) and
            (
                foreign is None or _is_foreignness_corresponding(rrn, foreign)
            ) and
            (
                female is None or _is_sex_corresponding(rrn, female)
            )
        )
    except (AssertionError, TypeError):
        return None
