from app.models.metrics import MetricsModel

def load_metrics_records() -> list[MetricsModel]:
    return [MetricsModel(identifier='metrics-seed', owner='metrics-owner', state='ACTIVE')]
