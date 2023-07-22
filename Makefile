start:
	cp example.env .env
	docker build -t flaskapp:latest .
	docker run -d -p 8000:8000 flaskapp
build:
	docker build -t flaskapp:latest .
up:
	docker run -d -p 8000:8000 flaskapp
stop:
	docker stop $$(docker ps -a -q)
test:
	pytest