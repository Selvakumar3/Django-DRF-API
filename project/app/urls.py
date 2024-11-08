from django.urls import path
from .import views

urlpatterns = [
    
    path('index/',views.index,name='index'),
    path('retrieve/',views.retrieve,name='retrieve'),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('popup/',views.popup,name="popup"),
]
