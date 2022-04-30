from controlcenter import Dashboard, widgets
from .models import Kitoblar


class ModelItemList(widgets.ItemList):
    model = Kitoblar
    list_display = ('pk', 'name','description')


class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )
