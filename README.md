# TODO list backend application in Python-Flask 
Python 3.11.2
## Steps to run the application locally

> Clone the repository

    git clone https://github.com/MeLio01/todo_list.git

      
> Jump to project directory

    cd todo_list

> Activate the virtual environment and install dependencies

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

> Initialize SqlAlchemy Database

    flask db init
    flask db migrate
    flask db upgrade

> Run the application

    flask run

----------------------------------------------------------

## Steps to run the Docker Container

> Install Docker in your system

> Run the docker container 

    docker-compose up
