from app.services.dispatch_service import load_dispatch_records

def test_dispatch_records_present() -> None:
    assert load_dispatch_records()
