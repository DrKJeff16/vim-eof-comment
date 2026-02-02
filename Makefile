.PHONY: all help lint build local-install clean run-script docs

all: help

clean:
	@echo "Cleaning..." ## Clean built files
	@rm -rf build dist *.egg-info
	@echo -e "Done!"

distclean: clean ## Clean everything
	@echo "Cleaning Everything..."
	@rm -rf .mypy_cache .ropeproject .pytest_cache
	@echo -e "Done!"

docs: ## Generate Sphinx docs
	@echo -e "Generating docs..."
	@$(MAKE) -C docs html
	@echo -e "Done!"

help: ## Show help
	@echo -e "Usage: make [target]\n\nAvailable targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo

lint: ## Lint files
	@echo "Linting..."
	@pipenv run flake8 vim_eof_comment
	@pipenv run pydocstyle --convention=numpy --match='.*\.py' vim_eof_comment
	# @autopep8 --aggressive --aggressive --aggressive --in-place --recursive vim_eof_comment
	$(eval files := $(shell fd --full-path vim_eof_comment -e py))
	@pipenv run numpydoc lint $(files)
	@echo "Done!"

stubs: lint ## Generate mypy stubs
	@echo "Generating stubs..."
	@pipenv run stubgen --include-docstrings --include-private -v -p vim_eof_comment -o .
	@echo -e "Done!\nRunning isort..."
	@pipenv run isort vim_eof_comment
	@echo -e "Done!\nLinting with mypy..."
	@pipenv run mypy vim_eof_comment
	@echo -e "Done!"

build: stubs ## Build project
	@echo -e "Building..."
	@pipenv run python -m build
	@echo -e "Done!"

local-install: build ## Install project in current pipenv virtual environment
	@echo -e "Installing locally..."
	@pipenv run python -m pip install .
	@echo -e "Done!"

run-script: local-install ## Run the built project
	@echo -e "Running vim-eof-comment..."
	@pipenv run vim-eof-comment -e py,pyi,Makefile,md,yaml,yml,toml -nv .
	@echo -e "Done!"

# vim: set ts=4 sts=4 sw=0 noet ai si sta:
