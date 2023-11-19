from django.urls import path

from .views import (
    ProductListAPIView,
    ProductDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, ReviewListAPIView, ReviewDetailAPIView,
    ProductReviewListAPIView,
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),

    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('review/', ReviewListAPIView.as_view()),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('product_review/', ProductReviewListAPIView.as_view()),
    ]