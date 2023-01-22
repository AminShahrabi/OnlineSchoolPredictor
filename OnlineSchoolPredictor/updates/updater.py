from bale import Update, User,Updater
from datetime import timedelta, datetime
from canstants import SPAM
from colorama import Fore

class RateLimitUser:
    def __init__(self, user: User) -> None:
        self.user = user
        self.useage = 0
        self.last_use = datetime.now()
    async def new_use(self, time: datetime):
        if self.is_rate_limited():
            return
        if time < (self.last_use + timedelta(seconds=1)):
            self.useage += 1
            if (self.useage - 1) == 2:
                await self.user.send(SPAM)
                print(Fore.BLUE + F"BANNED USER {self.user.username}")
        else:
            self.useage -= 1 if self.useage == 0 else self.useage - 1

        self.last_use = time

    def is_rate_limited(self) -> bool:
        if self.useage > 2:
            if datetime.now() < (self.last_use + timedelta(minutes=5)):
                return True
            else:
                self.useage = 0
                return False

class CustomUpdater(Updater):
    def __init__(self, bot):
        super().__init__(bot)
        self.user_rate_limits = {}
        
    async def call_to_dispatch(self, update: "Update"):
        if update.type.is_message_update() or update.type.is_callback_update():
            user = update.callback_query.user if update.callback_query else update.message.author
            rate_limit: RateLimitUser = self.user_rate_limits.get(user.user_id)
            if not rate_limit:
                self.user_rate_limits[user.user_id] = RateLimitUser(user)
                return await super().call_to_dispatch(update)
            elif rate_limit:
                await rate_limit.new_use(datetime.now())
                if not rate_limit.is_rate_limited():
                    return await super().call_to_dispatch(update)
        else:
            return await super().call_to_dispatch(update)
