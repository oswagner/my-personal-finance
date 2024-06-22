#!/bin/sh

# Function to display usage
usage() {
    echo "Usage: $0 [--ios]"
    exit 1
}

# Parse command line arguments
TARGET="default"
while [ "$1" != "" ]; do
    case $1 in
        --ios )  TARGET="ios"
                 ;;
        * )      usage
                 exit 1
    esac
    shift
done

# Check if poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install dependencies
echo "Installing dependencies..."
poetry install

# Run the Flet app
if [ "$TARGET" = "ios" ]; then
    echo "Running the Flet app on iOS..."
    poetry run flet run -d -r --ios main.py
else
    echo "Running the Flet app with hot reload..."
    poetry run flet run -d -r main.py
fi