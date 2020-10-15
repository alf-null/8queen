# 8queen

This is an implementation for nQueens problem using backtracing.
It is packet with docker-compose to set everything up.

Docker-compose contains:
    
    - Postgres DB
    - Adminer
    - 8queens

To build the containers use :
`$ docker-compose -f docker-compose.yaml up`

once everything is running use:
`$ docker exec -i -t 8queen_8queens_1 bash`
That would propt you a bash inside the solution containerm, the use
`$ pipenv run python main.py 8`
You can also any use other number
