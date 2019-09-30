from profiles.models import Education
from rest_framework import serializers


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('school', 'degree', 'field_of_study', 'start_year', 'end_year', 'grade')

    def create(self, valited_data):
        education = Education.objects.create(
            school=valited_data['school'], degree=valited_data['degree'],
            field_of_study=valited_data['field_of_study'], start_year=valited_data['start_year'],
            end_year=valited_data['end_year'], grade=valited_data['grade'],
            user=self.context.get('request').user
        )
        return education
