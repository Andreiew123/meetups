from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name} ({self.address})'
    
class Participant(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.email}'
    
    
class Meetup(models.Model):
    title = models.CharField(max_length=100)
    organizer_email = models.EmailField()
    dateof = models.DateField(auto_now_add=False, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='noimage.jpg')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} - {self.slug} - {self.dateof}'
    