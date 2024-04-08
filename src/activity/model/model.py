import pandera as pa
from pandera.typing import Series


class MemberSchema(pa.SchemaModel):
    id: Series[int] = pa.Field(
        nullable=False,
        unique=True,
    )
    name: Series[str] = pa.Field(nullable=False)


class ActivitySchema(pa.SchemaModel):
    id: Series[int] = pa.Field(nullable=False, unique=True)
    name: Series[str] = pa.Field(nullable=False)
    type: Series[str] = pa.Field(nullable=False)


class MemberActivitySchema(pa.SchemaModel):
    member_id: Series[int] = pa.Field(nullable=False)
    activity_id: Series[int] = pa.Field(nullable=False)
    minute: Series[int] = pa.Field(nullable=False)  # minute spent on the activity
