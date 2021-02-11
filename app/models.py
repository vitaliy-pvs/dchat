from django.db import models


class Settings(models.Model):
    site_title = models.TextField(default="#")
    main_page_title = models.TextField(default="#")
    page_list_title = models.TextField(default="#")
    header_color = models.TextField(default="#")
    up_button_color = models.TextField(default="#")
    menu_color = models.TextField(default="#")
    menu_text_color = models.TextField(default="#")
    page_color = models.TextField(default="#")
    page_text_color = models.TextField(default="#")
    page_text_max_width = models.IntegerField(default=1024)


class Message(models.Model):
    timestamp = models.IntegerField()
    username = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return str(self.username) + ": " + str(self.body)
