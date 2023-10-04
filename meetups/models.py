from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} {self.address}'

class Participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title=models.CharField(max_length=200) #CharField is a string field
    organizer_email=models.EmailField() #EmailField is a string field that checks for a valid email format
    date=models.DateField() #DateField is a field that stores a date
    slug=models.SlugField(unique=True) #SlugField is a string field that is used for urls
    description=models.TextField() #TextField is a string field with no limit
    image=models.ImageField(upload_to='images') #ImageField is a field that stores an image
    location=models.ForeignKey(Location, on_delete=models.CASCADE) #ForeignKey is a field that defines a many-to-one relationship
    participants=models.ManyToManyField(Participant, blank=True, null=True) #ManyToManyField is a field that defines a many-to-many relationship


    def __str__(self):
        return f'{self.title} - {self.slug}'