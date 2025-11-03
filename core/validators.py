from django.core.exceptions import ValidationError

from .pesel_utils import get_birth_date_from_pesel

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def _validate_birth_date(pesel: str):
    try:
        get_birth_date_from_pesel(pesel)
    except ValueError:
        raise ValidationError(
            "Invalid birth date encoded in PESEL.", code="invalid_date"
        )


def _validate_digits(pesel: str):
    if not pesel.isdigit():
        raise ValidationError(
            "PESEL contains invalid characters.", code="invalid_chars"
        )


def _validate_length(pesel: str):
    if len(pesel) != 11:
        raise ValidationError(
            "PESEL must contain exactly 11 digits.", code="invalid_length"
        )


def _validate_checksum(pesel: str):
    digits = [int(d) for d in pesel]
    control_sum = sum(d * w for d, w in zip(digits[:10], WEIGHTS))
    control_digit_calculated = (10 - (control_sum % 10)) % 10
    control_digit_given = digits[10]
    if control_digit_calculated != control_digit_given:
        raise ValidationError("Invalid PESEL checksum.", code="invalid_checksum")


def validate_pesel(pesel: str):
    _validate_digits(pesel)
    _validate_length(pesel)
    _validate_birth_date(pesel)
    _validate_checksum(pesel)
