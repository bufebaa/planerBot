from dataclasses import dataclass
from environs import Env
from typing import List


@dataclass
class DatabaseConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class BotConfig:
    token: str
    admin_ids: List[int]


@dataclass
class Config:
    bot: BotConfig
    database: DatabaseConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        database=DatabaseConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
    )