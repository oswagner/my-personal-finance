import flet as ft
from data.expense_repository import InMemoryExpenseRepository
from use_cases.add_expense import AddExpense
from presentation.add_expense_page import AddExpensePage
from colors import AppColors

def main(page: ft.Page):
    repository = InMemoryExpenseRepository()
    add_expense_use_case = AddExpense(repository)
    add_expense_page = AddExpensePage(add_expense_use_case)

    # Configure the page colors
    page.bgcolor = AppColors.LIGHT_GRAY.value  # Cinza Claro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # Initialize with the add expenses page
    add_expense_view = add_expense_page.create_page()
    page.add(add_expense_view)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)