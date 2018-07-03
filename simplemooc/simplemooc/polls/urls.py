from django.urls import path
from simplemooc.polls.views import home

urlpatterns = [
	path('', home),
    
]