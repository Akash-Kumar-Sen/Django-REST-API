from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

# Extending the default user model
User = get_user_model()


# Only model created
class BoxItem(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    last_updated=models.DateTimeField(auto_now_add=True)
    creation_date=models.DateTimeField(auto_now_add=True)
    length=models.FloatField()
    width=models.FloatField()
    height=models.FloatField()

    def get_volume(self):
        return self.length*self.width*self.height

    def get_area(self):
        return self.length*self.width

    def __str__(self):
        return str(self.id)+" Created By "+str(self.creator)


class RestrictionModel(models.Model):
    A1=models.IntegerField(default=100)
    V1=models.IntegerField(default=1000)
    L1=models.IntegerField(default=100)
    L2=models.IntegerField(default=50)

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError(
                "Can only create 1 instance of %s." % model.__name__)
    def __str__(self):
        return "Only restriction object id : " + str(self.id)