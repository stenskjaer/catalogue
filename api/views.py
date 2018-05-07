from rest_framework import viewsets

# Serializers
from api.serializers import ManuscriptSerializer, TextSerializer, ContentSerializer

# Models
from manuscripts.models import Manuscript, ManuscriptContentCommentary
from commentaries.models import Text


class ManuscriptContentViewSet(viewsets.ModelViewSet):
    """
    Endpoint returning the content of manuscripts.
    """
    queryset = ManuscriptContentCommentary.objects.all()
    serializer_class = ContentSerializer
    

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
