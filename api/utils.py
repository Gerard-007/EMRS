import random


def generate_id(appointment, value):
    appointment.appointment_id = value
    if appointment.appointment_id in [a.appointment_id for a in appointment.doctor.appointments]:
        appointment.appointment_id = random.randint(000000, 999999)
        generate_id(appointment, appointment.appointment_id)
    return appointment.appointment_id
