from app1 . views import *
from django . urls import path

app_name = 'somethingsomething'

urlpatterns= [
    path('ram/',ram,name='ram'),
]
