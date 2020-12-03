from django.urls import path
from . import views

urlpatterns = [

    # views.home is a function in the views class thats why we imported it from above
    # now if someone wants to go home this is what they will see
    # this is not enough you also have to go to the projects ulr and also let it know about this app as the projects url is the core mapping to every app
    path('', views.home, name='home'), 
    path('add', views.add, name='add')
]
