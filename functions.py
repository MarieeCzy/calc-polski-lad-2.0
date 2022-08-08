
class Calculator:
    
    @staticmethod
    def pension_ins_calc(gross_salary):
        return round(gross_salary * 0.0976, 2)
    
    @staticmethod
    def disability_ins_calc(gross_salary):
        return round(gross_salary * 0.015, 2)
    
    @staticmethod
    def med_ins_calc(gross_salary):
        return round(gross_salary * 0.0245, 2)
    
    @staticmethod
    def social_total_calc(contr1, contr2, contr3):
        return contr1 + contr2 + contr3
    
    @staticmethod
    def basis_health_insurance_contr(gross_salary, social_total):
        return gross_salary - social_total
    
    @staticmethod
    def tax_base_calc(gross_salary, *args):
        return (gross_salary - sum(args))
    
