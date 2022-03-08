from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.GroupRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.communities.count()

    pass


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):

    """Community Admin !"""

    # 진짜 어드민 패널에 뿌려주는것 ! fieldsets
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "people",
                )
            },
        ),
        (
            "추가정보등록",
            {
                "classes": ("open",),
                "fields": ("group_rules",),
            },
        ),
        ("Last Details", {"fields": ("owner",)}),
    )

    filter_horizontal = ("group_rules",)  # many to relationships에서 사용한다

    list_filter = (
        "name",
        "people",
        "owner",
    )

    list_display = (
        "name",
        "people",
        "owner",
    )
