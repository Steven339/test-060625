import logging

import httpx
from tenacity import (
    before_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)

from app.config import PRODUCTS_API_KEY
from app.domain.models import Inventory
from app.domain.repositories import AbstractRepository

logger = logging.getLogger(__name__)
tenacy_logger = logging.getLogger("tenacity")

""" Inventory use cases """

PRODUCTS_URL = "http://products:8000/products"
PRODUCTS_HEADERS = {"X-API-KEY": PRODUCTS_API_KEY}


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
    retry=retry_if_exception_type(httpx.RequestError),
    before=before_log(tenacy_logger, logging.INFO),
)
def check_product(product_id: int):
    """ Check if product exists """
    try:
        response = httpx.get(f"{PRODUCTS_URL}/{product_id}", headers=PRODUCTS_HEADERS, timeout=2.0)
        if response.status_code != 200:
            raise ValueError("Product not found")
    except Exception as e:
        logger.error(f"Connection error: {e}")
        raise ValueError(f"Connection error: {e}")

def get_inventory(repository: AbstractRepository, product_id: int) -> Inventory:
    """ Get inventory by product id """
    check_product(product_id)
    inventory = repository.get(product_id)
    if inventory:
        return Inventory(product_id=inventory.product_id, quantity=inventory.quantity)
    return None

def update_inventory(repository: AbstractRepository, product_id: int, quantity: int) -> Inventory:
    """ Update inventory """
    check_product(product_id)
    db_inventory = repository.update(Inventory(product_id=product_id, quantity=quantity))
    if db_inventory:
        return Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
    return None
