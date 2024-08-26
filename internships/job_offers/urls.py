from django.urls import path
from django.views.generic import TemplateView


app_name = "job_offers"
urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="job_offers/index.html"),
        name="main_page",
    ),
]
