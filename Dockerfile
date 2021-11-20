FROM python:3.9

WORKDIR /usr/src/app
RUN apt install g++ gcc libxslt-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]