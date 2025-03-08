from django.urls import path
from .views import ScrapeView

urlpatterns = [
    path("scrape-summarize/", ScrapeView.as_view(), name="scrape_summarize"),
]
