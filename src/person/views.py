from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import JSONRenderer
from .serializers import PersonSerializer
from .models import PersonModel


class PersonAllAPIView(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
    renderer_classes = [JSONRenderer]


class PersonAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
    renderer_classes = [JSONRenderer]
