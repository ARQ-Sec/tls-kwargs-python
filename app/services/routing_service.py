from app.models.routing import RoutingModel

def load_routing_records() -> list[RoutingModel]:
    return [RoutingModel(identifier='routing-seed', owner='routing-owner', state='ACTIVE')]
