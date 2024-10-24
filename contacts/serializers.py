from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_phone_number(self, value):
        if not value.startswith('+') or not value[1:].isdigit():
            raise serializers.ValidationError("The phone number must start with '+' and contain only numbers.")
        return value