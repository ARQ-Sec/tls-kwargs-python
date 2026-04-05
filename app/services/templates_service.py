from app.models.templates import TemplatesModel

def load_templates_records() -> list[TemplatesModel]:
    return [TemplatesModel(identifier='templates-seed', owner='templates-owner', state='ACTIVE')]
