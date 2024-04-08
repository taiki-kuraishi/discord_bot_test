## Activity調査結果

### 目的
discord.Activityクラスのattributeが、人によって違う
そのため、存在しないattributeにアクセスした際にattributeErrorが起きる
調査が必要。

### 詳細
DBでdiscord.activityを管理するにあたり、一意なidがほしい。
discord.Gameには、application_idがあり、ゲームを一意に識別することが可能
しかし、他のアクティビティには、ないため、方法を考える必要がある

### 提案
以下のように、discord.ActivityTypeを使用して区別することができるが、
discord.Spotifyのように、もっと細かく区別する必要がある。
```python
for member in members:
    if member.status == Status.offline or member.bot:   #オフライン、botのactivityは取得しない
        continue

    if member.activity is None: #activityがない人は取得しない
        continue

    if activity.type == discord.ActivityType.playing:
        ...
    elif activity.type == discord.ActivityType.listening:
        if isinstance(activity, discord.Spotify):
            ...
        else:
            ...
    elif activity.type == discord.ActivityType.custom:
        ...
    elif activity.type == discord.ActivityType.streaming:
        ...
    elif activity.type == discord.ActivityType.watching:
        ...
    elif activity.type == discord.ActivityType.unknown:
        ...
    else:
        ...
```

### 結論
技術的に十分可能であるが、
botアカウントはdiscord.activityを自由にいじれるため、discord.ActivityTypeに当てはまらない
つまり、botのactivityを取得するには、他の工夫が必要であり、botのactivityは取得しない方針が賢明である。
