from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.sqlalchemy_db import models
from app.application.models import FormTemplate
from app.application.protocols.database import DatabaseGateway


class SqlaGateway(DatabaseGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_matching_forms(self, required_fields_count: int) -> list[FormTemplate]:
        if required_fields_count == 0:
            return []

        query = (
            select(models.FormTemplate)
            .join(models.FormField, models.FormTemplate.id == models.FormField.template_id)
            .group_by(models.FormTemplate.id)
            .having(func.count(models.FormField.id) >= required_fields_count)
            .options(selectinload(models.FormTemplate.fields))

        )

        result = await self.session.execute(query)
        form_templates = result.scalars().all()
        if not form_templates:
            return []
        return [form.to_dto() for form in form_templates]
