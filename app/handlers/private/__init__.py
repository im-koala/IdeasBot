from aiogram import Dispatcher

from app.handlers.private import start, help_, main


def setup(dp: Dispatcher):
    for module in (main, start, help_):
        module.setup(dp)
