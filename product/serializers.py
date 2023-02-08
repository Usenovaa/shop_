from rest_framework import serializers
from .models import Category, Product
from review.serializers import RatingSerializer, CommentSerializer
from django.db.models import Avg


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price <=0:
            raise serializers.ValidationError(
                'price must be > 0'
            )
        return price

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = [i.body for i in instance.comments.all()]
        # print(CommentSerializer(instance.comments.all(),many=True).data)
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'
                                                        ))['rating__avg']
        representation['likes_count'] = instance.likes.count()

        return representation
