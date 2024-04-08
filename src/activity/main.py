import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from di.di import Container
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(dotenv_path="../../.env", verbose=True, override=True)

    token = os.environ["DISCORD_BOT_TOKEN"]
    interval = os.environ["INTERVAL"]

    container = Container()
    container.config.token.from_value(token)
    container.config.interval.from_value(interval)

    container.discord_client().run()
