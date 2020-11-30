from django.core.management.base import BaseCommand

from test_app.models import Post


class Command(BaseCommand):
    help = "Reset post upvotes"

    def handle(self, *args, **kwargs):
        Post.objects.all().update(upvotes=0)
