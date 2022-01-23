from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from app.keyboards.private.inline import Sharekb

from app.services.generator import idea_generator


async def get_project_idea(c: CallbackQuery):
    await c.answer()
    await c.message.answer(
        await idea_generator(await c.bot.get_session()), reply_markup=Sharekb().get()
    )


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(get_project_idea, text="get_new_idea")
