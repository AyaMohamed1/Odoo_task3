from odoo import models, fields

class doctor(models.Model):
    _name = 'doctor.doctor'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()
    patient_ids = fields.One2many('patients.patients', 'doctor_id')