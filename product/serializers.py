from rest_framework import serializers
from product.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class ProductSerializer(serializers.ModelSerializer):

    stars = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        #depth = 1



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'





class CategoryCreateValidateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=3)
    class Meta:
        model = Category
        fields = ['id', 'name']


    def create_validated_data(self):
        validated = self.validated_data
        return {
            'name': validated['name']
        }

class ProductCreateValidateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, min_length=3, max_length=70)
    description = serializers.CharField(required=False, default='There is no description in this product!')
    price = serializers.IntegerField(required=True)
    category = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create_validated_data(self):
        validated = self.validated_data
        return {
            'title': validated['title'],
            'description': validated['description'],
            'price': validated['price'],
            'category': validated['category']
        }
class ReviewCreateValidateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True, min_length=15)
    product = serializers.CharField(required=True)
    stars = serializers.IntegerField(required=True)

    class Meta:
        model = Review
        fields = '__all__'

    def create_validated_data(self):
        validated = self.validated_data
        return {
            'text': validated['text'],
            'product': validated['product'],
            'stars': validated['stars']
        }
