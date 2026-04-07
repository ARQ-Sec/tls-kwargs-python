from dataclasses import dataclass
@dataclass(slots=True)
class MetricsModel:
    identifier: str
    owner: str
    state: str
