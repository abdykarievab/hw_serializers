from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Position(models.Model):
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class Employee(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
