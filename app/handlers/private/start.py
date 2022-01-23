from aiogram import Dispatcher
from aiogram.types import Message

from app.keyboards.private.reply import GenerateIdeaMarkup


async def get_start_message(m: Message):
    await m.answer_sticker(
        "CAACAgIAAxkBAAENnrxh7UpI-RgEmNkUhvUqV27L5-cZiQAChwIAAladvQpC7XQrQFfQkCME"
    )
    await m.answer(
        """HI👋🏻
This bot can help u to generate idea for your new project.
Just click on button bellow and relax =)
    """,
        reply_markup=GenerateIdeaMarkup().get(),
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(get_start_message)
