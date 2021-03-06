from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.db.models import Avg
from series.models import Episode, Score, Serie, ScoreEpisode


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'title', 'description',)


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'name',)


class DetailSerieSerializer(serializers.ModelSerializer):
    ## Anidación de serializers
    # episodes = EpisodeSerializer(
    #     source='episode_set',
    #     many=True)
    episodes = SerializerMethodField()
    score = SerializerMethodField()
    def get_score(self, serie: Serie) -> int:
        return Score.objects.filter(serie=serie.pk).aggregate(score=Avg('score')).get('score')


    def get_episodes(self, instance):
        return list(instance.episode_set.values('id', 'name'))



    class Meta:
        model = Serie
        fields = ('id', 'title', 'description', 'episodes', 'score')


class ScoreSerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('id', 'score', 'user', 'serie')



class ScoreEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreEpisode
        fields = ('id', 'episode', 'user', 'score')




    # title = serializers.CharField(required=True)
    # description = serializers.CharField(required=True)
    # id = serializers.IntegerField(read_only=True)

    # def validate_title(self, title: str):
    #     series = Serie.objects.filter(title=title)
    #     if series.exists():
    #         raise ValidationError('The title already exists')
    #     return title

    # def validate_description(self, description: str):
    #     if not description:
    #         raise ValidationError('The description cannot be blank')
    #     return description

    # def create(self, **kwargs) -> Serie:
    #     serie = Serie.objects.create(**self.validated_data)
    #     return serie

    # def update(self, **kwargs) -> Serie:
    #     for attr, value in self.validated_data.items():
    #         setattr(self.instance, attr, value)

    #     self.instance.save()
    #     return self.instance

    # def save(self, **kwargs):
    #     if self.instance is not None:
    #         self.instance = self.update()
    #     else:
    #         self.instance = self.create()

    #     return self.instance
