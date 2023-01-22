import bale
from canstants import CANT_VOTE, START_TEXT, VOTE_SENT
from debug import Debuger
from scraper import Scraper
from messages import Message
from calculation import Calculation
from database import Database
from user import Users
from buttons import MENU_BUTTONS, ACCOUNT_MENU
from updates.updater import CustomUpdater
from adminmessag import ADMINMessageManger

class BaleBot(bale.Bot):
    def __init__(self):
        super().__init__(token= "1891053487:bfqw8JSCRB5iWhpKCoeBtzUT1Juxym4Ly8qn8eSx", updater= CustomUpdater)
        self.bot = self
        self.scraper = Scraper()
        self.calculator = Calculation(self.scraper)
        self.debug = Debuger()
        self.database = Database(self.debug)
        self.messagemanager = Message(self.calculator, self.database)
        self.Amg = ADMINMessageManger(self.database, self)
        self.user_manager = Users(self)
        self.add_event(bale.EventType.READY, self.on_ready)
        self.add_event(bale.EventType.MESSAGE, self.on_message)
        self.add_event(bale.EventType.CALLBACK, self.on_callback)
        self.add_event(bale.EventType.UPDATE, self.on_update)

    async def on_ready(self):
        self.debug.print_ready()

    async def on_message(self,  message: bale.Message):
            
        if message.content:
            self.database.add_log(message)

        if message.content in ["/start"]:
            self.database.open_database()
            if self.user_manager.is_active(message.author.user_id):
                await message.reply(START_TEXT, components=MENU_BUTTONS)
            else:
                await message.reply(START_TEXT, components= ACCOUNT_MENU)


            self.database.close_database()


        else:
            try:
                if message.content.startswith("/"):
                    self.database.open_database()
                    if self.user_manager.is_admin(message.author.user_id):

                        await self.Amg.check_msg(message)
                    self.database.close_database()
                else:
                    await self.messagemanager.check_message(message)



            except Exception:
                    self.debug.error_reply()



    async def on_update(self, update):
        self.debug.print_update(update)

    async def on_callback(self, callback: bale.CallbackQuery):
        try:
            if callback.data == "register":
                message = self.user_manager.register(callback)
                await callback.message.reply(message)

            elif callback.data == "yes":
                s =self.database.addanewvote("yes", callback.user)
                if s:
                    await callback.message.reply(VOTE_SENT, components= MENU_BUTTONS)
                else:
                    await callback.message.reply(CANT_VOTE, components= MENU_BUTTONS)



            elif callback.data == "no":
                s = self.database.addanewvote("no", callback.user)
                if s:
                    await callback.message.reply(VOTE_SENT, components= MENU_BUTTONS)
                else:
                    await callback.message.reply(CANT_VOTE, components= MENU_BUTTONS)

        except Exception:
            self.debug.error_reply()






            
bot = BaleBot()
bot.run()