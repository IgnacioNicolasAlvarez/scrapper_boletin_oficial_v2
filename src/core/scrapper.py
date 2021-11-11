from bs4 import BeautifulSoup
from datetime import datetime
import requests

today = datetime.today().strftime("%Y-%m-%d")
url = "https://boletin.tucuman.gov.ar/boletin/view"

payload = f"fechaBoletin={today}"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# class="float-end mb-1" volver a 
# class="font-monospace" texto del aviso
# class="blog-post-title" titulo del aviso
# class="class="pt-5 pb-4 mb-4 fst-italic border-bottom" numero del aviso

def run():
    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, "html.parser")
    notices = soup.find_all("article", class_="blog-post")[1]
    #c = [notices[i:i + 4] for i in range(0, len(notices), 4)]
    print(notices.findChildren("h3", class_="pt-5 pb-4 mb-4 fst-italic border-bottom"))
    print(notices.findChildren("h2", class_="blog-post-title"))
    print(notices.findChildren("p", class_="font-monospace"))
