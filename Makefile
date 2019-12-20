prepare:
	python3 db_create.py
	flask db init
	flask db migrate -m "user table"
	flask db upgrade
	python3 create_user.py
