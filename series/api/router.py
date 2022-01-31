from rest_framework.routers import DefaultRouter

from series.api.views import EpisodesViewset, ScoresViewset, SeriesViewset

router = DefaultRouter()

router.register(prefix='series', basename='series', viewset=SeriesViewset)
router.register(prefix='episodes', basename='episode', viewset=EpisodesViewset)
router.register(prefix='scores', basename='score', viewset=ScoresViewset)