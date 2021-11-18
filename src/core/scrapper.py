from bs4 import BeautifulSoup
from datetime import datetime
import requests

today = datetime.today().strftime("%Y-%m-%d")
url = "https://boletin.tucuman.gov.ar/boletin/view"

payload = f"fechaBoletin={today}"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}


def run():
    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, "html.parser")

    notices = soup.find_all("article", class_="blog-post")[1]
    titles = notices.findChildren(
        "h3", class_="pt-5 pb-4 mb-4 fst-italic border-bottom"
    )
    subtitles = notices.findChildren("h2", class_="blog-post-title")
    bodies = notices.findChildren("p", class_="font-monospace")

    if len(titles) != len(subtitles) != len(bodies):
        print("Error en el scrapper")
        return

    dict_advice = []
    for i in range(len(titles)):
        title = titles[i].text.strip()
        subtitle = subtitles[i].text.strip()
        body = bodies[i].text.strip()

        dict_advice.append({"title": title, "subtitle": subtitle, "body": body})

    print(dict_advice)
