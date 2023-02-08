from rest_framework import serializers
from .models import Like, Rating, Comment, LikeComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        user = requests.user
        comment = Comment.objects.create(
            author=user,
            **validated_data)
        return comment


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                'Рейтинг не может быть'
                ' меньше 0 или больше 5 '
            )
        return rating

    def validate_product(self, product):
        if self.Meta.model.objects.filter(
            product=product
        ).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на данный продукт'
            )
        return product

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating



class LikeSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        print('===================')
        print(user)
        print('===================')
        like = Like.objects.create(author=user, **validated_data)
        return like


class LikeCommentSerializer(serializers.ModelSerializer):
    comment = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = LikeComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        like_comment = LikeComment.objects.create(author=user, **validated_data)
        return like_comment



    
