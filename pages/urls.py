from django.urls import path
from .views import HomePageView, SeoPage,report_page
urlpatterns = [
# path("", HomePageView.as_view(), name="home"),
path("", SeoPage.as_view(), name="seo"),
path("report/", report_page.as_view(), name="report"),


]