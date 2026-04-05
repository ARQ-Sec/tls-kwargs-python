from dataclasses import dataclass
@dataclass(slots=True)
class DeliveryModel:
    identifier: str
    owner: str
    state: str
