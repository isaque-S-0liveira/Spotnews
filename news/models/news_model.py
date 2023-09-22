from django.db import models
from . import Categories, Users
from news.validators import validate_title


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, blank=False, validators=[validate_title]
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="news",
    )
    created_at = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        Categories,
        related_name="news",
    )

    def __str__(self):
        return self.title
