from django.db import models

# Create your models here.
class Player(models.Model):
    jn=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    teamname = models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.jn} - {self.name} - {self.runs}-{self.wickets}-{self.teamname}"