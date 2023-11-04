from rest_framework import serializers
from .models import GENDER_TYPE, Person

class GetPersonInfoRequestSerializer(serializers.Serializer):
    name                = serializers.CharField(max_length=100)

class SaveOrUpdatePersonInfoRequestSerializer(serializers.Serializer):
    token               = serializers.CharField()
    id                  = serializers.IntegerField(required=False, allow_null=True)
    name                = serializers.CharField(max_length=100)
    birthdate           = serializers.DateField(required=False, allow_null=True)
    photo_files         = serializers.ListSerializer(child=serializers.CharField(), required=False, allow_null=True, max_length=10)
    gender              = serializers.ChoiceField(choices=[i[0] for i in GENDER_TYPE], required=False, allow_null=True)

    lost_place          = serializers.CharField(required=False, allow_null=True, max_length=1000)
    lost_date           = serializers.DateField(required=False, allow_null=True)

    family_name         = serializers.CharField(required=False, allow_null=True, max_length=100)
    family_phone        = serializers.CharField(required=False, allow_null=True, max_length=100)
    family_email        = serializers.EmailField(required=False, allow_null=True, max_length=100)
    family_address      = serializers.CharField(required=False, allow_null=True, max_length=1000)

class SetPublicRequestSerializer(serializers.Serializer):
    id                  = serializers.IntegerField()
    is_public           = serializers.BooleanField()
    token               = serializers.CharField()


class GetAllPersonRequestSerializer(serializers.Serializer):
    token              = serializers.CharField()

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
