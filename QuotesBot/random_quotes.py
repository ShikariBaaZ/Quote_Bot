import random
import requests
from bs4 import BeautifulSoup
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def random_quote():
    URL = "https://www.brainyquote.com/topics/random-quotes"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    result_divs = soup.find_all("div", attrs={"class": "grid-item qb clearfix bqQt"})
    quotes = {}
    for result_div in result_divs:
        soup = BeautifulSoup(str(result_div), 'lxml')
        contents = soup.find_all("a")
        quote = contents[0].text.replace("\n", "")
        author = contents[1].text
        id = result_div.attrs['id']
        quotes[id] = [quote, author]
    articles = []
    for value in quotes.values():
        author = value[1]
        quote = value[0]
        result = InlineQueryResultArticle(
            title=author,
            input_message_content=InputTextMessageContent("ıllıllı★ 𝐐𝐮𝐨𝐭𝐞𝐬 𝐁𝐨𝐭 ★ıllıllı \n\n" + quote + "\n\n~ " + author),
            url="https://t.me/ShikariSupportNetwork",
            description=quote,
            thumb_url="https://telegra.ph/file/e3ef1e11030e1297061d6.jpg",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨ Search More Quotes ✨", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("♥ Support Group ♥", url="https://t.me/ShikariSupportNetwork")]
                ]
            ),
        )
        articles.append(result)
    article = random.choice(articles)
    return article
