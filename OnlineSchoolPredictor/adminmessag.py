import bale, asyncio
from colorama import Fore

class ADMINMessageManger:
    def __init__(self, db, bot):
        self.db = db
        self.bot = bot

    async def check_msg(self, mg : bale.Message):
        try:
            if mg.content.startswith("/sendall"):
                for i in self.db.get_ids():
                        try:
                            ss = bale.Chat(i, title = i, username = i, first_name=i, last_name=i, _type = "pv")
                            await self.bot.send_message(ss, '''
    
    ''')
                        except Exception:
                            try:
                                print(Fore.WHITE + f"ERROR SENDING MESSAGE TO {ss.username}")

                            except Exception:
                                print(Fore.WHITE +f"CANT FIND CHAT ID USERNAME WITH {i}")

        except Exception as e:
            print(e)

        if mg.content.startswith("/reload"):
            await mg.reply("بات در حال ریلود است 😉")
            await asyncio.sleep(5)
            self.db.close_database()
            await self.bot.close()