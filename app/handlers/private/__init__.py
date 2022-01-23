from aiogram import Dispatcher

from app.handlers.private import start, main


def setup(dp: Dispatcher):
    for module in (start, main):
        module.setup(dp)
