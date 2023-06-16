build:
	docker-compose build

generate:
	export FILENAME=$(FILENAME);
	docker-compose run app python main.py $(FILENAME) || true
