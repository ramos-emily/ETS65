from django.urls import path
from .views import PatoListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('patos/', PatoListCreateAPIView.as_view(), name='pato-list-create'),
    path('patos/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(), name='pato-especifico'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)