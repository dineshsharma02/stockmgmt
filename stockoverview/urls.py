from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name="stock_overview"),
    path('search-between/',views.search_dates,name="search_between_all"),
    path('search_last_seven_days/',views.search_last_seven_days,name="search_last_seven_days_all"),
    path('search_last_month/',views.search_last_month,name="search_last_month_all"),
    path('search_this_month/',views.search_this_month,name="search_this_month_all"),
    path('search_this_year/',views.search_this_year,name="search_this_year_all"),
    path('search_in_overview',csrf_exempt(views.search_in_overview),
         name="search_in_overview")
]