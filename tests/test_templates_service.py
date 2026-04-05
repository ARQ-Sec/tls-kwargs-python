from app.services.templates_service import load_templates_records

def test_templates_records_present() -> None:
    assert load_templates_records()
