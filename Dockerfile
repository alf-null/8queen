FROM  python:3.8
WORKDIR /8queens

RUN pip install pipenv
RUN pipenv install
COPY . .

RUN ["pipenv", "run", "python", "src/n_queens.py"]