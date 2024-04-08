from dataclasses import dataclass
from enum import Enum


class ActivityTypeEnum(Enum):
    """Activity Type Enum"""

    none = 0
    unknown = 1
    playing = 2
    streaming = 3
    listening = 4
    watching = 5
    custom = 6
    competing = 7


@dataclass
class ActivityData:
    id: int
    name: str
    type: ActivityTypeEnum


@dataclass
class MemberData:
    id: int
    name: str


@dataclass
class MemberActivityData:
    member_id: int
    activity_id: int
    minute: int
