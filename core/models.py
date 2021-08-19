from django.conf import settings
from django.db import models

class Item(medels.MODEL):
    title = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title

class OrderItem(medels.MODEL):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.item

class Order(medels.MODEL):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.user.username

class item(medels.MODEL):
    pass
    # def __str__(self) -> str:
    #     return self.title
