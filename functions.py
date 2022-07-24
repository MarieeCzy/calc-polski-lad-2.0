
def pension_ins_calc(gross_salary):
    return round(gross_salary * 0.0976, 2)
    
def disability_ins_calc(gross_salary):
    return round(gross_salary * 0.015, 2)
   
def med_ins_calc(gross_salary):
    return round(gross_salary * 0.0245, 2)
    
def social_total(contr1, contr2, contr3):
    return contr1 + contr2 + contr3
    
def basis_health_insurance_contr(gross_salary, social_total):
    return gross_salary - social_total
