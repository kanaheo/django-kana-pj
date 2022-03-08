from django.db import models
from core import models as core_models

# 아이템을 가질 때 ! ( room이 특별하게 뭔가 옵션을 가질 때? 그런데 처음에 migrate에는 영향안가게 필요할 때 사용하게 )
class AbstractItem(core_models.AbstractTimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class GroupRule(AbstractItem):

    """GroupRule Model Definition"""

    class Meta:
        verbose_name = "Group Rule"


class Community(core_models.AbstractTimeStampedModel):

    """Community Model Definition"""

    name = models.CharField("이름(name)", max_length=140)
    people = models.IntegerField("인원(people)")
    owner = models.ForeignKey(
        "users.User",
        related_name="communities",
        on_delete=models.CASCADE,
        verbose_name="그룹장",
    )

    group_rules = models.ManyToManyField(
        "GroupRule", related_name="communities", blank=True
    )

    list_display = (
        "name",
        "people",
        "owner",
    )
