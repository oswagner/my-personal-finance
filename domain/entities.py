class Expense:
    def __init__(self, date, description, category, amount, payment_method, installments, installment_amount, payment_month, notes):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount
        self.payment_method = payment_method
        self.installments = installments
        self.installment_amount = installment_amount
        self.payment_month = payment_month
        self.notes = notes