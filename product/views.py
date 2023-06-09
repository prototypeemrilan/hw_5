from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product,Review
from .serializers import CategorySerializer,ProductSerializer,ReviewSerializer

@api_view(['GET'])
def category_api_view(requests):
    shop = Category.objects.all()
    serializers = CategorySerializer(shop, many=True)
    return Response(data=serializers.data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! У ВАС ОШИБКА ТАКОЙ СТРАНИЦЫ НЕТ")
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def products_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! У ВАС ОШИБКА ТАКОЙ СТРАНИЦЫ НЕТ")
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)

@api_view(['GET'])
def reviews_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! У ВАС ОШИБКА ТАКОЙ СТРАНИЦЫ НЕТ")
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)

