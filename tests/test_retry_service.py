from app.services.retry_service import load_retry_records

def test_retry_records_present() -> None:
    assert load_retry_records()
