import os

from aiotinydb import AIOTinyDB
from tinydb.table import Document

from app.application.models import FormTemplate, FormField
from app.application.protocols.database import DatabaseGateway


class TinyDBGateway(DatabaseGateway):
    def __init__(self) -> None:
        db_path = os.getenv('DB_PATH')
        if not db_path:
            raise ValueError("DB_PATH env variable is not set")
        self.db_path = db_path

    async def get_matching_forms(self, required_fields_count: int) -> list[FormTemplate]:
        if required_fields_count == 0:
            return []
        async with AIOTinyDB(self.db_path) as db:
            return self.convert_documents_to_form_templates(db.all())

    @staticmethod
    def convert_documents_to_form_templates(documents: list[Document]) -> list[FormTemplate]:
        form_templates = []
        for doc in documents:
            data = {
                key: value
                for key, value in doc.items()
                if key != "name"
            }
            fields_data = []
            for name, field_value in data.items():
                fields_data.append(FormField(name=name, field={"value": field_value}))
            fields = {field.name: field.field.type for field in fields_data}

            form_template = FormTemplate(
                id=doc.doc_id,
                name=doc.get("name"),
                fields=fields
            )
            form_templates.append(form_template)
        return form_templates
