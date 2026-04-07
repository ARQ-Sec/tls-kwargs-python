from app.models.preferences import PreferencesModel

def load_preferences_records() -> list[PreferencesModel]:
    return [PreferencesModel(identifier='preferences-seed', owner='preferences-owner', state='ACTIVE')]
