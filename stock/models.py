from django.db import models
from django.conf import settings
from django.utils import timezone
from .validators import validate_symbol

class stock(models.Model):
    # symbol = models.CharField(max_length=4, help_text='Type Stock Symbol HERE', unique=True, validators = [validate_symbol])
    symbol = models.CharField(max_length=4, help_text='Type Stock Symbol HERE', unique=True)
    update_time = models.DateTimeField(default=timezone.now)
    buy_date = models.DateField()
    sell_date = models.DateField()
    profit = models.FloatField()
    plot = models.TextField(default="")

    def updtae(self, buy, sell, profit, plot):
        self.sell_date = buy
        self.buy_date = sell
        self.profit = profit
        self.update_time = timezone.now()
        self.plot = plot
        self.save()

    def get_data(self):
        return self.buy_date, self.sell_date, self.profit, self.plot

    
        