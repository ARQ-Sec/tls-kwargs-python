from app.models.delivery import DeliveryModel

def load_delivery_records() -> list[DeliveryModel]:
    return [DeliveryModel(identifier='delivery-seed', owner='delivery-owner', state='ACTIVE')]
