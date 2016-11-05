from rest_framework import serializers

from manuscripts.models import Manuscript, ManuscriptContentCommentary
from commentaries.models import Text


class ManuscriptSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    town = serializers.StringRelatedField()
    library = serializers.StringRelatedField()

    class Meta:
        model = Manuscript
        fields = ('id', 'country', 'town', 'library', 'shelfmark', 'number', 'date', 'date_earliest', 'date_latest',
                  'saeculo')
        depth = 2


class TextSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Text
        fields = ('id', 'author', 'authorship', 'title', 'date', 'saeculo', 'before', 'after')
