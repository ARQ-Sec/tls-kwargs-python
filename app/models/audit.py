from dataclasses import dataclass
@dataclass(slots=True)
class AuditModel:
    identifier: str
    owner: str
    state: str
