from dataclasses import dataclass
from environs import Env
from typing import List


@dataclass
class BotConfig:
    token: str
    admin_ids: List[int]


@dataclass
class GoogleConfig:
    client_secret: str
    scopes: List[str]
    api_service: str
    api_version: str
    redirect_url: str


@dataclass
class Config:
    bot: BotConfig
    google: GoogleConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        google=GoogleConfig(
            client_secret=env.str('CLIENT_SECRET_FILE'),
            scopes=env.list('SCOPES'),
            api_service=env.str('API_SERVICE_NAME'),
            api_version=env.str('API_VERSION'),
            redirect_url=env.str('REDIRECT_URL')
        )
    )
