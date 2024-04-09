from django import template
from django.urls import resolve, reverse
from ..models import MenuItem


register = template.Library()

@register.inclusion_tag("some_template.html", takes_context=True)
def draw_menu(context, menu_name: str) -> dict:
    objects = MenuItem.objects.filter(title=menu_name, is_active=True)
    objects_dict = {}
    for obj in objects:
        if obj.parent is None:
            objects_dict[str(obj.id)] = {"item": obj, "subitems": []}
        else:
            objects_dict[str(obj.parent_id)]["subitems"].append(obj)

    result = {"menu_name": menu_name, "data": list(objects_dict.values())}
    return {"result": result}

