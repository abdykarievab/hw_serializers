from rest_framework import serializers
from .models import Customer, Comment, Position, Employee


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.content = validated_data.get('content')
        instance.created = validated_data.get('created')
        instance.save()
        return instance


class PositionSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position = validated_data.get('position')
        instance.department = validated_data.get('department')
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birth_year = serializers.IntegerField()
    position_id = serializers.IntegerField()
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.birth_year = validated_data.get('birth_year')
        instance.position_id = validated_data.get('position')
        instance.salary = validated_data.get('salary')
        instance.save()
        return instance
