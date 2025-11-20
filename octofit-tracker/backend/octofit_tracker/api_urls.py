from rest_framework import generics, serializers
from django.contrib.auth import get_user_model
from djongo import models
from django.urls import path

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'user']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'difficulty']

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardList(generics.ListAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutList(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

urlpatterns = [
    from rest_framework.response import Response
    from rest_framework.decorators import api_view

    @api_view(['GET'])
    def api_root(request):
        return Response({
            'users': '/api/users/',
            'teams': '/api/teams/',
            'activities': '/api/activities/',
            'leaderboard': '/api/leaderboard/',
            'workouts': '/api/workouts/',
        })

    urlpatterns = [
        path('', api_root, name='api-root'),
        path('users/', UserList.as_view()),
        path('teams/', TeamList.as_view()),
        path('activities/', ActivityList.as_view()),
        path('leaderboard/', LeaderboardList.as_view()),
        path('workouts/', WorkoutList.as_view()),
    ]
]
