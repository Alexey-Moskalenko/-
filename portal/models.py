from django.db import models

# Create your models here.


class Competitions(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    matches = models.ManyToManyField('Match', related_name='competitions')

    def __str__(self):
        return '{}'.format(self.title)


class Match(models.Model):
    team1 = models.CharField(max_length=20, db_index=True)
    team2 = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, default='new')
    t1_c = models.IntegerField(max_length=2, db_index=True, default='0')
    t2_c = models.IntegerField(max_length=2, db_index=True, default='0')
    c1 = models.CharField(max_length=5, db_index=True)
    c2 = models.CharField(max_length=5, db_index=True)
    c3 = models.CharField(max_length=5, db_index=True)
    c4 = models.CharField(max_length=5, blank=True, db_index=True)
    c5 = models.CharField(max_length=5, blank=True, db_index=True)
    date = models.CharField(max_length=10, db_index=True, default='0.0.0')

    def __str__(self):
        return '{}'.format(self.team1, self.team2, self.c1, self.c2, self.c3, self.c4, self.c5, self.date)