import requests
from bs4 import BeautifulSoup
from src.db.postgre import Advice_raw

from ...utils.logger import loggear


def post_http(fecha):
    url = "https://boletin.tucuman.gov.ar/boletin/view"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = f"fechaBoletin={fecha}"
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text, response.status_code


def get_page_text(text):
    notices = []
    soup = None
    try:
        soup = BeautifulSoup(text, features="html.parser")
        notices = soup.find_all("article", class_="blog-post")[1]
    except Exception as e:
        loggear("ERROR: Crear objeto Soup", "error")
        exit(1)
    return notices


def get_title_subtitle_body(text):

    titles = text.findChildren("h3", class_="pt-5 pb-4 mb-4 fst-italic border-bottom")
    subtitles = text.findChildren("h2", class_="blog-post-title")
    bodies = text.findChildren("p", class_="font-monospace")

    if len(titles) != len(subtitles) != len(bodies):
        loggear(mensaje="Error en el scrapper", tipo="error")
        exit(1)

    return titles, subtitles, bodies


def crear_advices_raw(titles, subtitles, bodies):
    advices_raw = []
    for i in range(len(titles)):
        title = titles[i].text.strip()
        subtitle = subtitles[i].text.strip()
        body = bodies[i].text.strip()

        advices_raw.append(Advice_raw(title=title, subtitle=subtitle, body=body))
    return advices_raw
