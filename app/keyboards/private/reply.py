from aiogram.types import KeyboardButtonPollType

from app.utils.markup_constructor import ReplyMarkupConstructor


class GenerateIdeaMarkup(ReplyMarkupConstructor):
    def get(self):
        schema = [1]
        actions = [{"text": "💡Get idea"}]

        return self.markup(actions, schema, resize_keyboard=True)
