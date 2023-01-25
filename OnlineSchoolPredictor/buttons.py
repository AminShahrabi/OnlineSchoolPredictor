from bale import Keyboard, Components, InlineKeyboard
MENU_BUTTONS = Components(keyboards = [Keyboard("وضیعت تعطیلی تهران 📋")])
ACCOUNT_MENU = Components(inline_keyboards = [InlineKeyboard("ثبت نام", callback_data = "register")])
Vote_buttons = lambda tatil_vote, baz_vote: return Components(inline_keyboards = [InlineKeyboard(f"فردا تعطيل است {tatil_vote}", callback_data="yes"), InlineKeyboard(f"فردا تعطيل نيست {baz_vote}", callback_data="no")])
