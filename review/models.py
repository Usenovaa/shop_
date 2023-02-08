from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product


User = get_user_model()


class Comment(models.Model):
    body = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.body


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.product}Liked by{self.author.name}'


class LikeComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.comment}Liked by{self.author.username}'



class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ratings'
    )

    def __str__(self) -> str:
        return f'{self.rating} -> {self.product}'