from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from series.api.serializers import SerieSerializer
from series.models import Serie


class SeriesViewset(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        series = SerieSerializer(Serie.objects.all(), many=True)
        return Response(data=series.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        serie = get_object_or_404(Serie, pk=pk)
        return Response(data=SerieSerializer(serie).data, status=status.HTTP_200_OK)

    def create(self, request):
        serie_serializer = SerieSerializer(data=request.POST)
        serie_serializer.is_valid(raise_exception=True)

        serie_serializer.save()
        return self.list(request)
