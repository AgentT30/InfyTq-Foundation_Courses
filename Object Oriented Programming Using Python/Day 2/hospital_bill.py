class Bill:

    def __init__(self, bill_id, patient_name):
        self.bill_id = bill_id
        self.patient_name = patient_name
        self.bill_amount = None

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total = 0
        for i in range(len(quantity_list)):
            total += quantity_list[i] * price_list[i]
        self.bill_amount = total + consultation_fees

    def get_bill_id(self):
        return self.bill_id

    def get_patient_name(self):
        return self.patient_name

    def get_bill_amount(self):
        return self.bill_amount
