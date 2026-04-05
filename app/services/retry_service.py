from app.models.retry import RetryModel

def load_retry_records() -> list[RetryModel]:
    return [RetryModel(identifier='retry-seed', owner='retry-owner', state='ACTIVE')]
