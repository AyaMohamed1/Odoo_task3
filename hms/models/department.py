from odoo import models, fields

class department(models.Model):
    _name = 'department.department'

    name = fields.Char()
    patients = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many('patients.patients', 'department_id')
