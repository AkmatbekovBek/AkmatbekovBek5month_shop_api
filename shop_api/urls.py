from django.contrib import admin
from django.urls import path, include
from product import views
from .swagger import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('users.urls'))
]

urlpatterns += swagger_urlpatterns




# path('api/v1/categories/', views.category_list_api_view),
#     path('api/v1/categories/<int:category_id>/', views.category_detail_api_view),
#     path('api/v1/products/', views.product_list_api_view),
#     path('api/v1/products/<int:product_id>/', views.product_detail_api_view),
#     path('api/v1/reviews/', views.review_list_api_view),
#     path('api/v1/reviews/<int:review_id>/', views.review_detail_api_view)