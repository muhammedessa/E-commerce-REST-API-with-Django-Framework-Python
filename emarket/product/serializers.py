from rest_framework import serializers
from .models import Product,Review


class ProductSerializer(serializers.ModelSerializer):
    
    reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
      #  fields = ('name', 'price','brand')

    def get_reviews(self,obj):
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
     