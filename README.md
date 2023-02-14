# TODO list backend application in Python-Flask 
Python 3.11.2
## Steps to run the application

> Clone the repository

    git clone https://github.com/MeLio01/todo_list.git

> Install Poetry

    pip3 install poetry
      
> Jump to project directiory

    cd todo_list

> Activate poetry shell

    poetry shell
      
> Install the dependencies

    poetry install

> Initialize SqlAlchemy Database

    flask db init
    flask db migrate
    flask db upgrade

> Run the application

    python3 manage.py