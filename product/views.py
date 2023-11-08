from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CategoryCreateValidateSerializer, ProductCreateValidateSerializer, ReviewCreateValidateSerializer



#Category----------------------------------------------------
@api_view(['GET', 'POST'])
def category_list_api_view(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        categoryes_json = CategorySerializer(instance=categories, many=True).data
        return Response(data=categoryes_json)

    elif request.method == 'POST':

        #0
        serializer = CategoryCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,
                            data={'message': 'Request failed',
                                  'errors': serializer.errors})

        #1

        #2
        create_category = Category.objects.create(**serializer.create_validated_data())
        create_category.save()
        #3
        return Response(status=201,
                        data={'message': 'Category created',
                              'create_category': {'id': create_category.id,
                                                  'name': create_category.name}})



@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response(data={'message': 'Category not Found!'}, status=404)

    if request.method == 'GET':
        category_json = CategorySerializer(category).data
        return Response(data=category_json)

    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(status=201,
                        data={'message': 'Category updated'})

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204,
                        data={'message': 'Category Destoyed'})

    serializer = CategoryCreateValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400,
                        data={'message': 'Request failed',
                              'errors': serializer.errors})


#Product----------------------------------------------------
@api_view(['GET'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_json = ProductSerializer(products, many=True).data
        return Response(data=products_json)

    elif request.method == 'POST':
        # 0
        serializer = CategoryCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,
                            data={'message': 'Request failed',
                                  'errors': serializer.errors})
        #1

        #2
        create_product = Product.objects.create(**serializer.create_validated_data())
        create_product.save()
        #3
        return Response(status=201,
                        data={'message': 'Product created',
                              'create_product': {'id': create_product.id,
                                                 'title': create_product.title}})



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'message': 'Product not Found!'}, status=404)
    if request.method == 'GET':
        product_json = ProductSerializer(product).data
        return Response(data=product_json)

    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=201,
                        data={'message': 'Product updated'})

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204,
                        data={'message': 'Product Destoyed'})

    serializer = CategoryCreateValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400,
                        data={'message': 'Request failed',
                              'errors': serializer.errors})


#Review----------------------------------------------------
@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        reviews_json = ReviewSerializer(reviews, many=True).data
        return Response(data=reviews_json)

    elif request.method == 'POST':
        # 0
        serializer = CategoryCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400,
                            data={'message': 'Request failed',
                                  'errors': serializer.errors})
        #1

        #2
        create_review = Review.objects.create(**serializer.create_validated_data())
        create_review.save()
        #3
        return Response(status=201,
                        data={'message': 'Review created',
                              'create_review': {'id': create_review.id,
                                                'title': create_review.text}})



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review not Found!'}, status=404)
    if request.method == 'GET':
        review_json = ReviewSerializer(review).data
        return Response(data=review_json)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.product_id = request.data.get('product_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(status=201,
                        data={'message': 'Review updated'})

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204,
                        data={'message': 'Review Destoyed'})


    serializer = CategoryCreateValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400,
                        data={'message': 'Request failed',
                              'errors': serializer.errors})


