from django.db import models
from core import models as core_models

# Create your models here.


class Community(core_models.AbstractTimeStampedModel):

    """Community Model Definition"""

    name = models.CharField((), max_length=140)
    people = models.IntegerField()
