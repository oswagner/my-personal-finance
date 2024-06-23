import flet as ft
from datetime import datetime
from use_cases.add_expense import AddExpense
from colors import AppColors
from utils.logger_wrapper import LoggerWrapper

class AddExpensePage:
    def __init__(self, add_expense_use_case: AddExpense, logger: LoggerWrapper):
        self.add_expense_use_case = add_expense_use_case
        self.logger = logger
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.date = None
        self.description = None
        self.category = None
        self.amount = None
        self.payment_method = None
        self.installments = None
        self.installment_amount = None
        self.payment_month = None
        self.notes = None

    def create_page(self):
        self.logger.debug({"event": "create_page", "action": "start"})

        self.date = ft.TextField(
            label="Date", value=self.current_date, hint_text="YYYY-MM-DD",
            expand=True, bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.description = ft.TextField(
            label="Description", expand=True, bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.category = ft.Dropdown(
            label="Category",
            options=[
                ft.dropdown.Option("Food", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Transport", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Entertainment", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Electronics", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Others", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
            ],
            expand=True, bgcolor=AppColors.LIGHT_GRAY.value
        )
        self.amount = ft.TextField(
            label="Amount", keyboard_type=ft.KeyboardType.NUMBER, expand=True,
            bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.payment_method = ft.Dropdown(
            label="Payment Method",
            options=[
                ft.dropdown.Option("Credit Card", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Debit Card", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Cash", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
                ft.dropdown.Option("Other", text_style=ft.TextStyle(color=AppColors.BLUE_GRAY.value)),
            ],
            expand=True, bgcolor=AppColors.LIGHT_GRAY.value
        )
        self.installments = ft.TextField(
            label="Installments", keyboard_type=ft.KeyboardType.NUMBER, expand=True,
            bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.installment_amount = ft.TextField(
            label="Installment Amount", keyboard_type=ft.KeyboardType.NUMBER, expand=True,
            bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.payment_month = ft.TextField(
            label="Payment Month", hint_text="MM/YYYY", expand=True,
            bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        self.notes = ft.TextField(
            label="Notes", expand=True, bgcolor=AppColors.LIGHT_GRAY.value, color=AppColors.BLUE_GRAY.value
        )
        
        add_button = ft.ElevatedButton(
            text="Add Expense", on_click=lambda e: self.add_expense(), expand=True,
            bgcolor=AppColors.BLUE_PASTEL.value, color=AppColors.LIGHT_GRAY.value
        )

        self.logger.debug({"event": "create_page", "action": "end"})

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Expense Tracker", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=AppColors.BLUE_GRAY.value),
                    ft.Divider(),
                    ft.Text("Add New Expense", theme_style=ft.TextThemeStyle.HEADLINE_SMALL, color=AppColors.BLUE_GRAY.value),
                    ft.Row([self.date, self.description]),
                    ft.Row([self.category, self.amount]),
                    ft.Row([self.payment_method, self.installments]),
                    ft.Row([self.installment_amount, self.payment_month]),
                    ft.Row([self.notes]),
                    ft.Row([add_button]),
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START,
                width=800,
                expand=True,
            ),
            padding=20,
            bgcolor=AppColors.LIGHT_GRAY.value,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK)
            )
        )

    def add_expense(self):
        self.logger.info({"event": "add_expense", "action": "start"})
        self.add_expense_use_case.execute(
            self.date.value, self.description.value, self.category.value,
            self.amount.value, self.payment_method.value, self.installments.value,
            self.installment_amount.value, self.payment_month.value, self.notes.value
        )
        self.logger.info({"event": "add_expense", "action": "end"})
        self.reset_fields()

    def reset_fields(self):
        self.logger.debug({"event": "reset_fields", "action": "start"})
        self.date.value = self.current_date
        self.description.value = ""
        self.category.value = ""
        self.amount.value = ""
        self.payment_method.value = ""
        self.installments.value = ""
        self.installment_amount.value = ""
        self.payment_month.value = ""
        self.notes.value = ""
        self.date.update()
        self.description.update()
        self.category.update()
        self.amount.update()
        self.payment_method.update()
        self.installments.update()
        self.installment_amount.update()
        self.payment_month.update()
        self.notes.update()
        self.logger.debug({"event": "reset_fields", "action": "end"})