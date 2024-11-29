from django.db import models

# Create model for UniversityCampus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default='', blank=True, null=False)
    state = models.CharField(max_length=2, default='', blank=True, null=False)
    campus_id = models.IntegerField(default=0, blank=True, null=False)

    #Create Model Manager
    object = models.Manager()

    #Displays object output value in form of string
    def __str__(self):
        #Returns input value of the Campus name
        return self.campus_name

    #Removes added 's' that Django adds to model name in browser display
    class Meta:
        verbose_name_plural = 'University Campus'