from aiogram.utils.callback_data import CallbackData

from app.utils.markup_constructor import InlineMarkupConstructor


class Sharekb(InlineMarkupConstructor):
    def get(self):
        text = "Hi, want to create some project, but don't have some ideas?\nI can help!\n@pidea_bot"
        schema = [1, 1]
        actions = [
            {"text": "💡Get new idea", "callback_data": "get_new_idea"},
            {"text": "🗣Share this bot", "url": f"http://t.me/share/url?url={text}"},
        ]
        return self.markup(actions, schema)
