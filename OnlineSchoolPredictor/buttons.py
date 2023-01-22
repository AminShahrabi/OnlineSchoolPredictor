from bale import Keyboard, Components, InlineKeyboard
MENU_BUTTONS = Components(keyboards = [Keyboard("وضیعت تعطیلی تهران 📋")])
ACCOUNT_MENU = Components(inline_keyboards = [InlineKeyboard("ثبت نام", callback_data = "register")])
def Vote_buttons(yes, no):
    return Components(
        inline_keyboards = [InlineKeyboard(f"فردا تعطيل است {yes}", callback_data="yes"), InlineKeyboard(f"فردا تعطيل نيست {no}", callback_data="no")]
    )