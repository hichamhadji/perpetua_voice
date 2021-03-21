from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.filters import BaseFilterBackend
from . import serializers as playlist_serializers
from .pagination import CustomPagination
import coreapi
import requests
from rest_framework.response import Response
from django.conf import settings



class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='category',
            location='query',
            required=True,
            type='string'
        )]




class PlayListViewSet(viewsets.ViewSet):

    filter_backends = (SimpleFilterBackend,)


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['set_password',]:
            serializer_class  = playlist_serializers.PlayListSerializer

        return serializer_class


    def list(self, request,*args, **kwargs):
        song=dict()
        playlist=[]
        category=request.GET.get('category')
        for i in range(2):
            track=get_track(category,i)
            if track:
                lyrics=get_lyrics(track['track_id'])
                song['title']= track['track_name']
                song['artist']= track['artist_name']
                song['lyrics']=lyrics
                playlist.append(song)
                song=dict()
                new_query=get_random_words(lyrics)
        serializer = playlist_serializers.PlayListSerializer(data=playlist,many=True)
        if serializer.is_valid(): 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




def get_track(category,i):
    tracks_payload={'format':'json','q_lyrics':category,'quorum_factor':'1','apikey':settings.MUSIC_MATCH_API_KEY}
    tracks_response= requests.get(settings.MUSIC_MATCH_TRACKS, params=tracks_payload)
    track=tracks_response.json()['message']['body']['track_list'][:2][i]['track']
    return track

def get_lyrics(track_id):
    lyrics_payload={'format':'json','track_id':track_id,'quorum_factor':'1','apikey':settings.MUSIC_MATCH_API_KEY}
    lyrics_response= requests.get(settings.MUSIC_MARTCH_LYRICS, params=lyrics_payload)
    lyrics= lyrics_response.json()['message']['body']['lyrics']['lyrics_body']
    return lyrics

def get_random_words(lyrics):
    pass