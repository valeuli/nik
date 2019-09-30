from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.models import UserProfile
from rest_framework.validators import UniqueValidator
from phonenumber_field.serializerfields import PhoneNumberField
from django_countries.serializer_fields import CountryField
from profiles.models import GENDER_CHOICES
from api.v1.serializers.education import EducationSerializers
from api.v1.serializers.experience import ExperienceSerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password', 'phone_number', 'country', 'gender', 'title')
    
    first_name = serializers.CharField(
        required=True, write_only=True
    )
    last_name = serializers.CharField(
        required=True, write_only=True
    )
    username = serializers.CharField(
        required=True, write_only=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True, write_only=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True, write_only=True
    )
    phone_number = PhoneNumberField(
        required=False, write_only=True
    )
    country = CountryField(
        required=True, write_only=True
    )
    gender = serializers.ChoiceField(
        choices=GENDER_CHOICES, required=True
    )
    title = serializers.CharField(
        write_only=True, required=True
    )

    def create(self, validated_data):
        user = User.objects.create_user(
                        validated_data['username'],
                        password=validated_data['password'],
                        first_name=validated_data['first_name'],
                        last_name=validated_data['last_name'],
                        email=validated_data['email'],
        )
        UserProfile.objects.create(
                        user=user,
                        country=validated_data('country'),
                        gender=validated_data('gender'),
                        title=validated_data('title'),
                        phone_number=validated_data('phone_number')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'gender',
            'title',
            'country',
            'experience',
            'education'
        )
    phone_number = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    experience = ExperienceSerializer(many=True)
    education = EducationSerializers(many=True)

    @staticmethod
    def get_phone_number(user):
        return user.profile.phone_number

    @staticmethod
    def get_title(user):
        return user.profile.title

    @staticmethod
    def get_gender(user):
        return user.profile.gender

    @staticmethod
    def get_country(user):
        return user.profile.country
