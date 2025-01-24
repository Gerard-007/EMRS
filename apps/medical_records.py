import datetime


class MedicalRecord:
    def __init__(self, patient, doctor, diagnosis, medications, notes, date):
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.medications = medications
        self.notes = notes
        self.date = date or datetime.date.today()

    def update_medical_record(self, diagnosis, medications, notes):
        if diagnosis:
            self.diagnosis = diagnosis
        if medications:
            self.medications = medications
        if notes:
            self.notes = notes

    def __str__(self):
        medications_str = ", ".join(self.medications) if self.medications else "None"
        return (f"""
        Medical Record for {self.patient.first_name} {self.patient.last_name}
        Doctor: {self.doctor.first_name} {self.doctor.last_name}
        Date: {self.date}
        Diagnosis: {self.diagnosis}
        Medications: {medications_str}
        Notes: {self.notes}""")
