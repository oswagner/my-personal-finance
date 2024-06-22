from domain.entities import Expense
from domain.repositories import ExpenseRepository

class InMemoryExpenseRepository(ExpenseRepository):
    def __init__(self):
        self.expenses = []

    def add(self, expense: Expense):
        self.expenses.append(expense)

    def get_all(self):
        return self.expenses