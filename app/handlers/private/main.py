from aiogram import Dispatcher
from aiogram.types import Message
from app.keyboards.private.inline import Sharekb

from app.services.generator import idea_generator


async def get_project_idea(m: Message):
    await m.answer(
        await idea_generator(await m.bot.get_session()), reply_markup=Sharekb().get()
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(get_project_idea, text="💡Get idea")
