from django.db import models

class product(models.Model):
    Pname = models.CharField(max_length = 255,blank=False, null = False)
    Description = models.CharField(max_length = 1000, blank=False, null = False)
    price = models.FloatField(blank=False, null = False)
    iteid = models.AutoField(primary_key=True, null = False)
    itemid = str(iteid)


    def __str__(self):
        return self.itemid
    
