from scraper import Scraper
from random import random
class Calculation:
    def __init__(self, scraper: "Scraper"):
        self.pl_percent = 3
        self.gas_percent = 1.5
        self.cold_percent = 2
        self.er_percent = 1
        self.scraper = scraper


    def calculate_tehran(self):
        pullotion = self.scraper.get_pullution_tehran()
        temp = self.scraper.get_temp_tehran()

        pullotion = int(pullotion)
        temp = int(temp)

        if pullotion <= 100:
            self.pl_percent = 0

        elif pullotion > 100 and pullotion < 120:
            self.pl_percent = 1.75

        elif pullotion >= 120 and pullotion < 150:
            self.pl_percent = 2

        else:
            self.pl_percent = 2.75
   
        if temp >= 5:
            self.cold_percent = 0

        elif temp > 0 and temp < 5:
            self.cold_percent = 1
        
        elif temp <= 0 and temp >= -5:
            self.cold_percent = 2

        elif temp < -5 and temp > -10:
            self.cold_percent = 2.5

        else:
            self.cold_percent = 3

        percent = 0
        if self.pl_percent * 10 * 3 > 75:
            percent += 20
        
        if self.cold_percent * 10 * 4:
            percent += 20

        if self.gas_percent * 10 * 3:
            percent += 20

        if self.er_percent:
            percent += 30
        
        percent += int(random() * 10 )

        ehtemal = "نامعلوم"
        if percent >= 80:
            ehtemal = "بسيار زياد"
        elif percent <= 40:
            ehtemal = "كم"
        else:
            ehtemal = "متوسط"


        return f'''
شاخص : {pullotion}
دمای هوا : {temp} درجه
کمبود گاز : 😥✔

درصد امکان تعطیلی بخاطر شاخص : {self.pl_percent * 10 * 3}
درصد امکان تعطیلی بخاطر گاز : {self.gas_percent * 10 * 3}
درصد امکان تعطیلی بخاطر سرما : {self.cold_percent * 10 * 4}
درصد امکان تعطیلی بخاطر دلاليل ديگر : {self.er_percent * 10 * 7}
درصد تعطیلی کلی : {percent}
احتمال تعطيلي :‌ {ehtemal}
بات وضیعت تعطیلی ، دقیق تر از همجا ! 
با دوستان خود به اشتراک بگذارید 😁

@tehran_schools_off_bot

لطفا براي ادامه كار در ربات نظر خودتون رو اعلام كنيد :


'''



        
