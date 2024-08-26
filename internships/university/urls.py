from django.urls import path
from django.views.generic import TemplateView


app_name = "university"
urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="university/index.html"),
        name="main_page",
    ),
]
