from dataclasses import dataclass
@dataclass(slots=True)
class RoutingModel:
    identifier: str
    owner: str
    state: str
