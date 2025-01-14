from django.urls import path
from .views import about, contact, home, psl_details

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('<int:psl_id>/', psl_details, name='psl_details'),


]
