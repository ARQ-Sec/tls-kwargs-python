from app.services.metrics_service import load_metrics_records

def test_metrics_records_present() -> None:
    assert load_metrics_records()
