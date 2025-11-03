from django import forms

from .pesel_utils import get_birth_date_from_pesel, get_gender_from_pesel
from .validators import validate_pesel


class PeselCheckForm(forms.Form):
    pesel = forms.CharField(
        label="PESEL Number", min_length=11, max_length=11, validators=[validate_pesel]
    )

    def clean(self) -> dict:
        cleaned_data = super().clean()
        pesel = cleaned_data.get("pesel")

        if pesel is None:
            return cleaned_data

        birth_date = get_birth_date_from_pesel(pesel)
        gender = get_gender_from_pesel(pesel)

        cleaned_data["birth_date"] = birth_date
        cleaned_data["gender"] = gender

        return cleaned_data
