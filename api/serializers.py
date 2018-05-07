from rest_framework import serializers

from manuscripts.models import Manuscript, ManuscriptContentCommentary
from commentaries.models import Text


class ContentSerializer(serializers.ModelSerializer):
    manuscript = serializers.StringRelatedField()
    content = serializers.StringRelatedField()

    class Meta:
        model = ManuscriptContentCommentary
        fields = ('manuscript', 'content', 'folios')


class ManuscriptSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    town = serializers.StringRelatedField()
    library = serializers.StringRelatedField()
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Manuscript
        fields = ('id', 'country', 'town', 'library', 'shelfmark', 'number', 'date', 'date_earliest', 'date_latest',
                  'saeculo', 'content')
        depth = 1


class TextSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Text
        fields = ('id', 'author', 'authorship', 'title', 'date', 'saeculo', 'before', 'after')
