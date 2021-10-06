from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="stock_receipt"),
    path('update-receipt/<int:id>',views.update_receipt,name="update_receipt"),
    path('delete-receipt/<int:id>',views.delete_receipt,name="delete_receipt"),
]