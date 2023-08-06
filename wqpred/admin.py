from django.contrib import admin
# Register your models here.
from .models import UserInput

class UserInputAdmin(admin.ModelAdmin):
    list_display =("id","aluminum","ammonia","arsenic","barium","cadmium","chloramine","chromium","copper","flouride","bacteria","viruses","lead","nitrates","nitrites","mercury","perchlorate","radium","selenium","silver","uranium","pred")


admin.site.register(UserInput, UserInputAdmin)