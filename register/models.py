from django.db import models


# Create your models here.

class data(models.Model):
    name   = models.CharField(max_length=50)
    id_man = models.CharField(max_length=50)
    image = models.BinaryField(max_length=1000000)
    vector = models.BinaryField(max_length=1000000)
    def __str__(self):
        return self.name

# class data(models.Model):
#     name   = models.CharField(max_length=50)
#     id_man = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
#
# class image(models.Model):
#     id_image = models.ForeignKey(data,on_delete=models.CASCADE)
#     image = models.BinaryField(max_length=1000000)
#     def __str__(self):
#         return self.image
#
# class vector(models.Model):
#     id_vector = models.ForeignKey(data,on_delete=models.CASCADE)
#     vector = models.BinaryField(max_length=1000000)
#     def __str__(self):
#         return self.vector

