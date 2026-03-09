from app.api.client_get import redis_client
from app.api.manager import CurrencyManager

def get_manager():
    return CurrencyManager(redis_client)
