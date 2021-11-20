from datetime import datetime
from logging import log

import requests
from bs4 import BeautifulSoup

from ..db.postgre import insert_advice
from ..utils.conversion import reemplazar
from ..utils.logger import loggear
from ..utils.regex import aplicar_regex_title

today = datetime.today().strftime("%Y-%m-%d")
url = "https://boletin.tucuman.gov.ar/boletin/view"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}


def run(fecha: str = today):

    payload = f"fechaBoletin={fecha}"
    response = requests.request("POST", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text)

    notices = soup.find_all("article", class_="blog-post")[1]

    titles = notices.findChildren(
        "h3", class_="pt-5 pb-4 mb-4 fst-italic border-bottom"
    )
    subtitles = notices.findChildren("h2", class_="blog-post-title")
    bodies = notices.findChildren("p", class_="font-monospace")

    if len(titles) != len(subtitles) != len(bodies):
        loggear(mensaje="Error en el scrapper", tipo="error")
        return

    for i in range(len(titles)):
        title = titles[i].text.strip()

        aux = aplicar_regex_title(title)
        nro_aviso = reemplazar(aux, ".", "", fuction=int)

        subtitle = subtitles[i].text.strip()
        body = bodies[i].text.strip()

        insert_advice(nro_aviso, title, subtitle, body)
