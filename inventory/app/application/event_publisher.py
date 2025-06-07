import logging

logger = logging.getLogger("inventory-events")

def publish_event(type: str, data: dict):
    logger.info(f"Publishing event {type} with data {data}")