from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('import/', ImportBook),
    path('search/', searchbook),
    path('issue/<int:id>/', issuebook, name='bookissue'),
    path('return/', returnbook),
]