from profiles.models import Experience
from django.contrib.auth.models import User
from rest_framework import serializers


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('title', 'employment_type', 'company', 'country', 'start_date',
                  'end_date', 'current_work ')

    def create(self, validated_data):
        experience = Experience.objects.create(
            title=validated_data['title'], employment_type=validated_data['employment_type'],
            company=validated_data['company'], country=validated_data['country'],
            start_date=validated_data['start_date'], end_date=validated_data['end_date'],
            current_work=validated_data['current_work'], user=self.context.get('request').user
        )
        return experience
