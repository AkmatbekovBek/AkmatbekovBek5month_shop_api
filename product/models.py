from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title


STARS = (
    (1, '*' *1),
    (2, '*' *2),
    (3, '*' *3),
    (4, '*' *4),
    (5, '*' *5),
)
class Review(models.Model):
    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=1)

    def __str__(self):
        return self.text




