# Flet Personal Finance App

This is a personal finance application built using Flet. The app allows you to add and view expenses.

## Prerequisites

- Python 3.10 or higher
- Poetry

## Setup

### Automated Setup

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the setup script**:

   ```sh
   ./run.sh
   ```

This script will:

- Check if Poetry is installed and install it if necessary.
- Install the project dependencies.
- Run the Flet application with hot reload enabled.

### Manual Setup

If you prefer to run the steps manually, follow these instructions:

1. **Install Poetry** (if not already installed):

   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install dependencies**:

   ```sh
   poetry install
   ```

3. **Run the Flet app with hot reload**:

   ```sh
   poetry run flet run -d -r main.py
   ```

## File Structure

```sh
.
├── data
│   └── expense_repository.py  # In-memory repository for storing expenses
├── presentation
│   └── add_expense_page.py    # Implementation of the Add Expense page
├── use_cases
│   ├── add_expense.py         # Use case for adding an expense
│   └── get_expenses.py        # Use case for retrieving expenses
├── utils
│   ├── json_formatter.py      # JSON formatter for logging
│   └── logger_wrapper.py      # Logger wrapper
├── main.py                    # Main application entry point
├── run.sh                     # Script to set up and run the application
└── README.md                  # Project documentation
```

## Usage

### Adding an Expense

1. Run the application using the setup script or manually.
2. Fill in the details for the new expense in the form:
   - Date
   - Description
   - Category (e.g., Food, Transport, Entertainment, Electronics, Others)
   - Amount
   - Payment Method (e.g., Credit Card, Debit Card, Cash, Other)
   - Installments (if any)
   - Installment Amount (if any)
   - Payment Month
   - Notes (optional)
3. Click "Add Expense" to save the expense.

## Troubleshooting

If you encounter any issues, make sure that:

- You have Python 3.10 or higher installed.
- Poetry is installed and available in your system's PATH.

For more details, refer to the [official Flet documentation](https://flet.dev/docs/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
