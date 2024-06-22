from domain.entities import Expense
from domain.repositories import ExpenseRepository

class AddExpense:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def execute(self, date, description, category, amount, payment_method, installments, installment_amount, payment_month, notes):
        expense = Expense(date, description, category, amount, payment_method, installments, installment_amount, payment_month, notes)
        self.repository.add(expense)