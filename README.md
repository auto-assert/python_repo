# python_repo

## Getting Started

This app creates an API that sets and gets a user data:

### Routes

/user

Receives a POST request to create a user and returns the created user data with 201 status

/users

Returns all the users that were created with 200 status

## Prequisites

Install poetry using either method below:

#### Method 1

Run the following command

`curl -sSL https://install.python-poetry.org | python3 -`

Add poetry to your path

`export PATH="$HOME/.local/bin:$PATH"`

Verify the version

`poetry --version`

#### Method 2

Install using Homebrew

Update Homebrew

`brew update`

Install Poetry

`brew install poetry`

Verify the version

`poetry --version`

### Install application dependencies

`poetry install`

### Run Unit tests

The following command with write the coverage report to coverage.json, coverage.lcov, and to htmlcov/index.html

`poetry run pytest --cov=flask_app --cov-report=html --cov-report=lcov --cov-report=json`