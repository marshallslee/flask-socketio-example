FROM python:3
MAINTAINER Marshall Lee <marshall.s.lee@gmail.com>

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 12380

CMD python app.py