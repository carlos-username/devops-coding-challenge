FROM python:3

ARG APP_PORT
RUN mkdir -p /opt/app
COPY source /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD python -u app_get.py 5000