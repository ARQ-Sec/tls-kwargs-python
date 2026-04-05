from app.services.audit_service import load_audit_records

def test_audit_records_present() -> None:
    assert load_audit_records()
