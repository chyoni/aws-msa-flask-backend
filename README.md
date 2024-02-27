# Owner Service by Flask

### Init
```bash
touch main.py
touch requirements.txt
touch Dockerfile
touch docker-compose.yml
```

### Venv
```bash
python3 -m venv ./venv
source ./venv/bin/activate
```

### Dependencies
```bash
Flask
FlaskSQLAlchemy
SQLAlchemy
Flask-Migrate
Flask-Script
Flask-Cors
requests
mysqlclient
pika
```

### DB Migrate

```bash
1. Go inside the backend container
2. Execute following commands.

export FLASK_APP=main
flask db init
flask db migrate
flask db upgrade

```