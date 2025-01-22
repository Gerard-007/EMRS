import json
from http.server import BaseHTTPRequestHandler
from api.patient import Patient


class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    # def do_POST(self):
    #     # Parse incoming JSON payload
    #     content_length = int(self.headers['Content-Length'])
    #     post_data = self.rfile.read(content_length)
    #     payload = json.loads(post_data)

    #     # Route based on the path
    #     if self.path == '/patients/register':
    #         self.register_patient(payload)
    #     elif self.path == '/appointments/book':
    #         self.book_appointment(payload)
    #     else:
    #         self._send_response(404, {"error": "Endpoint not found"})

    # def do_GET(self):
    #     if self.path.startswith('/patients/'):
    #         patient_id = int(self.path.split('/')[-1])
    #         self.get_medical_records(patient_id)
    #     else:
    #         self._send_response(404, {"error": "Endpoint not found"})

    # def register_patient(self, payload):
    #     patient = Patient(
    #         first_name=payload['first_name'],
    #         last_name=payload['last_name'],
    #         dob=payload['dob'],
    #         address=payload['address'],
    #         phone=payload['phone'],
    #         email=payload['email']
    #     )
    #     patients.append(patient)
    #     self._send_response(200, {"message": f"Patient {patient.first_name} registered successfully."})

    # def book_appointment(self, payload):
    #     appointment = {
    #         "id": len(appointments) + 1,
    #         "date": payload['date'],
    #         "time": payload['time'],
    #         "doctor_id": payload['doctor_id'],
    #         "patient_id": payload['patient_id'],
    #         "details": payload.get('details', '')
    #     }
    #     appointments.append(appointment)
    #     self._send_response(200, {"message": f"Appointment booked for patient ID {payload['patient_id']}."})

    # def get_medical_records(self, patient_id):
    #     # For simplicity, return a dummy medical record
    #     record = {
    #         "patient_id": patient_id,
    #         "records": [
    #             {"diagnosis": "Flu", "medications": ["Paracetamol"], "notes": "Recovering well", "date": "2025-01-20"}
    #         ]
    #     }
    #     self._send_response(200, record)
