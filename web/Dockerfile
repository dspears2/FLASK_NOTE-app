FROM tiangolo/uwsgi-nginx-flask:python3.9
#RUN app --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY . /app
RUN pip install -r /var/www/requirements.txt

CMD python main.py