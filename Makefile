.PHONY: all help lint build local-install upload clean sign run-script

all: help

clean:
	@rm -rf build dist *.egg-info

distclean: clean
	@rm -rf .mypy_cache .ropeproject

help:
	@echo -e "Available targets:\n  help\n  lint\n  build\n  sign\n  local-install\n  stubs\n  run-script\n  upload\n  clean\n"

lint:
	@flake8 --statistics --show-source --color=always --max-line-length=100 --ignore=D401 \
		--exclude .tox,.git,*staticfiles*,build,locale,docs,tools,venv,.venv,*migrations*,*.pyc,*.pyi,__pycache__,test_*.py \
		.
	@isort vim_eof_comment
	@mypy vim_eof_comment

stubs:
	@stubgen --include-docstrings --include-private -p vim_eof_comment -o .

build: stubs
	@python3 -m build &> /dev/null

sign:
	@pypi-attestations sign dist/*

local-install: build
	@python3 -m pip install .

run-script:
	@vim-eof-comment -e py,pyi -n .

upload:
	@twine upload dist/*
