FROM  python:3.8
WORKDIR /8queens

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system 
COPY src .
