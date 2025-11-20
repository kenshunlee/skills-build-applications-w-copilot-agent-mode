from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()

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

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })
