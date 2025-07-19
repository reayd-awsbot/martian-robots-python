# Source directories for the application code
SOURCE_DIR := src/

# Source directories for tests
TESTS_DIR:=tests/

## Testing targets...
test:
	@echo "Running pytest with coverage and cache clear..."
	@PYTHONPATH=$(SOURCE_DIR) poetry run pytest \
		--cache-clear \
		--cov=. \
		$(TESTS_DIR) \
		--cov-report=term \
		--cov-report=html

# Check-in code after formatting
checkin: black tests ## Perform a check-in after formatting the code
    ifndef COMMIT_MESSAGE
		$(eval COMMIT_MESSAGE := $(shell bash -c 'read -e -p "Commit message: " var; echo $$var'))
    endif
	@git add --all; \
	  git commit -m "$(COMMIT_MESSAGE)"; \
	  git push

# Run pylint on the codebase
lint: ## Run pylint on the codebase
	@echo "Running pylint..."
	PYTHONPATH=$(SOURCE_DIR) poetry run pylint .

# Check code formatting using Black
check-black: ## Check code formatting with Black
	@echo "Checking code formatting with Black..."
	@poetry run black --check .

# Format code using Black
black: ## Format code using Black
	@echo "Formatting code with Black..."
	@poetry run black .

run:
	@echo "Running script..."
	@python $(SOURCE_DIR)/martian_robots/v1/main.py < $(TESTS_DIR)/fixtures/input.txt

# Install project environment dependencies
install: ## Install project environment dependencies
	@echo "Installing project environment dependencies..."
	@poetry install