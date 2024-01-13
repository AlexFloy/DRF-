from django.contrib import admin
from .views import ContactList, ContactCrate, ContactRetrieve, ContactUpdate, ContactDestroy, EventsView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', EventsView, basename='events')

urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('create/', ContactCrate.as_view(), name='create_contact'),
    path('<int:pk>/', ContactRetrieve.as_view(), name='contact_retrieve'),
    path('<int:pk>/delete/', ContactDestroy.as_view(), name='contact_delete'),
    path('<int:pk>/update/', ContactUpdate.as_view(), name='contact_update'),
    path('events/', include(router.urls))
]
