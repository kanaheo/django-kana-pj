from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # 장고가 제공하는 userAdmin
from . import models


@admin.register(models.User)  # models에서의 User정보를 가져오기
class UserCustomAdmin(UserAdmin):  # 위에 장고가 제공하는것을 상속받아서 쓰기

    """UserCustomAdmin 내용"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom User detail",
            {
                "fields": (
                    "superhost",
                    "biometric",
                    "gender",
                )
            },
        ),
    )

    list_display = ("username", "superhost", "email", "biometric", "gender")
    list_filter = ("superhost",)
