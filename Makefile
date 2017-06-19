.PHONY: build

PYTHON ?= python
HOST    = 0.0.0.0
PORT    = 3001

install:
	cat requirements/*.txt > requirements.txt

	pip install -r requirements.txt

	bundler install

build:
	$(PYTHON) -B -m build

	bundle exec jekyll build

serve:
	bundle exec jekyll serve --host=$(HOST) --port=$(PORT)

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	rm -rf _site .sass-cache _config.yml

	clear

all:
	make clean install build serve
