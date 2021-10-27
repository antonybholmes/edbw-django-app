from rest_framework import serializers

from api.persons.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'first_name', 'last_name', 'email')
