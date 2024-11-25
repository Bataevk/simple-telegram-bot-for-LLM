# Telegram Bot for Consulting Users

Telegram bot for consulting users on system data using lightRAG technology.

## Содержание

- [Telegram Bot for Consulting Users](#telegram-bot-for-consulting-users)
  - [Содержание](#содержание)
  - [Требования](#требования)
  - [Установка](#установка)
  - [Настройка](#настройка)
  - [Запуск бота](#запуск-бота)
  - [Использование](#использование)
  - [Пример использования](#пример-использования)

## Требования

1. **Python 3.x**
2. **Библиотеки:**
   - `telebot`
   - `requests`

## Установка

1. **Установите необходимые библиотеки:**
   ```sh
   pip install telebot requests
   ```

## Настройка

1. **Создайте файл `config.py` и добавьте в него следующие настройки:**
   ```python
   SERVER_HOST = 'YOUR_SERVER_HOST'
   API_TOKEN = 'YOUR_API_TOKEN'
   ```

2. **Замените `YOUR_SERVER_HOST` и `YOUR_API_TOKEN` на ваши значения.**

## Запуск бота

1. **Запустите бота с помощью команды:**
   ```sh
   python bot.py
   ```

## Использование

1. **Откройте Telegram и найдите вашего бота по имени или через поиск.**
2. **Начните диалог с ботом, отправив команду `/start`.**
3. **Отправляйте текстовые сообщения боту для получения консультаций.**

## Пример использования

1. **Отправка команды `/start`:**
   ```
   Привет, я - Телеграмм-бот для
   консультации граждан
   по государственным
   услугам и сервисам.
   ```

2. **Отправка текстового сообщения:**
   ```
   Ваше сообщение в обработке
   ```
