from rest_framework import viewsets

# Serializers
from api.serializers import ManuscriptSerializer, TextSerializer

# Models
from manuscripts.models import Manuscript
from commentaries.models import Text


class ManuscriptViewSet(viewsets.ModelViewSet):
    """
    Endpoint returning manuscript objects
    """
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer


class TextViewSet(viewsets.ModelViewSet):
    """
    Endpoint returning text objects
    """
    queryset = Text.objects.all()
    serializer_class = TextSerializer
