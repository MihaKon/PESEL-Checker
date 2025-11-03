import pytest


@pytest.fixture
def valid_pesel():
    """
    Valid pesel:
    - Gender: Male
    - Day: 15
    - Month: 05
    - Year: 2005

    :return: Valid PESEL string.
    """
    return "05251512319"


@pytest.fixture
def invalid_pesel_checksum():
    return "05251512310"


@pytest.fixture
def invalid_pesel_birth_date():
    return "90113212315"
