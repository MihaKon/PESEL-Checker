import datetime

from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PeselCheckForm


class PeselCheckView(FormView):
    form_class = PeselCheckForm
    template_name = "check_form.html"
    success_url = reverse_lazy("pesel_checker:check")

    def form_valid(self, form: PeselCheckForm):
        birth_date: datetime.date = form.cleaned_data.get("birth_date")
        gender = form.cleaned_data.get("gender")

        context = self.get_context_data(
            form=form,
            is_valid=True,
            extracted_data=dict(
                gender=gender,
                day=birth_date.day,
                month=birth_date.month,
                year=birth_date.year,
            ),
        )

        return self.render_to_response(context)

    def form_invalid(self, form: PeselCheckForm):
        context = self.get_context_data(
            form=form,
            is_valid=False,
        )
        return self.render_to_response(context)
