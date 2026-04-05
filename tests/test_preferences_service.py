from app.services.preferences_service import load_preferences_records

def test_preferences_records_present() -> None:
    assert load_preferences_records()
