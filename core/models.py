from django.db import models


class AbstractTimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상적인 ! 데이터베이스에는 테이블(core)는 등록이 안된다. 상속시켜서 사용은 가능함
