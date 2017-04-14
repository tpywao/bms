from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=32)
#     detail = models.TextField(max_length=140)

#     def __str__(self):
#         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    # category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
