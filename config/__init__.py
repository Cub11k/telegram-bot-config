from io import StringIO
import os

from dataclass_factory import Factory
from jinja2 import Environment, FileSystemLoader
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from telegram_bot.config.models import Config
from telegram_bot.config.models import Webhook, Redis, Loggers, Messages, Buttons, MultiLangText


def process_config_template(data: dict):
    jinja_env = Environment(loader=FileSystemLoader('templates'))
    jinja_env.filters['env_var'] = lambda value, key: os.environ.get(key, value)
    template = jinja_env.get_template('config_template.yaml')
    stream = StringIO()
    stream.write(template.render(data))
    stream.seek(0)
    return yaml.load(stream, Loader=Loader)


def load_config() -> Config:
    config_path = os.environ.get('CONFIG_PATH', 'config.yaml')
    with open(config_path, 'r') as f:
        data = yaml.load(f, Loader=Loader)
    data = process_config_template(data)
    factory = Factory()
    return factory.load(data, Config)
