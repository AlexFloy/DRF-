from rest_framework import serializers
from .models import Contact, Events


class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class EventContactList(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name']


class EventsSerializers(serializers.ModelSerializer):
    contacts = EventContactList(many=True, read_only=True)

    def validate_location(self, data):
        if data['location'] == 'росія':
            raise serializers.ValidationError("У ПІДАРІВ НІЧОГО НЕ ПРОВОДИМО!")
        return data

    class Meta:
        model = Events
        fields = ['title', 'description', 'date_time', 'location', 'contacts']
