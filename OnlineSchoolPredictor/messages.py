from calculation import Calculation
from buttons import Vote_buttons
class Message:
    def __init__(self, calculator : "Calculation", database):
        self.calculator = calculator
        self.database = database


    async def check_message(self, message):
        if message.content == "وضیعت تعطیلی تهران 📋":
            vote = self.database.get_votes()
            await message.reply(self.calculator.calculate_tehran(), components = Vote_buttons(vote[0], vote[1]))

        elif message.content == "نظرات":
            await message.reply(self.database.get_comments())

        else:
            await message.reply("همچين دستوري وجود ندارد 🙄")


    
