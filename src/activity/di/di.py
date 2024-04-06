from dependency_injector import containers
from dependency_injector.providers import Configuration, Factory, Singleton
from discord import Intents

from src.activity.dataframe.dataframe import (
    ActivityDataFrame,
    MemberActivityDataFrame,
    MemberDataFrame,
)
from src.activity.repository.repository import (
    ActivityRepository,
    MemberActivityRepository,
    MemberRepository,
)
from src.activity.router.router import DiscordClient
from src.activity.service.service import ActivityService


class Container(containers.DeclarativeContainer):
    config = Configuration()

    activity_df = Singleton(ActivityDataFrame)
    member_df = Singleton(MemberDataFrame)
    member_activity_df = Singleton(MemberActivityDataFrame)

    activity_repository = Factory(
        ActivityRepository,
        adf=activity_df(),
    )

    member_repository = Factory(
        MemberRepository,
        mdf=member_df(),
    )

    member_activity_repository = Factory(
        MemberActivityRepository,
        madf=member_activity_df(),
    )

    activity_service = Factory(
        ActivityService,
        ar=activity_repository,
        mr=member_repository,
        mar=member_activity_repository,
        interval=config.interval,
    )

    discord_client = Factory(
        DiscordClient,
        token=config.token,
        intents=Intents.default(),
        ase=activity_service,
    )
