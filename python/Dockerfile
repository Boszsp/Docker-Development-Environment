FROM python:3.12.3-alpine3.19
WORKDIR /home
COPY requirements.txt  /home/requirements.txt
RUN pip install -r /home/requirements.txt
CMD [ "python","/home/main.py" ]
