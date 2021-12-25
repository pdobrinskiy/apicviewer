FROM docker.io/ciscotestautomation/pyats:latest


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
