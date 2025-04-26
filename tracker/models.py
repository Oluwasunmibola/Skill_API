from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Progress(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='progress_entries')
    note = models.TextField()
    progress_level = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill.name} - {self.progress_level}"
