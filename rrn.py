import itertools
import re
from datetime import datetime


HYPHEN = re.compile('[-–]')

BIRTH = 0, 6
BIRTH_DATE_FORMAT = '%y%m%d'

LOC = 7, 9
MAX_LOC = 97

HASH = 12
HASH_BASE = 11


def _validate_birth(rrn: str) -> bool:
    try:
        return datetime.strptime(
            rrn[slice(*BIRTH)],
            BIRTH_DATE_FORMAT
        ) is not None
    except ValueError:
        return False


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
    Validate given RRN and returns if it is valid or not.
    RRN should include at least 6 digits(birthday part).
    Otherwise, it would be somewhat meaningless.

    :param rrn: RRN string
    :type rrn: str
    :return: validity
    :rtype: bool
    """
    try:
        rrn = HYPHEN.sub('', rrn)
        assert rrn.isdigit() and len(rrn) >= BIRTH[1]

        return (
            _validate_birth(rrn) and
            _validate_location(rrn) and
            _validate_hash(rrn)
        )
    except AssertionError:
        raise ValueError


def is_corresponding_rrn(rrn: str, **kwargs) -> bool:
    pass
