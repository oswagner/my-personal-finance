from abc import ABC, abstractmethod

class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense):
        pass

    @abstractmethod
    def get_all(self):
        pass