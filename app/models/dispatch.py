from dataclasses import dataclass
@dataclass(slots=True)
class DispatchModel:
    identifier: str
    owner: str
    state: str
