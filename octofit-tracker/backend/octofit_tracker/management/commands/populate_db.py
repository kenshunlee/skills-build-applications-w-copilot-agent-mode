from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

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

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # 清空数据
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 创建团队
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # 创建用户
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass')

        # 创建活动
        Activity.objects.create(name='Run', user='ironman')
        Activity.objects.create(name='Swim', user='captain')
        Activity.objects.create(name='Fly', user='superman')
        Activity.objects.create(name='Drive', user='batman')

        # 创建排行榜
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # 创建锻炼
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', difficulty='Medium')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功填充测试数据'))
