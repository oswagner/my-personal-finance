from domain.repositories import ExpenseRepository

class GetExpenses:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()