from dataclasses import dataclass
@dataclass(slots=True)
class RetryModel:
    identifier: str
    owner: str
    state: str
