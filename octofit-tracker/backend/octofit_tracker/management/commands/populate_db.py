from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User(email='captain@marvel.com', name='Captain Marvel', team=marvel.name),
            User(email='batman@dc.com', name='Batman', team=dc.name),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name),
        ]
        User.objects.bulk_create(users)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Running', description='Run 5km', difficulty='medium'),
            Workout(name='Deadlift', description='Deadlift 100kg', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create activities
        user_objs = list(User.objects.all())
        activities = [
            Activity(user=user_objs[0], type='Pushups', duration=10, date=date.today()),
            Activity(user=user_objs[1], type='Running', duration=30, date=date.today()),
            Activity(user=user_objs[2], type='Deadlift', duration=45, date=date.today()),
            Activity(user=user_objs[3], type='Pushups', duration=15, date=date.today()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
