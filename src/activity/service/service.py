import discord
import pandas as pd
from discord import Member, Status
from discord.activity import ActivityTypes

from src.activity.const.const import ActivityData, ActivityTypeEnum
from src.activity.model.model import ActivitySchema, MemberActivitySchema, MemberSchema
from src.activity.repository.repository import (
    ActivityRepository,
    MemberActivityRepository,
    MemberRepository,
)


class ActivityService:
    def __init__(
        self,
        ar: ActivityRepository,
        mr: MemberRepository,
        mar: MemberActivityRepository,
        interval: int,
    ):
        self.ar = ar
        self.mr = mr
        self.mar = mar
        self.interval = interval

    def StoreActivity(self, members: list[Member]) -> str:
        for member in members:
            if member.status == Status.offline or member.bot:
                continue

            if member.activity is None:
                continue

            activityData = self.ActivityToDataFrame(member.activity)
            print(activityData)

            if not self.ar.has_activity(activityData.id):
                print("create activity")
                activity_df = pd.DataFrame(
                    {
                        "id": [activityData.id],
                        "name": [activityData.name],
                        "type": [str(activityData.type.value)],
                    }
                )
                validated_activity_df = ActivitySchema.validate(activity_df)
                self.ar.create_activity(validated_activity_df)

            if not self.mr.has_member(member.id):
                print("create member")
                member_df = pd.DataFrame(
                    {
                        "id": [member.id],
                        "name": [member.name],
                    }
                )
                validated_df = MemberSchema.validate(member_df)
                self.mr.create_member(validated_df)

            if not self.mar.has_member_activity(member.id, activityData.id):
                print("create member activity")
                member_activity_df = pd.DataFrame(
                    {
                        "member_id": [member.id],
                        "activity_id": [activityData.id],
                        "minute": [self.interval],
                    }
                )
                validated_member_activity_df = MemberActivitySchema.validate(
                    member_activity_df
                )
                self.mar.create_member_activity(validated_member_activity_df)
            else:
                print("update member activity")
                self.mar.update_hours(member.id, activityData.id, self.interval)

        return (
            "```\n"
            + "activity\n"
            + str(self.ar.adf.df)
            + "\n\nmember\n"
            + str(self.mr.mdf.df)
            + "\n\nmember_activity\n"
            + str(self.mar.madf.df)
            + "\n```"
        )

    def ActivityToDataFrame(self, activity: ActivityTypes) -> ActivityData:
        if activity.type == discord.ActivityType.playing:
            try:
                return ActivityData(
                    id=activity.application_id,
                    name=activity.name,
                    type=ActivityTypeEnum.playing,
                )
            except Exception as e:
                print(e)
        elif activity.type == discord.ActivityType.listening:
            print("listening")
            try:
                if isinstance(activity, discord.Spotify):
                    return ActivityData(
                        id=ActivityTypeEnum.listening.value,
                        name="spotify",
                        type=ActivityTypeEnum.listening,
                    )
                else:
                    print(activity)
            except Exception as e:
                print(e)
        elif activity.type == discord.ActivityType.custom:
            try:
                return ActivityData(
                    id=ActivityTypeEnum.custom.value,
                    name="custom",
                    type=ActivityTypeEnum.custom,
                )
            except Exception as e:
                print(e)
        elif activity.type == discord.ActivityType.streaming:
            ...
        elif activity.type == discord.ActivityType.watching:
            ...
        elif activity.type == discord.ActivityType.unknown:
            ...
        print("unknown activity")
        print(activity)
        print(type(activity))
        print(activity.type)
        return ActivityData(
            id=ActivityTypeEnum.unknown.value,
            name="unknown",
            type=ActivityTypeEnum.unknown,
        )
