from app.models.audit import AuditModel

def load_audit_records() -> list[AuditModel]:
    return [AuditModel(identifier='audit-seed', owner='audit-owner', state='ACTIVE')]
