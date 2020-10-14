#!/bin/bash

# To run all tests: ./bin/tests.sh
# To run unit tests: ./bin/tests.sh unit

if [ -z "$1" ]
then
    DIR="test"
else
    DIR="test/$1"
fi

export ENVIRON=test
export PYTHONPATH=./src
pipenv run pytest -s $DIR
