import functions as func

class SalaryCalc:
      def __init__(self, gross_salary):
            self.gross_salary = gross_salary
            self.pension_ins = 0
            self.disability_ins = 0
            self.med_ins = 0
            self.social_total = 0
            
            
      def calculate(self):
            self.pension_ins = func.Calculator.pension_ins_calc(self.gross_salary)
            self.disability_ins = func.Calculator.disability_ins_calc(self.gross_salary)
            self.med_ins = func.Calculator.med_ins_calc(self.gross_salary)
            
      def total(self):
            self.social_total = func.Calculator.social_total_calc(self.pension_ins, self.disability_ins, self.med_ins)
            self.basis_health_insurance_contribution = func.Calculator.basis_health_insurance_contr(self.gross_salary, self.social_total)
            