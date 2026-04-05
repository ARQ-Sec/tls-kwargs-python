from app.models.dispatch import DispatchModel

def load_dispatch_records() -> list[DispatchModel]:
    return [DispatchModel(identifier='dispatch-seed', owner='dispatch-owner', state='ACTIVE')]
