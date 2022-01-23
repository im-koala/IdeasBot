from aiogram import Dispatcher
from aiogram.types import Message
from app.keyboards.private.inline import Sharekb

from app.keyboards.private.reply import GenerateIdeaMarkup
from app.services.generator import idea_generator


async def get_start_message(m: Message):
    await m.answer_sticker(
        "CAACAgIAAxkBAAENnrxh7UpI-RgEmNkUhvUqV27L5-cZiQAChwIAAladvQpC7XQrQFfQkCME"
    )
    await m.answer(
        """HI👋🏻
This bot can help u to generate idea for your new project.
Just click on button bellow and relax =)
    """,
    )
    await m.answer(
        await idea_generator(await m.bot.get_session()), reply_markup=Sharekb().get()
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(get_start_message)
