import datetime

CENTURY_MAP = {
    0: (1900, 0),
    1: (2000, 20),
    2: (2100, 40),
    3: (2200, 60),
    4: (1800, 80),
}


def get_birth_date_from_pesel(pesel: str) -> datetime.date | None:
    month_with_century = int(pesel[2:4])
    century_code = month_with_century // 20
    base_year, month_offset = CENTURY_MAP.get(century_code, (1900, 0))

    year = int(pesel[0:2]) + base_year
    month = month_with_century - month_offset
    day = int(pesel[4:6])

    return datetime.date(year, month, day)


def get_gender_from_pesel(pesel: str) -> str:
    gender_digit = int(pesel[9])
    if gender_digit % 2 == 1:
        return "Male"
    return "Female"
