import pandas as pd
from pandera.typing import DataFrame

from src.activity.dataframe.dataframe import (
    ActivityDataFrame,
    MemberActivityDataFrame,
    MemberDataFrame,
)
from src.activity.model.model import ActivitySchema, MemberActivitySchema, MemberSchema


class ActivityRepository:
    def __init__(self, adf: ActivityDataFrame) -> None:
        self.adf = adf

    def create_activity(self, activity: DataFrame[ActivitySchema]) -> None:
        print(activity)
        print(self.adf.df)
        self.adf.df = pd.concat([self.adf.df, activity], ignore_index=True)

    def has_activity(self, activity_id: int) -> bool:
        return not self.adf.df[self.adf.df["id"] == activity_id].empty


class MemberRepository:
    def __init__(self, mdf: MemberDataFrame) -> None:
        self.mdf = mdf

    def create_member(self, member: DataFrame[MemberSchema]) -> None:
        print(member)
        self.mdf.df = pd.concat([self.mdf.df, member], ignore_index=True)

    def has_member(self, member_id: int) -> bool:
        return not self.mdf.df[self.mdf.df["id"] == member_id].empty


class MemberActivityRepository:
    def __init__(self, madf: MemberActivityDataFrame) -> None:
        self.madf = madf

    def create_member_activity(
        self, member_activity: DataFrame[MemberActivitySchema]
    ) -> None:
        self.madf.df = pd.concat([self.madf.df, member_activity], ignore_index=True)

    def has_member_activity(self, member_id: int, activity_id: int) -> bool:
        return not self.madf.df[
            (self.madf.df["member_id"] == member_id)
            & (self.madf.df["activity_id"] == activity_id)
        ].empty

    def update_hours(self, member_id: int, activity_id: int, minute: int) -> None:
        self.madf.df.loc[
            (self.madf.df["member_id"] == member_id)
            & (self.madf.df["activity_id"] == activity_id),
            "minute",
        ] += minute
