import flet as ft
from use_cases.get_expenses import GetExpenses

class ViewExpensesPage:
    def __init__(self, get_expenses_use_case: GetExpenses):
        self.get_expenses_use_case = get_expenses_use_case

    def create_table(self):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Date")),
                ft.DataColumn(ft.Text("Description")),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Amount")),
                ft.DataColumn(ft.Text("Payment Method")),
                ft.DataColumn(ft.Text("Installments")),
                ft.DataColumn(ft.Text("Installment Amount")),
                ft.DataColumn(ft.Text("Payment Month")),
                ft.DataColumn(ft.Text("Notes")),
            ],
            rows=[]
        )

    def create_page(self):
        table = self.create_table()
        expenses = self.get_expenses_use_case.execute()
        for expense in expenses:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(expense.date)),
                        ft.DataCell(ft.Text(expense.description)),
                        ft.DataCell(ft.Text(expense.category)),
                        ft.DataCell(ft.Text(expense.amount)),
                        ft.DataCell(ft.Text(expense.payment_method)),
                        ft.DataCell(ft.Text(expense.installments)),
                        ft.DataCell(ft.Text(expense.installment_amount)),
                        ft.DataCell(ft.Text(expense.payment_month)),
                        ft.DataCell(ft.Text(expense.notes)),
                    ]
                )
            )
        table.update()

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Recorded Expenses", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.Divider(),
                    table,
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START,
                width=800,
                expand=True,
            ),
            padding=20,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=ft.BorderRadius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK)
            )
        )