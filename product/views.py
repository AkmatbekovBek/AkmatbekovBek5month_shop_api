from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer



#Category----------------------------------------------------
@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    categoryes_json = CategorySerializer(categories, many=True).data
    return Response(data=categoryes_json)

@api_view(['GET'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response(data={'message': 'Category not Found!'}, status=404)
    category_json = CategorySerializer(category).data
    return Response(data=category_json)



#Product----------------------------------------------------
@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    products_json = CategorySerializer(products, many=True).data
    return Response(data=products_json)

@api_view(['GET'])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'message': 'Product not Found!'}, status=404)
    product_json = ProductSerializer(product).data
    return Response(data=product_json)



#Review----------------------------------------------------
@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    reviews_json = ReviewSerializer(reviews, many=True).data
    return Response(data=reviews_json)

@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review not Found!'}, status=404)
    review_json = ReviewSerializer(review).data
    return Response(data=review_json)
