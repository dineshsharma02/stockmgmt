from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path('',views.index,name="stock_receipt"),
    path('update-receipt/<int:id>',views.update_receipt,name="update_receipt"),
    path('delete-receipt/<int:id>',views.delete_receipt,name="delete_receipt"),
    path('search-between/',views.search_dates,name="search_between"),
    path('search_last_seven_days/',views.search_last_seven_days,name="search_last_seven_days"),
    path('search_last_month/',views.search_last_month,name="search_last_month"),
    path('search_this_month/',views.search_this_month,name="search_this_month"),
    path('search_this_year/',views.search_this_year,name="search_this_year"),
    
    
]