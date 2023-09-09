class RoiCalculator:
    def propertyIncome(self):
        rental_income = int(input('what the rental monthly income of your property? '))
        return rental_income

    def propertyExpenses(self):
        tax = input('whats your monthly property tax ?')
        insurance = input('whats your monthly insuranse? ')
        repairs = input ('whats you monthly repai saving? ')
        expenses = int(tax) + int(insurance) + int(repairs)
        return expenses


    def cashFlow(self):
        rental_income = int(input('what the rental monthly income of your property? '))
        tax = input('whats your monthly property tax ?')
        insurance = input('whats your monthly insuranse? ')
        repairs = input ('whats you monthly repai saving? ')
        expenses = int(tax) + int(insurance) + int(repairs)
        cashflow = rental_income - expenses
        return cashflow


    def CashOnCash (self):
        downpayment = int(input('how much downpayment you put for the house? '))
        closing = int(input('what was your closing cost? '))
        totalcost= downpayment + closing
        rental_income = int(input('what the rental monthly income of your property? '))
        tax = input('whats your monthly property tax ?')
        insurance = input('whats your monthly insuranse? ')
        repairs = input ('whats you monthly repai saving? ')
        expenses = int(tax) + int(insurance) + int(repairs)
        cashflow_monthly = rental_income - expenses
        cashflow_yearly = cashflow_monthly * 12
        roi = (cashflow_yearly / totalcost) * 100
        return f'your ROI and cash on cash return is {roi} % '

# milad = RoiCalculator()
# # print(milad.propertyIncome())
# # print(milad.propertyExpenses())
# # print(milad.cashFlow())
# print(milad.CashOnCash())


