from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'


# in def marbot b ( def Delete_product_image ) daron file signals.py ast k marbot mishavad b inke vaghti kalai ra az daron panel karbari pak mikonim b sorate automat axs oun kala ham az system va az compyoter ma ham pak shavad
# bad az inke ( def Delete_product_image ) ra neveshtim bayad in code ra ham inja benvisim ta system oun def ra beshnasad va ejra konad
    def ready(self) -> None:
        from . import signals
        return super().ready()

