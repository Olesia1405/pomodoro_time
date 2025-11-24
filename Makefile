.DEFAULT_GOAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

run: ## Run the application using uvicorn with provided arguments or defaults
	poetry run uvicorn main:app --host $(HOST) --port $(PORT) --reload --env-file $(ENV_FILE)

install: ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstall dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

migrate-create: ## Create a new Alembic migration
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply: ## Apply all pending migrations
	alembic upgrade head

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " %-20s %s\n", $$1, $$2}'