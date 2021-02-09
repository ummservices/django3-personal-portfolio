from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)

    #return the title of the project in the projectlist in the admin
    #Don't forget to tab this function!
    def __str__(self):
        return self.title
