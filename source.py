import os
import salary_calc

cost_of_getting_income = 300
tax_relief = 300

def main():
      gross_salary = input("Enter gross salary...\n")
      #name = input('Enter your name...\n')
      gross_salary = float(gross_salary)
      
      calc_case = salary_calc.SalaryCalc(gross_salary)
      calc_case.calculate()
      calc_case.tax_func(cost_of_getting_income, tax_relief)
      calc_case.net_salary_calc()
      
      print('GROSS SALARY:', gross_salary, 
      '\nPENSION INSURANCE:', calc_case.pension_ins, 
      '\nDISABILITY INSURANCE:', calc_case.disability_ins,
      '\nMEDICAL INSURANCE:', calc_case.med_ins,
      '\nSOCIAL SOCIETY CONTRIBUTIONS:', calc_case.social_total,
      '\nBASIS HEALTH INSURANCE CONTRIBUTION', calc_case.basis_health_insurance_contribution,
      '\nHEALTH CARE CONTRIBUTION', round(calc_case.health_care_contr, 2),
      '\nCOST OF GETTING INCOME', cost_of_getting_income,
      '\nTAX RELIEF', tax_relief,
      '\nTAX BASE', calc_case.tax_base,
      '\nINCOME TAX', calc_case.income_tax,
      '\nTAX TO THE TAX OFFICE', round(calc_case.income_tax, 0),
      '\nNET SALARY', round(calc_case.net_salary, 2))
      
main()
