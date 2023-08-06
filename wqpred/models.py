from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class TrainData(models.Model):
    aluminum = models.FloatField()
    ammonia = models.FloatField() 
    arsenic = models.FloatField()
    barium = models.FloatField()
    cadmium = models.FloatField()
    chloramine = models.FloatField( )
    chromium = models.FloatField()
    copper = models.FloatField()
    flouride = models.FloatField()
    bacteria = models.FloatField() 
    viruses = models.FloatField()
    lead = models.FloatField()
    nitrates = models.FloatField()
    nitrites = models.FloatField() 
    mercury = models.FloatField()
    perchlorate = models.FloatField()
    radium = models.FloatField()
    selenium = models.FloatField() 
    silver = models.FloatField()
    uranium = models.FloatField()
    is_safe = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.aluminum} - {self.ammonia} - {self.arsenic} - {self.barium} - {self.cadmium} - {self.chloramine } - {self.chromium} - {self.chromium} - {self.copper} - {self.flouride} - {self.bacteria} - {self.viruses} - {self.lead} - {self.nitrates} - {self.nitrites} - {self.mercury} - {self.perchlorate} - {self.radium} - {self.selenium} - {self.silver} - {self.uranium} - {self.is_safe}"

class UserInput(models.Model):
    id = models.CharField(max_length=22,primary_key=True, editable=True)
    aluminum = models.FloatField()
    ammonia = models.FloatField() 
    arsenic = models.FloatField()
    barium = models.FloatField()
    cadmium = models.FloatField()
    chloramine = models.FloatField( )
    chromium = models.FloatField()
    copper = models.FloatField()
    flouride = models.FloatField()
    bacteria = models.FloatField() 
    viruses = models.FloatField()
    lead = models.FloatField()
    nitrates = models.FloatField()
    nitrites = models.FloatField() 
    mercury = models.FloatField()
    perchlorate = models.FloatField()
    radium = models.FloatField()
    selenium = models.FloatField() 
    silver = models.FloatField()
    uranium = models.FloatField()
    pred = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.aluminum} - {self.ammonia} - {self.arsenic} - {self.barium} - {self.cadmium} - {self.chloramine } - {self.chromium} - {self.chromium} - {self.copper} - {self.flouride} - {self.bacteria} - {self.viruses} - {self.lead} - {self.nitrates} - {self.nitrites} - {self.mercury} - {self.perchlorate} - {self.radium} - {self.selenium} - {self.silver} - {self.uranium} - {self.pred}"