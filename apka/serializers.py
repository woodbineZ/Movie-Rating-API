
from rest_framework import serializers
from .models import Movie, Rating, Actors, Directors
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'actors', 'directors', 'premiere', 'updated', 'number_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ('id', 'name', 'surname')

class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = ('id', 'name', 'surname')