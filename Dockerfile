# base image
FROM ubuntu:18.04

# sets up the working directory in the container
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY form.html /app/form.html

# install flask
RUN pip install Flask

COPY . /app

CMD [ "python" , "./app.py" ]
