from django.urls import path
from checker.views import CheckInsuranceNumberView

urlpatterns = [
    path("", CheckInsuranceNumberView.as_view(), name="checker"),
]
