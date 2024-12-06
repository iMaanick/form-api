from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.sqlalchemy_db.models import Base
from .field_value_type import FieldValueType

if TYPE_CHECKING:
    from .form_template import FormTemplate


class FormField(Base):
    __tablename__ = "form_fields"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[FieldValueType] = mapped_column(Enum(FieldValueType), nullable=False)
    value: Mapped[str] = mapped_column(String, nullable=False)
    template_id: Mapped[int] = mapped_column(ForeignKey("form_templates.id"))
    template: Mapped["FormTemplate"] = relationship("FormTemplate", back_populates="fields")