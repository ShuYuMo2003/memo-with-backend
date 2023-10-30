from rest_framework import serializers
from .models import GENDER_TYPE, Person

class GetPersonInfoSerializer(serializers.Serializer):
    name                = serializers.CharField(max_length=100, required=False, allow_null=True)
    birthdate           = serializers.DateField(required=False, allow_null=True)
    gender              = serializers.ChoiceField(choices=[i[0] for i in GENDER_TYPE], required=False, allow_null=True)

    lost_place          = serializers.CharField(required=False, allow_null=True)
    lost_date           = serializers.DateField(required=False, allow_null=True)

    family_name         = serializers.CharField(required=False, allow_null=True)

class SaveOrUpdatePersonInfoRequestSerializer(serializers.Serializer):
    id                  = serializers.IntegerField(required=False, allow_null=True)
    name                = serializers.CharField(max_length=100)
    birthdate           = serializers.DateField(required=False, allow_null=True)
    photos_uuid         = serializers.ListSerializer(child=serializers.UUIDField(), required=False, allow_null=True, max_length=10)
    gender              = serializers.ChoiceField(choices=[i[0] for i in GENDER_TYPE], required=False, allow_null=True)

    lost_place          = serializers.CharField(required=False, allow_null=True, max_length=1000)
    lost_date           = serializers.DateField(required=False, allow_null=True)

    family_name         = serializers.CharField(required=False, allow_null=True, max_length=100)
    family_phone        = serializers.CharField(required=False, allow_null=True, max_length=100)
    family_email        = serializers.EmailField(required=False, allow_null=True, max_length=100)
    family_address      = serializers.CharField(required=False, allow_null=True, max_length=1000)

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'