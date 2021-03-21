from rest_framework import serializers




class PlayListSerializer(serializers.Serializer):
    """
        Serializer for playlist endpoint.
    """
    title= serializers.CharField(required=True)
    artist= serializers.CharField(required=True)
    lyrics= serializers.CharField(required=True)