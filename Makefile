.PHONY: install dev-backend dev-frontend deps clean deploy

install:
	@echo "Installing backend dependencies...."
	@pip install -r backend/src/requirements.txt
dev-backend:
	@echo "Starting backend server...."
	@cd backend/src/core && uvicorn main:app --reload
deps:
	@pip-compile -v backend/src/requirements.in
deploy:
	@okteto context use "https://cloud.okteto.com"
	@okteto deploy -n varun-dhruv --build
clean:
