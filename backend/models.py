from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Connection(models.Model):
    sender = models.ForeignKey(User, related_name="sent_connections", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_connections", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default="pending")

class Collaboration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
