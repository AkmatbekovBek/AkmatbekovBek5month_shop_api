from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_api_view),
    path('<int:category_id>/', views.category_detail_api_view),

    path('', views.product_list_api_view),
    path('<int:product_id>/', views.product_detail_api_view),

    path('', views.review_list_api_view),
    path('<int:review_id>/', views.review_detail_api_view),
 ]
