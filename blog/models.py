from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)  # Можно заменить на URLField для валидации URL
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_menu_items(self):
        if not self.is_active:
            return []

        menu_items = [self]

        children = self.children.filter(is_active=True)
        for child in children:
            menu_items.extend(child.get_menu_items())

        return menu_items

    @property
    def has_children(self):
        return self.children.filter(is_active=True).exists()
