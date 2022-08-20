from django.db import models

# Create your models here.


class Candidate(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    name = models.CharField(max_length=20, null=False)
    hostel = models.CharField(max_length=20, null=False)
    photo_link = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.email


class Post(models.Model):
    hostel = models.CharField(max_length=20, null=False)
    post_name = models.CharField(max_length=20, null=False)
    candidates = models.ManyToManyField(Candidate)

    def __str__(self):
        return f"{self.hostel}-{self.post_name}"


class VoterList(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    hostel = models.CharField(max_length=20, null=False)
    voted = models.BooleanField(null=False)

    def __str__(self):
        return self.email


class Vote(models.Model):
    user = models.ForeignKey(VoterList, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_casted = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
