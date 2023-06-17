import math

class tariff:
    def __init__(self, NAME="ТАРИФ", GADGET=0, ONNET=0, ONNET_UNLIMET_AFTER=0, OFFNET=0, ANYNET=0, DATA=0, DATA_UNLBONUS=0, DATA_TPAYBONUS=0, ROAMING=0, INTNET=0, FAMILY=0, SMS=0, SOCIAL=0, EDUCATIONAL=0, TV=0, LIFEBOX=0, FREE_APN=0, CAMPUSDISCOUN=0, PRICE_OF=4, PRICE_ST=0, PRICE_TR=0, PRICE_PER=0, LINK=""):
      self.NAME = NAME #назва тарифу
      self.GADGET = int(GADGET)
      self.ONNET = int(ONNET)
      self.ONNET_UNLIMET_AFTER = int(ONNET_UNLIMET_AFTER)
      self.OFFNET = int(OFFNET)
      self.ANYNET = int(ANYNET)
      self.DATA = int(DATA)
      self.DATA_UNLBONUS = int(DATA_UNLBONUS)
      self.DATA_TPAYBONUS = int(DATA_TPAYBONUS)
      self.ROAMING = int(ROAMING)
      self.INTNET = int(INTNET)
      self.FAMILY = int(FAMILY)
      self.SMS = int(SMS)
      self.SOCIAL = int(SOCIAL)
      self.EDUCATIONAL = int(EDUCATIONAL)
      self.TV = int(TV)
      self.LIFEBOX =int(LIFEBOX)
      self.FREE_APN = int(FREE_APN)
      self.CAMPUSDISCOUN = int(CAMPUSDISCOUN)
      self.PRICE_OF = int(PRICE_OF)
      self.PRICE_ST = int(PRICE_ST)
      self.PRICE_TR = int(PRICE_TR)
      self.PRICE_PER = int(PRICE_PER)
      self.LINK = LINK

tariffs = [
    tariff(NAME="ПОТУЖНИЙ", ANYNET=800, DATA=40, DATA_UNLBONUS=1, DATA_TPAYBONUS=20, FREE_APN=1, CAMPUSDISCOUN=10, PRICE_ST=165, PRICE_TR=100, PRICE_PER=150, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/potuzhnyy/"),
  
    tariff(NAME="ІНЕРНЕТ БЕЗМЕЖ", ONNET=10000, OFFNET=250, DATA=10000, FREE_APN=1, PRICE_ST=175, PRICE_TR=100, PRICE_PER=150, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/int-bezmezh-2021/"),
  
  tariff(NAME="ДЗВІНКИЙ БЕЗМЕЖ", ONNET=10000, OFFNET=250, PRICE_ST=130, PRICE_TR=75, PRICE_PER=120, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/dzvinkiy/"),

  tariff( NAME="ВІЛЬНИЙ ЛАЙФ. РЕГІОН", ONNET_UNLIMET_AFTER=1, ANYNET=1600, DATA=1000, SOCIAL=1, TV=1, LIFEBOX=50, FREE_APN=1, CAMPUSDISCOUN=10, PRICE_ST=275, PRICE_TR=150, PRICE_PER=250, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-reg-2021/"),

   tariff( NAME="ВІЛЬНИЙ ЛАЙФ", ONNET_UNLIMET_AFTER=1, ANYNET=1600, DATA=10000, SOCIAL=1, EDUCATIONAL= 1, TV=1, LIFEBOX=50, FREE_APN=1, CAMPUSDISCOUN=10, PRICE_ST=325, PRICE_TR=180, PRICE_PER=275, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/"),

   tariff( NAME="СМАРТ ЛАЙФ", ONNET_UNLIMET_AFTER=1, ANYNET=800, DATA=25, SOCIAL=1, EDUCATIONAL= 1, FREE_APN=1, CAMPUSDISCOUN=10, PRICE_ST=225, PRICE_TR=120, PRICE_PER=175, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/"),
  
  tariff( NAME="ПРОСТО ЛАЙФ", ONNET_UNLIMET_AFTER=1, ANYNET=300, DATA=8, EDUCATIONAL=1, FREE_APN=1, CAMPUSDISCOUN=10, PRICE_ST=160, PRICE_TR=90, PRICE_PER=140, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/"),

   tariff( NAME="PLATINUM ЛАЙФ", ONNET_UNLIMET_AFTER=1, ANYNET=3000, DATA=10000, ROAMING=500, INTNET=50, SMS=50, SOCIAL=1,EDUCATIONAL=1, TV=2, LIFEBOX=500, FREE_APN=1, PRICE_ST=450, PRICE_TR=250, PRICE_PER=400, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/"),

  tariff(NAME="ШКІЛЬНИЙ ЛАЙФ", ONNET=10000, OFFNET=2.10000, DATA=7,SOCIAL=1,EDUCATIONAL=1, PRICE_ST=150, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/"),

  tariff(NAME="ҐАДЖЕТ БЕЗПЕКА",GADGET=1, ONNET=15, DATA=150,  SMS=15, PRICE_OF=12, PRICE_ST=90,LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/"), #  ONNET, DATA, SMS на день

  tariff(NAME="ҐАДЖЕТ СМАРТ",GADGET=2, ONNET=50, DATA=500,  SMS=50, EDUCATIONAL=1, PRICE_ST=150,LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/"), #  ONNET, DATA, SMS на день

  tariff(NAME="ҐАДЖЕТ ПЛАНШЕТ",GADGET=3, DATA=50, SOCIAL=1,EDUCATIONAL=1, PRICE_ST=275,LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/"), 
  
  tariff(NAME="ҐАДЖЕТ РОУТЕР",GADGET=4, DATA=10000, SOCIAL=1,EDUCATIONAL=1, FREE_APN=1,PRICE_ST=375,LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/"), 

  tariff( NAME="СМАРТ СІМ'Я S", ONNET=10000, OFFNET=500, DATA=20, SMS=500, EDUCATIONAL=1,  FAMILY=1, PRICE_ST=375, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/"),

  tariff( NAME="СМАРТ СІМ'Я M", ONNET=10000, OFFNET=1500, DATA=30, SMS=1000, SOCIAL=1, EDUCATIONAL=1,  FAMILY=1, PRICE_ST=500, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/"),

  tariff( NAME="СМАРТ СІМ'Я L", ONNET=100000, OFFNET=750, DATA=50, SMS=1000, SOCIAL=1, EDUCATIONAL=1,  FAMILY=1, PRICE_ST=425, LINK="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/"),
]





U_tariff = tariff(NAME="U_TARIFF", GADGET=0,
                  SOCIAL=1, ONNET=0, DATA = 30, ROAMING=500,
                  PRICE_ST = 250)


def calculate_euclidean_distance(tariff1, tariff2):
    if tariff1.GADGET > 0 or tariff2.GADGET > 0:
        return float('inf')
    
    distance = 0
    for factor in dir(tariff1):
        if not factor.startswith('__') and not callable(getattr(tariff1, factor)) and factor not in ['LINK', 'NAME', 'GADGET']:
            value1 = getattr(tariff1, factor)
            value2 = getattr(tariff2, factor)
            if isinstance(value1, str) and value1:
                value1 = int(value1)
            if isinstance(value2, str) and value2:
                value2 = int(value2)
            distance += (value1 - value2) ** 2
    return math.sqrt(distance)

for tariff in tariffs: distance = calculate_euclidean_distance(U_tariff, tariff) print(f"Відстань до тарифу '{tariff.NAME}': 
{distance}")