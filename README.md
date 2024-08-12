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

### Run Flask API

Activate Poetry Shell

`poetry shell`

Run the Application

`python run.py`

Use Postman to POST to http://127.0.0.1:5000/user using the following test json in the body:
```
    {
        "username": "john_doe",
        "password": "securepassword",
        "profile": {
            "email": "john_doe@example.com",
            "name": "John Doe",
            "age": 30
        }
    }
```

This should return status 201 with the added user

Then make a GET request to http://127.0.0.1:5000/users to receive and array of users returned with status 200

### Run Unit tests

The following command with write the coverage report to coverage.json, coverage.lcov, and to htmlcov/index.html

`poetry run pytest --cov=flask_app --cov-report=html --cov-report=lcov --cov-report=json`