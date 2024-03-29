from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="stock_exp"),
    path('update-exp/<int:id>',views.update_exp,name="update_exp"),
    path('delete-exp/<int:id>',views.delete_exp,name="delete_exp"),
    path('search-between/',views.search_dates,name="search_between_exp"),
    path('search_last_seven_days/',views.search_last_seven_days,name="search_last_seven_days_exp"),
    path('search_last_month/',views.search_last_month,name="search_last_month_exp"),
    path('search_this_month/',views.search_this_month,name="search_this_month_exp"),
    path('search_this_year/',views.search_this_year,name="search_this_year_exp"),
]