import flet as ft
from data.expense_repository import InMemoryExpenseRepository
from use_cases.add_expense import AddExpense
from presentation.add_expense_page import AddExpensePage
from colors import AppColors
from utils.logger_wrapper import LoggerWrapper

def main(page: ft.Page):
    # Configurar logging
    logger_wrapper = LoggerWrapper(__name__)

    repository = InMemoryExpenseRepository()
    add_expense_use_case = AddExpense(repository)
    add_expense_page = AddExpensePage(add_expense_use_case, logger_wrapper)

    # Configure the page colors
    page.bgcolor = AppColors.LIGHT_GRAY.value  # Cinza Claro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # Log page initialization
    logger_wrapper.info({"event": "init", "message": "Initializing the add expense page"})

    # Initialize with the add expenses page
    add_expense_view = add_expense_page.create_page()
    page.add(add_expense_view)
    page.update()

    # Log completion of initialization
    logger_wrapper.info({"event": "init", "message": "Application initialized successfully"})

if __name__ == "__main__":
    ft.app(target=main)