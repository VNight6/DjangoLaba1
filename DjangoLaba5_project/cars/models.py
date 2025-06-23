
from django.db import models
from django.utils import timezone

class Dealership(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва Дилерства")
    city = models.CharField(max_length=100, default="Київ") # Дефолтне значення
    address = models.CharField(max_length=255, help_text="Повна адреса дилерства") # Field option: help_text
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True) # Field option: unique

    def __str__(self):
        return self.name

class TeslaCar(models.Model):
    MODEL_CHOICES = [ # Field option: choices
        ('M3', 'Model 3'),
        ('MY', 'Model Y'),
        ('MS', 'Model S'),
        ('MX', 'Model X'),
        ('CYT', 'Cybertruck'),
    ]

    COLOR_CHOICES = [ # Field option: choices
        ('BLK', 'Чорний'),
        ('WHT', 'Білий'),
        ('RED', 'Червоний'),
        ('BLU', 'Синій'),
        ('GRY', 'Сірий'),
    ]

    DRIVETRAIN_CHOICES = [ # Field option: choices
        ('RWD', 'Задній привід (RWD)'),
        ('AWD', 'Повний привід (AWD)'),
    ]

    dealership = models.ForeignKey(
        Dealership,
        on_delete=models.CASCADE,
        related_name='cars', # Field option: related_name
        verbose_name="Дилерство" # Field option: verbose_name
    )
    model = models.CharField(
        max_length=3,
        choices=MODEL_CHOICES,
        verbose_name="Модель Tesla" # Field option: verbose_name
    )
    year = models.IntegerField(
        default=timezone.now().year, # Дефолтне значення: поточний рік
        help_text="Рік випуску автомобіля" # Field option: help_text
    )
    color = models.CharField(
        max_length=3,
        choices=COLOR_CHOICES,
        default='WHT', # Дефолтне значення
        verbose_name="Колір" # Field option: verbose_name
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Ціна автомобіля в USD" # Field option: help_text
    )
    mileage = models.IntegerField(
        default=0, # Дефолтне значення
        verbose_name="Пробіг (км)",
        help_text="Пробіг автомобіля в кілометрах" # Field option: help_text
    )
    drivetrain = models.CharField(
        max_length=3,
        choices=DRIVETRAIN_CHOICES,
        default='AWD', # Дефолтне значення
        verbose_name="Тип приводу" # Field option: verbose_name
    )
    battery_range_km = models.IntegerField(
        null=True, blank=True,
        verbose_name="Запас ходу (км)",
        help_text="Заявлений запас ходу на повному заряді" # Field option: help_text
    )
    vin = models.CharField(
        max_length=17,
        unique=True, # Field option: unique
        help_text="Унікальний ідентифікаційний номер транспортного засобу (VIN)", # Field option: help_text
        verbose_name="VIN номер" # Field option: verbose_name
    )
    is_new = models.BooleanField(
        default=True, # Дефолтне значення
        verbose_name="Новий автомобіль" # Field option: verbose_name
    )
    date_added = models.DateTimeField(
        auto_now_add=True, # Автоматично встановлюється при створенні
        verbose_name="Дата додавання" # Field option: verbose_name
    )

    class Meta:
        ordering = ['-date_added'] # Field option: ordering

    def __str__(self):
        return f"{self.get_model_display()} ({self.year}) - {self.dealership.name}"
