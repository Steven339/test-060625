import logging

import httpx
from tenacity import (
    before_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)

from app.domain.models import Inventory, Product
from app.domain.repositories import AbstractRepository

logger = logging.getLogger(__name__)
tenacy_logger = logging.getLogger("tenacity")

""" Inventory use cases """

PRODUCTS_URL = "http://products:8000/products"


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
    retry=retry_if_exception_type(httpx.RequestError),
    before=before_log(tenacy_logger, logging.INFO),
)
def check_product(product_id: int) -> Product:
    """ Check if product exists """
    from app.config import PRODUCTS_API_KEY
    PRODUCTS_HEADERS = {"x-api-key": PRODUCTS_API_KEY}
    try:
        response = httpx.get(f"{PRODUCTS_URL}/{product_id}", headers=PRODUCTS_HEADERS, timeout=2.0)
        if response.status_code != 200:
            raise ValueError("Product not found")
        response_json = response.json()
        response_data= response_json["data"]
        return Product(id=response_data["id"], name=response_data["attributes"]["name"], price=response_data["attributes"]["price"])
    except Exception as e:
        logger.exception(str(e))
        raise ValueError(str(e))

def get_inventory(repository: AbstractRepository, product_id: int) -> tuple[Product, Inventory]:
    """ Get inventory by product id """
    product = check_product(product_id)
    inventory = repository.get(product_id)
    if inventory:
        return product, Inventory(product_id=inventory.product_id, quantity=inventory.quantity)
    return None, None

def update_inventory(repository: AbstractRepository, product_id: int, quantity: int) -> tuple[Product, Inventory]:
    """ Update inventory """
    product = check_product(product_id)
    db_inventory = repository.update(Inventory(product_id=product_id, quantity=quantity))
    if db_inventory:
        return product, Inventory(product_id=db_inventory.product_id, quantity=db_inventory.quantity)
    return None
