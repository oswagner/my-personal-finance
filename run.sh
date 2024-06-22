#!/bin/sh

# Check if poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install dependencies
echo "Installing dependencies..."
poetry install

# Run the Flet app with hot reload
echo "Running the Flet app with hot reload..."
poetry run flet run -d -r main.py