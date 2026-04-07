from app.services.delivery_service import load_delivery_records

def test_delivery_records_present() -> None:
    assert load_delivery_records()
