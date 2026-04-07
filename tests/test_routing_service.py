from app.services.routing_service import load_routing_records

def test_routing_records_present() -> None:
    assert load_routing_records()
