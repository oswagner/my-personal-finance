import flet as ft
from data.expense_repository import InMemoryExpenseRepository
from use_cases.add_expense import AddExpense
from presentation.add_expense_page import AddExpensePage

def main(page: ft.Page):
    repository = InMemoryExpenseRepository()
    add_expense_use_case = AddExpense(repository)
    add_expense_page = AddExpensePage(add_expense_use_case).create_page()
    

    # Initialize with the add expenses page
    page.add(add_expense_page)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)