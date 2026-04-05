from dataclasses import dataclass
@dataclass(slots=True)
class TemplatesModel:
    identifier: str
    owner: str
    state: str
