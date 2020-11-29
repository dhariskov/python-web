from django.db import models


# Create your models here.
class Pet(models.Model):
    type = models.CharField(max_length=6, choices=[('dog', 'dog'), ('cat', 'cat'), ('parrot', 'parrot')])
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False, default='desc')
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f'{self.name}, with age {self.age} and desc: {self.description}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()

