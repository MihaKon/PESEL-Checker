import pytest
from django.core.exceptions import ValidationError

from core import validators


def test_checksum_does_not_raise_error_for_valid_pesel(valid_pesel: str):
    assert validators._validate_checksum(valid_pesel) is None


def test_checksum_raises_error_for_invalid_pesel(invalid_pesel_checksum: str):
    with pytest.raises(ValidationError):
        validators._validate_checksum(invalid_pesel_checksum)


def test_validate_birth_date_raises_error_for_invalid_pesel(
    invalid_pesel_birth_date: str,
):
    with pytest.raises(ValidationError):
        validators._validate_birth_date(invalid_pesel_birth_date)


def test_validate_birht_date_does_not_raises_eror_for_valid_pesel(valid_pesel: str):
    assert validators._validate_birth_date(valid_pesel) is None
