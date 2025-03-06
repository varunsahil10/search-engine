from django.urls import path
from fulltextsearch.views import *

urlpatterns = [
    path('', home, name='home'),
    path('trigram', trigramsearch, name='trigramsearch'),
]
