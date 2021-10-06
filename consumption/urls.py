from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="stock_exp"),
    path('update-exp/<int:id>',views.update_exp,name="update_exp"),
    path('delete-exp/<int:id>',views.delete_exp,name="delete_exp"),
]