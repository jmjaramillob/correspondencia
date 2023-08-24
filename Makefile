.IPHONY: start
start: 
	poetry run python manage.py runserver

.IPHONY: migrations
migrations:
	poetry run python manage.py makemigrations