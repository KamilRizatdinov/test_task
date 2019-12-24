from rest_framework import serializers

from app.models import Subject


class SubjectSerializer(serializers.Serializer):
    inn = serializers.CharField(max_length=10)
    ogrn = serializers.CharField(max_length=13)
    request_time = serializers.DateTimeField()
    registration_date = serializers.CharField(max_length=50)
    name_ex = serializers.CharField(max_length=500)

    def create(self, validated_data):
        """
        Create and return a new `Subject` instance, given the validated data.
        """
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Subject` instance, given the validated data.
        """
        instance.inn = validated_data.get('inn', instance.inn)
        instance.ogrn = validated_data.get('ogrn', instance.ogrn)
        instance.request_time = validated_data.get('request_time', instance.request_time)
        instance.registration_date = validated_data.get('registration_date', instance.registration_date)
        instance.name_ex = validated_data.get('name_ex', instance.name_ex)
        instance.save()
        return instance
