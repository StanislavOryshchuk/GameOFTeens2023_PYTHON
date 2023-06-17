import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from flask_back import keep_alive
from model_user import UserProfile
from model_tariffs import tariffs
import sqlite3 


# Підключення до бази даних SQLite
conn = sqlite3.connect('user_profile.db')
cursor = conn.cursor()

# Створення таблиці
async def create_table(table_name, user_id):
  table_name = "table_" + str(user_id) 
  cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
  (user_id INTEGER PRIMARY KEY,
  U_GADGET INTEGER,
  ONNET_MIN INTEGER,
  ONNET_MAX INTEGER,
  OFFNET_MIN INTEGER,
  OFFNET_MAX INTEGER,
  DATA_MIN INTEGER,
  DATA_MAX INTEGER,
  ROAMING INTEGER,
  INTNET INTEGER,
  FAMILY INTEGER,
  SMS INTEGER,
  SOCIAL INTEGER,
  EDUCATIONAL INTEGER,
  TV INTEGER,
  LIFEBOX INTEGER,
  NUMBER_TYPE TEXT,
  PRICE_MIN INTEGER,
  PRICE_MAX INTEGER
    )
''')
conn.commit()

log = logging.basicConfig(filename="Botlogs.log", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")

bottoken = os.getenv("bot_token")
bot = Bot(token=bottoken)
dp = Dispatcher(bot)

admin_id = 1300417787



class TariffState(StatesGroup):
    SELECT_TARIFF = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Привіт👋")
    await bot.send_message(chat_id=message.from_user.id, text="Я телеграм бот - помічник компанії Lifecell")
   # Inline клавіатура з кнопкою "Підібрати"
    keyboard = InlineKeyboardMarkup()
    button_p = InlineKeyboardButton(text="Підібрати", callback_data="select_category")
    keyboard.row(button_p)
  
    await bot.send_message(chat_id=message.from_user.id, text="Я допоможу вам підібрати вигідний тариф", reply_markup=keyboard)



@dp.callback_query_handler(text="select_category")
async def select_category_callback(query: types.CallbackQuery):
  await query.answer(cache_time=1) 

   
  keyboard = InlineKeyboardMarkup()
  button_private = InlineKeyboardButton(text="Приватним клієнтам", callback_data="private_clients")
  button_business = InlineKeyboardButton(text="Бізнес", callback_data="business")
  keyboard.row(button_private, button_business)

  await query.message.answer("1. Оберіть категорію:", reply_markup=keyboard)


@dp.callback_query_handler(text="private_clients")
async def private_clients_callback(query: types.CallbackQuery):
  await query.answer(cache_time=1) 
  
  keyboard = InlineKeyboardMarkup()
  button_start_poll = InlineKeyboardButton(text="так", callback_data="start_poll")
  button_show_list = InlineKeyboardButton(text="показати всі", callback_data="show_all")
  keyboard.row(button_start_poll, button_show_list)
  await query.message.answer("2. Бажаєте пройти опитування задля отримання рекомендації?", reply_markup=keyboard)


@dp.callback_query_handler(text="start_poll")
async def start_poll_callback(query: types.CallbackQuery):
  await query.answer(cache_time=1) 
  user_id = int(query.from_user.id)
  table_name = "table_" + str(user_id)
  await create_table(table_name,user_id)
  cursor.execute(f"INSERT INTO {table_name} (user_id) VALUES (?)", (user_id,))
  conn.commit()
  
  keyboard = InlineKeyboardMarkup()
  button_gadget0 = InlineKeyboardButton(text="смартфон", callback_data="gadget0")
  button_gadget1 = InlineKeyboardButton(text="датчик", callback_data="gadget1")
  button_gadget2 = InlineKeyboardButton(text="смартгодинник",
                                        callback_data="gadget2")
  button_gadget3 = InlineKeyboardButton(text="планшет", callback_data="gadget3")
  button_gadget4 = InlineKeyboardButton(text="роутер", callback_data="gadget4")
  keyboard.row(button_gadget0)
  keyboard.row(button_gadget1)
  keyboard.row(button_gadget2)
  keyboard.row(button_gadget3)
  keyboard.row(button_gadget4)
  await query.message.answer("3. Оберіть ваш пристрій", reply_markup=keyboard)






@dp.callback_query_handler(lambda query: query.data.startswith('gadget'))
async def handle_gadget_selection(query: types.CallbackQuery):
  await query.answer(cache_time=1)
  user_id = query.from_user.id
  U_GADGET  = int(query.data[len('gadget'):])
  table_name = "table_" + str(user_id)
  cursor.execute(f"INSERT INTO {table_name} (U_GADGET) VALUES (?)", (U_GADGET,))
  conn.commit()
  await query.message.answer(f"Ви обрали гаджет {U_GADGET}")
  if U_GADGET==1:
    R_TARIFF = tariffs[9]
    message_text = (
            f"Вам підійде тариф *{R_TARIFF.NAME}* \n"
            f"Дзвінки на lifecell: {R_TARIFF.ONNET} хв/на день \n"
            f"Інтернет: {R_TARIFF.DATA} МБ/на день \n"
            f"SMS: {R_TARIFF.SMS} /на день \n"
            f"Вартість: {R_TARIFF.PRICE_ST} грн/12 тижнів\n"
        )
    await query.message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
      
    await query.message.answer("Детальніше і nідключити тариф"
      f"{R_TARIFF.LINK}")


  if U_GADGET == 2:
    R_TARIFF = tariffs[10]
    message_text = (
            f"Вам підійде тариф *{R_TARIFF.NAME}* \n"
            f"Дзвінки на lifecell: {R_TARIFF.ONNET} хв/на день \n"
            f"Інтернет: {R_TARIFF.DATA} МБ/на день \n"
            f"SMS: {R_TARIFF.SMS} /на день \n"
            "БЕзліміт на освітні платформи \n"
            f"Вартість: {R_TARIFF.PRICE_ST} грн/4 тижні\n"
        )
    await query.message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
    await query.message.answer("Детальніше і nідключити тариф\n"
      f"{R_TARIFF.LINK}")

  if U_GADGET==3:
    R_TARIFF = tariffs[11]
    message_text = (
            f"Вам підійде тариф *{R_TARIFF.NAME}* \n"
            f"Інтернет: {R_TARIFF.DATA} ГБ \n"
            " Безлім на соціальні мережі та освітні пллатформи \n"
            f"Вартість: {R_TARIFF.PRICE_ST} грн/4 тижні\n"
        )
    await query.message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
    await query.message.answer("Детальніше і nідключити тариф \n"
      f"{R_TARIFF.LINK}")
    
  if U_GADGET==4:
    R_TARIFF = tariffs[12]
    message_text = (
            f"Вам підійде тариф *{R_TARIFF.NAME}* \n"
            f"Інтернет: Безліміт\n"
            " Безліміт на соціальні мережі, мемсенджери й освітні пллатформи \n"
            f"Вартість: {R_TARIFF.PRICE_ST} грн/4 тижні\n"
        )
    await query.message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
    await query.message.answer("Детальніше і nідключити тариф \n"
      f"{R_TARIFF.LINK}")

  if U_GADGET==0:
    keyboard = InlineKeyboardMarkup()
    button_net_option1 = InlineKeyboardMarkup(text = "дуже рідко(до 500)",callback_data="500" )
    button_net_option2 = InlineKeyboardButton(text="Говорю по потребі (600 - 1000)", callback_data="1000")
    button_net_option3 = InlineKeyboardButton(text="Часто заговорююсь (1000 - 2000)", callback_data="2000")
    button_net_option4 = InlineKeyboardButton(text="Завжди на телефоні (понад 2000)", callback_data="100000")
      
    keyboard.add(button_net_option1)
    keyboard.add(button_net_option2)
    keyboard.add(button_net_option3)
    keyboard.add(button_net_option4)
    await query.message.answer("4. Як часто ви спілкуєтесь по телефону?\n"
                               "(в середньому хв/місяць)", reply_markup=keyboard)


    @dp.callback_query_handler(lambda query: query.data in ["500", "1000", "2000", "100000"])
    async def handle_phone_frequency(query: types.CallbackQuery):
      await query.answer(cache_time=1)
      user_id = query.from_user.id
      frequence_mapping = {
    "500": {"ONNET_MIN": 0, "ONNET_MAX": 500},
    "1000": {"ONNET_MIN": 600, "ONNET_MAX": 1000},
    "2000": {"ONNET_MIN": 1000, "ONNET_MAX": 2000},
    "100000": {"ONNET_MIN": 2000, "ONNET_MAX": 100000}
      }
      table_name = "table_" + str(user_id)
      data = query.data
      
      values = frequence_mapping[data]
      ONNET_MIN = values["ONNET_MIN"]
      ONNET_MAX = values["ONNET_MAX"]
      cursor.execute(f"INSERT INTO {table_name} (ONNET_MIN) VALUES (?)", (ONNET_MIN,))
      cursor.execute(f"INSERT INTO {table_name} (ONNET_MAX) VALUES (?)", (ONNET_MAX,))
      conn.commit() 
      
      
      keyboard = InlineKeyboardMarkup()
      button_offnet_option1 = InlineKeyboardMarkup(text = "мої люди на лайфі)",callback_data="100" )
      button_offnet_option2 = InlineKeyboardButton(text="50/50", callback_data="550")
      button_offnet_option3 = InlineKeyboardButton(text="майже всі на інші(", callback_data="1000")
      keyboard.add(button_offnet_option1)
      keyboard.add(button_offnet_option2)
      keyboard.add(button_offnet_option3)
      
      await query.message.answer("5.Як багато дзвінків припадає на інші мережі?", reply_markup=keyboard)
      @dp.callback_query_handler(lambda query: query.data in ["100", "550", "1000"])
      async def handle_offnet_frequency(query: types.CallbackQuery):
        await query.answer(cache_time=1)
        user_id = query.from_user.id
        offnet_frequence_mapping = {
    "100": {"OFFNET_MIN": 0, "OFFNET_MAX": 100},
    "550": {"OFFNET_MIN": 101, "OFFNET_MAX": 1000},
    "1000": {"OFFNET_MIN": 1001, "OFFNET_MAX": 2000}
        }
        table_name = "table_" + str(user_id)
        data = query.data
        
        values = offnet_frequence_mapping[data]
        OFFNET_MIN = values["OFFNET_MIN"]
        OFFNET_MAX = values["OFFNET_MAX"]
        cursor.execute(f"INSERT INTO {table_name} (OFFNET_MIN) VALUES (?)", (OFFNET_MIN,))
        cursor.execute(f"INSERT INTO {table_name} (OFFNET_MAX) VALUES (?)", (OFFNET_MAX,))
        conn.commit()
        
        keyboard = InlineKeyboardMarkup()
        button_roaming_option1 = InlineKeyboardMarkup(text = "дуже часто",callback_data="1" )
        button_roaming_option2 = InlineKeyboardButton(text="час від часу ", callback_data="1")
        button_roaming_option3 = InlineKeyboardButton(text="рідко", callback_data="0")
        button_roaming_option4 = InlineKeyboardButton(text="ніколи", callback_data="0")
        keyboard.add(button_roaming_option1)
        keyboard.add(button_roaming_option2)
        keyboard.add(button_roaming_option3)
        keyboard.add(button_roaming_option4)
        await query.message.answer("6.Наскільки часто ви подорожуєте за кордон?", reply_markup=keyboard)
        
        @dp.callback_query_handler(lambda query: query.data in ["1", "1"," 0", "0"])
        async def handle_roaming(query: types.CallbackQuery):
          await query.answer(cache_time=1)
          user_id = query.from_user.id
          table_name = "table_" + str(user_id)
          ROAMING = query.data
          cursor.execute(f"INSERT INTO {table_name} (ROAMING) VALUES (?)", (ROAMING,))
          conn.commit() 
          
          await query.message.answer("йдемо далі")
          
          keyboard = InlineKeyboardMarkup()
          button_data_option1 = InlineKeyboardMarkup(text = "мало(до 10 ГБ)",callback_data="11" )
          button_data_option2 = InlineKeyboardButton(text="по-середньо (10-25ГБ)", callback_data="25")
          button_data_option3 = InlineKeyboardButton(text="багато(25+)", callback_data="100")
          keyboard.add(button_data_option1)
          keyboard.add(button_data_option2)
          keyboard.add(button_data_option3)
          
          await query.message.answer("7.Скільки мобільного інтернету ви витрачаєте ? (на місяць)", reply_markup=keyboard)
          
          @dp.callback_query_handler(lambda query: query.data in ["11", "25"," 100"])
          async def handle_data(query: types.CallbackQuery):
            await query.answer(cache_time=1)
            user_id = query.from_user.id
            data_mapping = {
    "11": {"DATA_MIN": 0, "DATA_MAX": 10},
    "25": {"DATA_MIN": 10, "DATA_MAX": 25},
    "100": {"DATA_MIN": 25, "DATA_MAX": 100}
            }
            table_name = "table_" + str(user_id)
            data = query.data
            values =data_mapping[data]
            DATA_MIN = values["DATA_MIN"]
            DATA_MAX = values["DATA_MAX"]
            cursor.execute(f"INSERT INTO {table_name} (DATA_MIN) VALUES (?)", (DATA_MIN,))
            cursor.execute(f"INSERT INTO {table_name} (DATA_MAX) VALUES (?)", (DATA_MAX,))
            conn.commit() 
      
            
            keyboard = InlineKeyboardMarkup()
            button_aditionals_option1 = InlineKeyboardButton(text = "SMS 50",callback_data="50")
            button_aditionals_option2 = InlineKeyboardButton(text="SMS 250", callback_data="250")
            button_aditionals_option3 = InlineKeyboardButton(text="∞ соцмережі", callback_data="5")
            button_aditionals_option4 = InlineKeyboardButton(text="∞ освіта", callback_data="6")
            button_aditionals_option5 = InlineKeyboardButton(text="LIFEBOX", callback_data="7")
            button_aditionals_option6 = InlineKeyboardButton(text="TV+", callback_data="8")
            button_aditionals_option7 = InlineKeyboardButton(text=">5 на 1 тарифі", callback_data="9")
            button_aditionals_option8 = InlineKeyboardButton(text="далі", callback_data="10")
            keyboard.add(button_aditionals_option1, button_aditionals_option2 )
            keyboard.add(button_aditionals_option3, button_aditionals_option4)
            keyboard.add(button_aditionals_option5,button_aditionals_option6)
            keyboard.add(button_aditionals_option7, button_aditionals_option8)
            await query.message.answer("8. Що б ви хотіли ще додати у свій тариф", reply_markup=keyboard)

            @dp.callback_query_handler(lambda query: query.data in ["50", "250", "5", "6", "7", "8", "9"])
            async def handle_aditionals(query: types.CallbackQuery):
              user_id = query.from_user.id
              aditionals_mapping = {
        "50": {"SMS": 50},
        "250": {"SMS": 250},
        "5": {"SOCIAL": 1},
        "6": {"EDUCATIONAL": 1},
        "7": {"LIFEBOX": 250},
        "8": {"TV": 0.5},
        "9": {"FAMILY": 1}
              }
              table_name = "table_" + str(user_id)
              data = query.data
              values = aditionals_mapping[data]
              SMS = values.get("SMS", 0)
              SOCIAL = values.get("SOCIAL", 0)
              EDUCATIONAL = values.get("EDUCATIONAL", 0)
              LIFEBOX = values.get("LIFEBOX", 0)
              TV = values.get("TV", 0)
              FAMILY = values.get("FAMILY", 0)
              cursor.execute(f"INSERT INTO {table_name} (SMS, SOCIAL, EDUCATIONAL, LIFEBOX, TV, FAMILY) VALUES (?, ?, ?, ?, ?, ?)",
                   (SMS, SOCIAL, EDUCATIONAL, LIFEBOX, TV, FAMILY))
              conn.commit() 
              @dp.callback_query_handler(lambda query: query.data=="10")
              async def hendler_go_price(query: types.CallbackQuery):
                await query.message.answer("Дякую за відповідь! Ваш вибір збережено. Далі - питання ціни")
                keyboard_new = InlineKeyboardMarkup()
                button_price_option1 = InlineKeyboardButton(text = "до 120",callback_data="121")
                button_price_option2 = InlineKeyboardButton(text="до 250", callback_data="251")
                button_price_option3 = InlineKeyboardButton(text="гроші не проблема", callback_data="501")
                keyboard_new.add(button_price_option1)
                keyboard_new.add(button_price_option2)
                keyboard_new.add(button_price_option3)
                await query.message.answer("9.Яка ціна буде для вас оптимальною?", reply_markup=keyboard_new)
            
                @dp.callback_query_handler(lambda query: query.data in ["121", "251", "501"])
                async def handle_price(query: types.CallbackQuery):
                  await query.answer(cache_time=1)
                  user_id = query.from_user.id
                  table_name = "table_" + str(user_id)
                  data = query.data
                  price_mapping={
                    "121": {"PRICE_MIN":75, "PRICE_MAX": 120},
                    "251": {"PRICE_MIN":120, "PRICE_MAX": 250},
                    "501": {"PRICE_MIN":251, "PRICE_MAX": 500},
                  }
                  values = price_mapping[data]
                  PRICE_MIN = values["PRICE_MIN"]
                  PRICE_MAX = values["PRICE_MAX"]
                  cursor.execute(f"UPDATE {table_name} SET PRICE_MIN = ?, PRICE_MAX = ? WHERE user_id = ?", (PRICE_MIN, PRICE_MAX, user_id))
                  conn.commit() 
                
                  await query.message.answer("Дякую за присвячений час.")
                  await query.message.answer("Зачекайте йде розрахунок")
                  user_id = query.from_user.id
                  async def get_table_data(user_id):
                    table_name = "table_" + str(user_id)
                    cursor.execute(f"SELECT * FROM {table_name}")
                    rows = cursor.fetchall()
                    data_array = []
                    for row in rows:
                      data = {
            "user_id": row[0],
            "U_GADGET": row[1],
            "ONNET_MIN": row[2],
            "ONNET_MAX": row[3],
            "OFFNET_MIN": row[4],
            "OFFNET_MAX": row[5],
            "DATA_MIN": row[6],
            "DATA_MAX": row[7],
            "ROAMING": row[8],
            "INTNET": row[9],
            "FAMILY": row[10],
            "SMS": row[11],
            "SOCIAL": row[12],
            "EDUCATIONAL": row[13],
            "TV": row[14],
            "LIFEBOX": row[15],
            "NUMBER_TYPE": row[16],
            "PRICE_MIN": row[17],
            "PRICE_MAX": row[18]
                      }
                    data_array.append(data)
                    return data_array
                    data_array = await get_table_data(user_id)
                    def prepering_user_profile(data_array): ###далі псевдокод 
                      data_c = {
            "U_GADGET": U_GADGET,
            "ONNET_": 0.5*(data_array["ONNET_MIN"]+data_array["ONNET_MAX"]
            "OFFNET": 0.5*(data_array["ONNET_MIN"]+data_array["ONNET_MAX"]# так само з іншими
            "DATA": DATA_MAX,
            "ROAMING": ROAMING,
            "INTNET": INTNET,
            "FAMILY": FAMILY,
            "SMS": SMS,
            "SOCIAL": SOCIAL,
            "EDUCATIONAL": EDUCATIONAL,
            "TV": TV,
            "LIFEBOX": LIFEBOX,
            "NUMBER_TYPE": NUMBER_TYPE,
            "PRICE_MIN": PRICE_MIN,
            "PRICE_MAX": PRICE_MAX
                      }
 

##далі за евклідовими відстаннями рахуємо 
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
          
                  
                  
            ##щр найближче те і рекомендуємо      
    



  
            
          
          

          


    



@dp.callback_query_handler(text="business")
async def business_callback(query: types.CallbackQuery):
  await query.answer(cache_time=1) 
  await query.message.answer("Ви обрали категорію 'Бізнес'.")
  await query.message.answer("На жаль, я не встиг створити рекомендаційну систему для цієї категорії тарифів.\n"
                            "https://www.lifecell.ua/uk/malii-biznes-lifecell/golovna/")






@dp.message_handler()
async def send_message(message: Message, state):
    if message.text == "Привіт":
        await bot.send_message(chat_id=message.from_user.id, text="Привіт")


if __name__ == '__main__':
    keep_alive()
    executor.start_polling(dp)
