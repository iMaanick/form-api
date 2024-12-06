from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models import Base
from app.application import models

if TYPE_CHECKING:
    from .form_field import FormField


class FormTemplate(Base):
    __tablename__ = "form_templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    fields: Mapped[list["FormField"]] = relationship("FormField", back_populates="template")

    def to_dto(self) -> models.FormTemplate:
        fields_data = [field.to_dto() for field in self.fields]
        fields = {field.name: field.field.type for field in fields_data}
        return models.FormTemplate(id=self.id, name=self.name, fields=fields)
