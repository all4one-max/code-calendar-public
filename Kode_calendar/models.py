from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class codeforces(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class atcoder(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class topcoder(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class leetcode(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class hackerrank(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class hackerearth(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)


class codechef(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)

class all_contest(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=200, null=True)
    end_time = models.CharField(max_length=200, null=True)