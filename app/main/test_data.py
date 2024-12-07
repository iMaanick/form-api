import asyncio
import os

from aiotinydb import AIOTinyDB
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from app.adapters.sqlalchemy_db.models import FormTemplate, FormField
from app.application.models.field_value_type import FieldValueType


def create_async_session(db_uri: str) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(db_uri, echo=False)
    return async_sessionmaker(bind=engine, class_=AsyncSession)


async def populate_test_data_sql(session: AsyncSession) -> None:
    form1 = FormTemplate(
        name="Registration Form",
        fields=[
            FormField(name="Email Address", type=FieldValueType.email, value="user1@example.com"),
            FormField(name="Phone Number", type=FieldValueType.phone, value="+71234567890"),
            FormField(name="Birth Date", type=FieldValueType.date, value="2000-01-01"),
        ],
    )

    form2 = FormTemplate(
        name="Feedback Form",
        fields=[
            FormField(name="Name", type=FieldValueType.text, value="John Doe"),
            FormField(name="Email Address", type=FieldValueType.email, value="feedback@example.com"),
            FormField(name="Message", type=FieldValueType.text, value="Great service!"),
        ],
    )

    session.add_all([form1, form2])
    await session.commit()


async def populate_test_data_nosql(form_templates: list[dict[str, str]]) -> None:
    db_path = os.getenv('DB_PATH')
    if not db_path:
        raise ValueError("DB_PATH env variable is not set")
    async with AIOTinyDB(db_path) as db:
        db.insert_multiple(form_templates)


async def main() -> None:
    db_uri = os.getenv("DATABASE_URI")
    if not db_uri:
        raise ValueError("DATABASE_URI environment variable is not set")
    async_session_factory = create_async_session(db_uri)
    async with async_session_factory() as session:
        async with session.begin():
            await populate_test_data_sql(session)

        form_template1 = {
            "name": "Registration Form",
            "Email Address": "user1@example.com",
            "Phone Number": "+71234567890",
            "Birth Date": "2000-01-01"
        }

        form_template2 = {
            "name": "Feedback Form",
            "Name": "John Doe",
            "Email Address": "feedback@example.com",
            "Message": "Great service!"
        }
    await populate_test_data_nosql([form_template1, form_template2])


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
