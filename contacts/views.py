from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import status, filters, viewsets
from rest_framework.viewsets import ModelViewSet
from django.http import Http404

from .models import Contact, Events
from .serializers import ContactSerializers, EventsSerializers


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'city']


class ContactCrate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactUpdate(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactDestroy(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactRetrieve(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class EventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['contacts']

