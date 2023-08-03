import uuid
from django.db import models

#Абстрактная модель, созданная для индетенфецирования с помощью uuid
class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True