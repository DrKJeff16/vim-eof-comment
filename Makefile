.PHONY: all help lint build local-install clean run-script docs format

all: run-script

clean: ## Clean built files
	@echo "Cleaning..."
	@rm -rf build dist *.egg-info
	@echo "Done!"

distclean: clean ## Clean everything
	@echo "Cleaning Everything..."
	@rm -rf .mypy_cache .ropeproject .pytest_cache
	@echo "Done!"

docs: ## Generate Sphinx docs
	@echo "Generating docs..."
	@$(MAKE) -C docs html
	@echo "Done!"

help: ## Show help
	@echo -e "Usage: make [target]\n\nAvailable targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo

lint: ## Lint files
	@echo "Running flake8..."
	@pipenv run flake8 vim_eof_comment
	@echo -e "Done!\n\nRunning pydocstyle..."
	@pipenv run pydocstyle --convention=numpy --match='.*\.py' vim_eof_comment
	$(eval files := $(shell fd --full-path vim_eof_comment -e py))
	@echo -e "Done!\n\nLinting with numpydoc..."
	@pipenv run numpydoc lint $(files)
	@echo "Done!"

stubs: lint ## Generate mypy stubs
	@echo "Generating stubs..."
	@pipenv run stubgen --include-docstrings --include-private -v -p vim_eof_comment -o .
	@echo -e "Done!\n\nRunning isort..."
	@pipenv run isort vim_eof_comment
	@echo -e "Done!\n\nChecking typing with mypy..."
	@pipenv run mypy vim_eof_comment
	@echo "Done!"

format: stubs ## Format using Ruff
	@echo "Formatting with Ruff..."
	@pipenv run ruff format vim_eof_comment
	@echo -e "Done!\n\nChecking with Ruff..."
	@pipenv run ruff check vim_eof_comment
	@echo "Done!"

build: format ## Build project
	@echo "Building..."
	@pipenv run python -m build
	@echo "Done!"

local-install: build ## Install project in current pipenv virtual environment
	@echo "Installing locally..."
	@pipenv run python -m pip install .
	@echo "Done!"

run-script: local-install ## Run the built project
	@echo "Running vim-eof-comment..."
	@pipenv run vim-eof-comment -e py,pyi,Makefile,md,yaml,yml,toml -nv .
	@echo "Done!"

# vim: set ts=4 sts=4 sw=0 noet ai si sta:
