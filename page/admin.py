from django.contrib import admin
from .models import *


class BlockAnnouncement(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title","create_at",)
    list_display = (
        "title",
        "comment",
        "image",
        "create_at",
        "update_at",
    )


admin.site.register(Announcement,BlockAnnouncement)

class BlockProduck(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("title","create_at",)
    list_display = (
        "title",
        "comment",
        "image",
        "create_at",
        "update_at",
    )


admin.site.register(Produck,BlockProduck)
