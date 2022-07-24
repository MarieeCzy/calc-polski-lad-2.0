import os
import functions as func
import tkinter as tk

#win = tk.Tk()
gross_salary = input("Enter gross salary...\n")
gross_salary = float(gross_salary)

pension_ins = (func.pension_ins_calc(gross_salary))
disability_ins = func.disability_ins_calc(gross_salary)
med_ins = func.med_ins_calc(gross_salary)

social_total = func.social_total(pension_ins, disability_ins, med_ins)

basis_health_insurance_contribution = func.basis_health_insurance_contr(gross_salary, social_total)

print('GROSS SALARY:', gross_salary, 
      '\nPENSION INSURANCE:', pension_ins, 
      '\nDISABILITY INSURANCE:', disability_ins,
      '\nMEDICAL INSURANCE:', med_ins,
      '\nSOCIAL SOCIETY CONTRIBUTIONS:', social_total,
      '\nBASIS HEALTH INSURANCE CONTRIBUTION', basis_health_insurance_contribution)

#win.mainloop()

