import mechanicalsoup as ms

from datetime import datetime
import requests

today = datetime.today().strftime("%Y-%m-%d")
url = "https://boletin.tucuman.gov.ar/boletin/view"

payload = f"fechaBoletin={today}"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "ci_session=fvbho0m1t7q0nhalep2jkgcpuhm761hg",
}


def run():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


# browser = ms.StatefulBrowser()
