from rest_framework import serializers

from app5.models import Student


# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('url', 'id', 'name', 'grade', 'score')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'grade', 'score')