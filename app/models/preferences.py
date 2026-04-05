from dataclasses import dataclass
@dataclass(slots=True)
class PreferencesModel:
    identifier: str
    owner: str
    state: str
