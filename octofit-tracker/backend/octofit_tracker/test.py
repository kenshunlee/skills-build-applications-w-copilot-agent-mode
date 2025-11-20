from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='TestActivity', user='TestUser')
        self.assertEqual(activity.name, 'TestActivity')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='TestTeam', points=10)
        self.assertEqual(lb.points, 10)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')
