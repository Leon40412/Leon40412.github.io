import telebot
import webbrowser
from telebot import types
import random
import sqlite3
import requests
import json
import datetime
import time

bot = telebot.TeleBot("6527541829:AAEUIVybXadehmNi-nTVcLzh0uKtnqxClhk")
API = '287815fc4ac76b92a8035c5790c7f102'
i = 1
i2 = 1


# Это Кнопки
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    
    btn11 = types.KeyboardButton("⚡ Как дела?")
    btn12 = types.KeyboardButton("🎲 (D&D) Бросок кубика")
    btn13 = types.KeyboardButton("🌄 Прикольные картинки")
    markup.row(btn11, btn12, btn13)

    btn14 = types.KeyboardButton("☔ Погода - узнать температуру")
    btn15 = types.KeyboardButton("🌅 Время до Лета")
    markup.row(btn14, btn15)
    
    btn16 = types.KeyboardButton("📞 Служба поддержки")
    btn17 = types.KeyboardButton("📄 Информация о боте") 
    btn18 = types.KeyboardButton("🔨 Функции бота")
    btn19 = types.KeyboardButton("📣 Обновления")
    markup.row(btn16, btn17, btn18, btn19)

    bot.send_message(message.chat.id, f"Приветствую, {message.from_user.first_name}!\nВерсия бота: 1.2.1!", reply_markup=markup)




# Это функции кнопок
@bot.message_handler()
def on_click(message):
    if message.text == "⚡ Как дела?":
        global i2
        if i2 == 1:
            bot.send_message(message.chat.id, f"Всё хорошо, {message.from_user.first_name}!")
            i2 += 1
        elif i2 == 2:
            bot.send_message(message.chat.id, f"Замечательно, {message.from_user.first_name}!")
            i2 += 1
        elif i2 == 3:
            bot.send_message(message.chat.id, f"У меня всё круто, а у тебя {message.from_user.first_name}?")
            i2 += 1
        elif i2 == 4:
            bot.send_message(message.chat.id, f"Всё отлично, {message.from_user.first_name}!")
            i2 = 1        
      
    
    elif message.text == "📞 Служба поддержки":
        bot.send_message(message.chat.id, '<b>📝 Гугл форма для вопросов, отзывов, ошибок: </b>https://forms.gle/m5vfA9U4emVW5mbH9', parse_mode="html")             
    
    
    elif message.text == "📄 Информация о боте":
        bot.send_message(message.chat.id, '<b>💾 Справочная информация:</b>\n<b>Версия бота: 1.2</b>\n<b>Последнее изменение: 03.01.2024</b>\n<b>Дата создания: 18.12.2023</b>\n\n<b>📢 Присоединиться к каналу Автора с новостями о проекте</b> - https://t.me/+gHGAUmk3FiQwNTUy', parse_mode="html")
    
    
    elif message.text == "🔨 Функции бота":
        bot.send_message(message.chat.id, '<b>Доступные команды:</b>\n/start - Запуск бота.\n\nДля того чтобы обновить бота, введите команду /start ещё раз.', parse_mode="html")
    
    
    elif message.text == "📣 Обновления":
        bot.send_message(message.chat.id, """
                         <b>📋 Обновление версии 1.2.1 от 09.02.2024</b>\n<b>Добавления и изменения:</b>
                         \n<b>1.</b> Изменения в функции "⚡ Как дела?".
                         \n<b>2.</b> Оптимизация файлов.                        
                         
                         
                         \n\n\n<b>📋 Обновление версии 1.2 от 03.01.2024</b>\n<b>Добавления и изменения:</b>
                         \n<b>1. Обновление функции "🎲 Случайное число 1-100":</b>
  - Добавленна полноценная генерация чисел по системе днд. Навигация осуществленна путём нажатия на встроенные кнопки. В функцию добавленна справка - статья.
<b>1.1</b> Изменено название "🎲 Случайное число 1-100" → "🎲 (D&D) Бросок кубика".
                         \n<b>2. Обновление функции "🎄 Время до Нового года" → "🌅 Время до Лета".</b>
  - С наступившим! Теперь отсчёт идёт до начала Лета этого года (01.06.2024).
<b>2.1</b> Изменено название "🎄 Время до Нового года" → "🌅 Время до Лета".
                         \n<b>3. Изменён алгоритм работы функции "🌄 Прикольная картинка":</b>
  - Теперь картинки будут идти по порядку, а после просмотра последней очередь будет обнуляться.
<b>3.1</b> Изменено название "🌄 Прикольная картинка" → "🌄 Прикольные картинки".
<b>3.2</b> Добавленно 2 новые картинки.                         
                         \n<b>4. Изменён алгоритм работы функции "⚡ Как дела?":</b>
  - Теперь ответы будут идти по порядку, а после последнего ответа очередь будет обнуляться.                         
                         \n<b>5. Обновленно приветствие:</b>
  - Теперь, после ввода команды "/start" будет выводиться текущая версия бота.
                         \n<b>6. Был оптимизирован файл-менеджмент.</b>

                         
                         \n\n\n<b>📋 Обновление версии 1.1 от 29.12.2023</b>\n<b>Добавления и изменения:</b>
                         \n<b>1.</b> Добавлена функция "🎄 Время до Нового года"
                         
                         
                         \n\n\n<b>📋 Обновление версии 1.0 от 24.12.2023</b>\n<b>Добавления и изменения:</b>
                         \n<b>1.</b> С версии 1.0 доступ к боту открыт для всех пользователей!
                         \n<b>2.</b> Изменение нумерации версий бота. В рамках изменений, версия [0.3.0 = 1.0].
                         \n<b>3.</b> Добавленна функция "☔ Погода - узнать температуру".
                         \n<b>4.</b> Добавленна функция "📣 Обновления".
                         \n<b>5.</b> Обновление нескольких функций.
                         \n<b>6.</b> Бета тестирование базы данных - завершено.
                         """, parse_mode="html")    
    
    
    elif message.text == "🌄 Прикольные картинки":
        global i
        if i == 1:
            file1 = open("./files/kartinka/kot2.jpg", "rb")
            bot.send_photo(message.chat.id, file1)
            i += 1
        elif i == 2:
            file2 = open("./files/kartinka/kot.jpg", "rb")
            bot.send_photo(message.chat.id, file2)
            i += 1
        elif i == 3:
            file3 = open("./files/kartinka/sobaka.jpg", "rb")
            bot.send_photo(message.chat.id, file3)
            i += 1
        elif i == 4:
            file4 = open("./files/kartinka/razrih.jpg", "rb")
            bot.send_photo(message.chat.id, file4)
            i += 1
        elif i == 5:
            file4 = open("./files/kartinka/pagan.jpg", "rb")
            bot.send_photo(message.chat.id, file4)
            i += 1
        elif i == 6:
            file4 = open("./files/kartinka/rib.jpg", "rb")
            bot.send_photo(message.chat.id, file4)
            i += 1
        elif i == 7:
            file4 = open("./files/kartinka/kot3.jpg", "rb")
            bot.send_photo(message.chat.id, file4)
            i += 1
        elif i == 8:
            file4 = open("./files/kartinka/susi.jpg", "rb")
            bot.send_photo(message.chat.id, file4)
            i = 1                        
    
    
    elif message.text == "☔ Погода - узнать температуру":
        bot.send_message(message.chat.id, "Введите название города")
        bot.register_next_step_handler(message, get_weather)
    
    
    elif message.text == "🌅 Время до Лета":       
        target_date = datetime.datetime(2024, 6, 1)
        now = datetime.datetime.now()
        delta = target_date - now
        days = delta.days
        hours = delta.seconds // 3600
        minutes = delta.seconds % 3600 // 60
        seconds = delta.seconds % 60
        
        ndays = ""
        nhours = ""
        nminutes = ""
        nseconds = ""
        
        # Можно было модефицировать посредством: если осталось 0 минут писать: 1 день 1 час 1 секудна.
        if days == 1 or days % 10 == 1 and days != 11:
            ndays = "день"
        elif days == 2 or days == 3 or days == 4 or days % 10 == 2 or days % 10 == 3 or days % 10 == 4 and not((days // 10) % 10 == 1):
            ndays = "дня"
        elif days <= 5 or not days % 10 == 2 or not days % 10 == 3 or not days % 10 == 4 or (days // 10) % 10 == 1:
            ndays = "дней"

        if hours == 1 or hours % 10 == 1 and hours != 11:
            nhours = "час"
        elif hours == 2 or hours == 3 or hours == 4 or hours % 10 == 2 or hours % 10 == 3 or hours % 10 == 4 and not((hours // 10) % 10 == 1):
            nhours = "часа"
        elif hours <= 5 or not hours % 10 == 2 or not hours % 10 == 3 or not hours % 10 == 4 or (hours // 10) % 10 == 1:
            nhours = "часов"

        if minutes == 1 or minutes % 10 == 1 and minutes != 11:
            nminutes = "минута"
        elif minutes == 2 or minutes == 3 or minutes == 4 or minutes % 10 == 2 or minutes % 10 == 3 or minutes % 10 == 4 and not((minutes // 10) % 10 == 1):
            nminutes = "минуты"
        elif minutes <= 5 or not minutes % 10 == 2 or not minutes % 10 == 3 or not minutes % 10 == 4 or (minutes // 10) % 10 == 1:
            nminutes = "минут"

        if seconds == 1 or seconds % 10 == 1 and seconds != 11:
            nseconds = "секундa"
        elif seconds == 2 or seconds == 3 or seconds == 4  or seconds % 10 == 2 or seconds % 10 == 3 or seconds % 10 == 4 and not((seconds // 10) % 10 == 1):
            nseconds = "секунды"
        elif seconds <= 5 or not seconds % 10 == 2 or not seconds % 10 == 3 or not seconds % 10 == 4 or (seconds // 10) % 10 == 1:
            nseconds = "секунд"       

        if days == 0:
            if hours == 0:
                if minutes == 0:
                    if seconds == 0:
                        bot.send_message(message.chat.id, f"С новым годом!")    
                    else:
                        bot.send_message(message.chat.id, f"<b>🌅 До начала Лета осталось:</b> \n{seconds} {nseconds}! \nОсталось совсем немного!", parse_mode="html")    
                else:
                    bot.send_message(message.chat.id, f"<b>🌅 До начала Лета осталось:</b> \n{minutes} {nminutes}, {seconds} {nseconds}! \nОсталось совсем немного!", parse_mode="html")        
            else:
                bot.send_message(message.chat.id, f"<b>🌅 До начала Лета осталось:</b> \n{hours} {nhours}, {minutes} {nminutes}, {seconds} {nseconds}! \nОсталось совсем немного!", parse_mode="html") 
        else:
            bot.send_message(message.chat.id, f"<b>🌅 До начала Лета осталось:</b> \n{days} {ndays}, {hours} {nhours}, {minutes} {nminutes}, {seconds} {nseconds}! \nОсталось совсем немного!", parse_mode="html")    
        file5 = open("./files/time/leto.gif", "rb")
        bot.send_video(message.chat.id, file5)


    elif message.text == "🎲 (D&D) Бросок кубика":
        markup = types.InlineKeyboardMarkup()

        btn21 = types.InlineKeyboardButton("Бросить кубик d4/к4", callback_data="d4")
        markup.row(btn21)
        
        btn22 = types.InlineKeyboardButton("Бросить кубик d6/к6", callback_data="d6")
        markup.row(btn22)

        btn23 = types.InlineKeyboardButton("Бросить кубик d8/к8", callback_data="d8")
        markup.row(btn23)

        btn24 = types.InlineKeyboardButton("Бросить кубик d10/к10", callback_data="d10")
        markup.row(btn24)

        btn25 = types.InlineKeyboardButton("Бросить кубик d12/к12", callback_data="d12")
        markup.row(btn25)

        btn26 = types.InlineKeyboardButton("Бросить кубик d20/к20", callback_data="d20")
        markup.row(btn26)

        btn27 = types.InlineKeyboardButton("Бросить кубик d100/к100", callback_data="d100")
        markup.row(btn27)
        
        bot.reply_to(message, """
                     <b>Описание функции:</b>
                     \nЭта функция может подбросить кубик (сгенерировать случайное число) по системе Dungeons & Dragons (D&D).
                     \nD&D существует 6 видов кубов: d4, d6, d8, d10, d12, d20 и d100 (получемый сложением бросков кубка d10 и кубика с десятками) | d от dice (кубик), есть вариант "к" (к6) от кубик.
                     \nФункция "Бросок кубика" может быть полезна как и при игре в Dungeons & Dragons так и просто для генерации случайных чисел!
                     \n
                     \nПосле нажатия на определённую кнопку для повторного нажатия подождите несколько секунд или используйте команду "Бросок кубика" заного.  
                     """, reply_markup=markup, parse_mode="html")




@bot.callback_query_handler(func=lambda callback: True)
def supernumber(callbackDND):
    file6 = open("./files/dnd/d20.gif", "rb")
    bot.send_video(callbackDND.message.chat.id, file6)
    if callbackDND.data == "d4":
        random100 = random.randint(1, 4)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d4: {random100}', parse_mode="html")   
    elif callbackDND.data == "d6":
        random100 = random.randint(1, 6)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d6: {random100}', parse_mode="html")
    elif callbackDND.data == "d8":
        random100 = random.randint(1, 8)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d8: {random100}', parse_mode="html")
    elif callbackDND.data == "d10":
        random100 = random.randint(1, 10)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d10: {random100}', parse_mode="html")                    
    elif callbackDND.data == "d12":
        random100 = random.randint(1, 12)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d12: {random100}', parse_mode="html")         
    elif callbackDND.data == "d20":
        random100 = random.randint(1, 20)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d20: {random100}', parse_mode="html")
    elif callbackDND.data == "d100":
        random100 = random.randint(1, 100)
        bot.send_message(callbackDND.message.chat.id, f'Результат броска d100: {random100}', parse_mode="html")  




def get_weather(message):
    city1 = message.text
    city = city1.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        dataw = json.loads(res.text)
        temp = dataw['main']['temp']
        bot.reply_to(message, f"Сейчас температура в городе {city1}: {temp} °C")

        image = "dontcold.jpg" if temp > 5.0 else "cold.jpg"
        filew = open("./files/temp/" + image, "rb")
        bot.send_photo(message.chat.id, filew)
    else:
        bot.reply_to(message, "Город указан не верно")




bot.polling(none_stop=True)