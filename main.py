import requests 
from bs4 import BeautifulSoup
import telebot

bot =  telebot.TeleBot('5396424319:AAG9jBitflNGqcOcbUgVvYDgy1B-qN2P268')

@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.chat.id,'Привет')
        bot.send_message(message.chat.id, "введите команду /help для того чтобы узнать больше")

@bot.message_handler(commands=['habrTop'])
def habr(message):
    number = 1
    for  i in range(4):
        page = requests.get('https://habr.com/ru/news/page' + str(number))
        soup = BeautifulSoup(page.text, "html.parser")
        blockNews = soup.find_all('article', class_="tm-articles-list__item")
        for newsItems in blockNews:
            viwes = ((newsItems.find('span', class_="tm-icon-counter__value").text).replace('K', "00")).replace(".", "")
            if int(viwes) == 1300:
                articletitle = newsItems.find("a", class_="tm-article-snippet__title-link")
                bot.send_message(message.chat.id, "Статья: " + articletitle.text)
                link = articletitle.get('href')
                bot.send_message( message.chat.id, "Сылка: " +"https://habr.com/" + link)
        number += 1
    bot.send_message(message.chat.id, "Всё!!")

@bot.message_handler(commands=['habr20'])
def habr20(message):
    page = requests.get('https://habr.com/ru/news/')
    soup = BeautifulSoup(page.text, "html.parser")
    blockNews = soup.find_all('article', class_="tm-articles-list__item")
    for newsItems in blockNews:
        articletitle = newsItems.find("a", class_="tm-article-snippet__title-link")
        link = articletitle.get('href')
        viwes = ((newsItems.find('span', class_="tm-icon-counter__value").text).replace('K', "00")).replace(".", "")
        comment = newsItems.find('span', class_='tm-article-comments-counter-link__value')
        bot.send_message(message.chat.id, "Статья: "+ articletitle.text)
        bot.send_message(message.chat.id, 'Комментарии: ' + comment.text)
        bot.send_message(message.chat.id, 'Просмотры: ' + viwes)
        bot.send_message(message.chat.id, "Сылка: " + "https://habr.com" + link)
    bot.send_message(message.chat.id, "Всё!!")

@bot.message_handler(commands=['weather'])
def news(message):
    page = requests.get('https://pogoda.mail.ru/prognoz/ekaterinburg/')
    soup = BeautifulSoup(page.text, 'html.parser')
    newsBlock = soup.find_all('div', class_='day day_index')
    for newsItems in newsBlock:
        dataDay = newsItems.find('div', class_="day__date")
        temperature = newsItems.find('div', class_='day__temperature')
        bot.send_message(message.chat.id, 'Дата:' + dataDay.text)
        bot.send_message(message.chat.id, "Температура" + temperature.text)
    bot.send_message(message.chat.id, "Всё!!")

@bot.message_handler(commands=['igromania'])
def stopgame(message):
    page = requests.get('https://www.igromania.ru/articles/')
    soup = BeautifulSoup(page.text, "html.parser")
    blokNews = soup.select('#uni_com_feed_cont > div > div')
    for newsItems in blokNews:
        articletitle = newsItems.find('a', class_="aubli_name")
        newsdesc = newsItems.find('div', class_='aubli_desc')
        link = articletitle.get('href')
        bot.send_message(message.chat.id, 'Статья: ' + articletitle.text)
        bot.send_message(message.chat.id, newsdesc)
        bot.send_message(message.chat.id, 'Сылка: ' + "https://www.igromania.ru" + link)
    bot.send_message(message.chat.id, "Всё!!")

@bot.message_handler(commands=['sport'])
def sport(message):
    page = requests.get('https://matchtv.ru/news')
    soup = BeautifulSoup(page.text, "html.parser")
    news = soup.find_all('a', class_='node-news-list__item')
    for newsItems in news:
        articletitle = newsItems.find('div', class_='node-news-list__title')
        bot.send_message(message.chat.id, "Статья: " + articletitle.text)
    bot.send_message(message.chat.id, "Всё!!")
        
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Привет")
    bot.send_message(message.chat.id, "Для того чтобы узнать погоду,введите команду /weather")
    bot.send_message(message.chat.id, "для того чтобы узнать новости с 1-ой страницы https://habr.com/ru/news/? введите команду /habr20")
    bot.send_message(message.chat.id, "для того чтобы узнать популярные новости с 4-ох страниц https://habr.com/ru/news/? введиты  команду /habrTop")
    bot.send_message(message.chat.id, "для того чтобы узнать популярные игровые  новости с сайта https://www.igromania.ru/ введите команду /igromania")
    bot.send_message(message.chat.id, "для того чтобы узнать популярные спортивные  новости с сайта https://matchtv.ru/news введите команду /sport")


bot.polling()