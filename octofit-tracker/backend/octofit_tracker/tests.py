from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        team = Team.objects.create(name='Test Team2', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_create_activity(self):
        team = Team.objects.create(name='Test Team3', description='A test team')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-11-29')
        self.assertEqual(str(activity), 'Test User2 - Run on 2025-11-29')

    def test_create_workout(self):
        team = Team.objects.create(name='Test Team4', description='A test team')
        workout = Workout.objects.create(name='Test Workout', description='A test workout')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'Test Workout')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team5', description='A test team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(str(leaderboard), 'Test Team5 - 50 points')
