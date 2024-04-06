import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

from src.activity.model.model import ActivitySchema, MemberActivitySchema, MemberSchema


class ActivityDataFrame:
    def __init__(self):
        self.df = self.create_activity_dataframe()

    def create_activity_dataframe(self) -> DataFrame[ActivitySchema]:
        schema = pa.DataFrameSchema(
            {
                "id": pa.Column(pa.Int),
                "name": pa.Column(pa.Object),
                "type": pa.Column(pa.Object),
            }
        )
        return schema(
            pd.DataFrame(
                columns=["id", "name", "type"],
            ).astype({"id": "int64", "name": "object", "type": "object"})
        )


class MemberDataFrame:
    def __init__(self):
        self.df = self.create_member_dataframe()

    def create_member_dataframe(self) -> DataFrame[MemberSchema]:
        schema = pa.DataFrameSchema(
            {
                "id": pa.Column(pa.Int),
                "name": pa.Column(pa.Object),
            }
        )
        return schema(
            pd.DataFrame(
                columns=["id", "name"],
            ).astype({"id": "int64", "name": "object"})
        )


class MemberActivityDataFrame:
    def __init__(self):
        self.df = self.create_member_activity_dataframe()

    def create_member_activity_dataframe(self) -> DataFrame[MemberActivitySchema]:
        schema = pa.DataFrameSchema(
            {
                "member_id": pa.Column(pa.Int),
                "activity_id": pa.Column(pa.Int),
                "minute": pa.Column(pa.Int),
            }
        )
        return schema(
            pd.DataFrame(
                columns=["member_id", "activity_id", "minute"],
            ).astype({"member_id": "int64", "activity_id": "int64", "minute": "int64"})
        )
