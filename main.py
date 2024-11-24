import telebot
import requests
import time
from json import loads

SERVER_HOST = 'http://127.0.0.1:5000'

# Создаём экземпляр бота с токеном
API_TOKEN = '7886193892:AAFvRos8PvwtwSUgtqUW4JwtSC19sY580Mc'

bot = telebot.TeleBot(API_TOKEN)

# Стек для хранения сообщений
message_queue = []

# Максимальная длина одного сообщения
MAX_MESSAGE_LENGTH = 1600

# Функция для отправки запроса на сервер
def make_request_to_server(user_message, chat_id):
    try:
        # Отправляем словарь с сообщением пользователя и ID диалога на сервер
        data = {'query': user_message, 'id': chat_id}
        response = requests.post(f'{SERVER_HOST}/invoke', json=data)
        # print(response.json())
        return response.json().get('text', 'нет ответа')
    except Exception as e:
        return f'Ошибка при запросе: {str(e)}'

# Функция для дробления длинного ответа на части
def split_message(message):
    # Разбиваем сообщение на части, если оно слишком длинное
    return [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]

# Функция для обработки сообщений из очереди
def process_queue():
    if message_queue:
        # Получаем следующее сообщение из очереди
        user_message = message_queue.pop(0)

        # Отправляем запрос на сервер
        response = make_request_to_server(user_message['message'], user_message['chat_id'])

        # Дробим ответ, если он слишком длинный
        parts = split_message(response)

        # Отправка ответа пользователю частями
        for part in parts:
            bot.send_message(user_message['chat_id'], part)

        # Запускаем обработку следующего сообщения
        time.sleep(0.2)  # Задержка для предотвращения излишней нагрузки
        process_queue()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('Приветсвие на старте')
    chat_id = message.chat.id  # Получаем chat_id  
    user_first_name = message.from_user.first_name  # Имя пользователя  
    user_last_name = message.from_user.last_name  # Фамилия пользователя (может быть None)  
    
    # Формируем полное имя (можно оставить фамилию пустой, если ее нет)  
    full_name = f"{user_first_name} {user_last_name}" if user_last_name else user_first_name  

    # user initialization
    print(requests.post(f'{SERVER_HOST}/init_user', json={'id': chat_id, 'user_name': full_name}).json())

    welcome_text = '''Привет, я - Телеграмм-бот для
консультации граждан
по государственным
услугам и сервисам.'''
    bot.send_message(message.chat.id, welcome_text)

# Обработчик всех сообщений
@bot.message_handler(content_types='text')
def handle_message(message):
    if message.text.startswith('/'):
        return  # Игнорируем команды
    print('обращение к серверу: ', message.text)
    # Сохраняем сообщение в стек
    message_queue.append({'message': message.text, 'chat_id': message.chat.id})

    # Если в очереди нет других сообщений, начинаем обработку
    if len(message_queue) == 1:
        bot.send_message(message.chat.id, 'Ваше сообщение в обработке')
        process_queue()

# Запуск бота
bot.infinity_polling()
