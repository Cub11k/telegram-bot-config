from dataclasses import dataclass
from typing import Optional


@dataclass
class Webhook:
    base_url: str
    drop_pending: bool
    secret_token: str


@dataclass
class Redis:
    host: str
    password: str
    port: int


@dataclass
class Logger:
    logstream: bool
    loglevel: Optional[str] = None
    logfile: Optional[str] = None


@dataclass
class Loggers:
    loglevel: str
    bot_logger: Logger


@dataclass
class MultiLangText:
    en: str
    ru: str


@dataclass
class Messages:
    unknown: MultiLangText
    message_timeout: MultiLangText
    callback_timeout: MultiLangText
    choose_language: MultiLangText
    register_or_login: MultiLangText
    canceled: MultiLangText
    new_login: MultiLangText
    invalid_login: MultiLangText
    login_taken: MultiLangText
    new_password: MultiLangText
    invalid_password: MultiLangText
    password_too_weak: MultiLangText
    repeat_password: MultiLangText
    passwords_dont_match: MultiLangText
    registration_failed: MultiLangText
    get_login: MultiLangText
    get_password: MultiLangText
    login_failed: MultiLangText
    logged_in: MultiLangText


@dataclass
class Buttons:
    register: MultiLangText
    login: MultiLangText
    cancel: MultiLangText
    reset_login: MultiLangText
    reset_password: MultiLangText
    reset_login_password: MultiLangText
    logout: MultiLangText


@dataclass
class Config:
    token: str
    webhook: Webhook
    redis: Redis
    loggers: Loggers
    messages: Messages
    buttons: Buttons
    telegram_api_url: Optional[str] = None
