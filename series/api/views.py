from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from series.api.serializers import DetailSerieSerializer, ScoreSerieSerializer, EpisodeSerializer, SerieSerializer
from series.models import Serie, Episode, Score
from series.api.permissions import IsMeOrReadOnly


class EpisodesViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

class ScoresViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ScoreSerieSerializer
    queryset = Score.objects.all()


class SeriesViewset(ModelViewSet):
    permission_classes = [IsMeOrReadOnly]
    serializer_class = SerieSerializer
    queryset = Serie.objects.all()

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == 'retrieve':
            serializer = DetailSerieSerializer
        if self.action == 'set_score':
            serializer = ScoreSerieSerializer
        return serializer

    @action(
        detail=True,
        methods=['PUT'],
        url_path='set-score',
        permission_classes = [IsMeOrReadOnly])
    def set_score(self, request, pk: int):
        data = {'serie': pk,
                'user': request.user.pk,
                'score': int(request.POST['score'])}

        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_200_OK)

    # ViewSets
    # def list(self, request):
    #     series = SerieSerializer(Serie.objects.all(), many=True)
    #     return Response(data=series.data, status=status.HTTP_200_OK)

    # def retrieve(self, request, pk=None):
    #     serie = get_object_or_404(Serie, pk=pk)
    #     return Response(data=SerieSerializer(serie).data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     serie_serializer = SerieSerializer(data=request.POST)
    #     serie_serializer.is_valid(raise_exception=True)

    #     serie_serializer.save()
    #     return self.list(request)
