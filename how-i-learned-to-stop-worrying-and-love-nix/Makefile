.DEFAULT_GOAL := help

NPM_PATH := node_modules/.bin

REVEAL_BIN := $(NPM_PATH)/reveal-md
REVEAL_OPTS := 
REVEAL_TARGET := main.md
REVEAL_SOURCES := $(REVEAL_TARGET) style.css

REVEAL := $(REVEAL_BIN) $(REVEAL_TARGET) $(REVEAL_OPTS)

# Porcelain
# ###############
.PHONY: ci build lint setup

serve: setup ## show presentation in local browser
	$(REVEAL) -w

ci: setup lint build ## run all tests and build all artifacts
	@echo "Not implemented"; false

build: setup ## create artifact
	$(REVEAL) --static dist

lint: ## run static analysis
	@echo "Not implemented"; false


# Plumbing
# ###############
.PHONY: setup

setup: node_modules


node_modules:
	yarn install --frozen-lockfile --ignore-engines

# Utilities
# ###############
.PHONY: help
help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
