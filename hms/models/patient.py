import re
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class patient(models.Model):
    _name = 'patients.patients'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    age = fields.Integer()
    birthdate = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('o positive', 'O+',),
        ('o negative', 'O-',),
    ])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    states = fields.Selection([
        ('undetermined', 'Undetermined',),
        ('good', 'Good',),
        ('fair', 'Fair',),
        ('serious', 'Serious',),
    ])
    department_id = fields.Many2one('department.department')
    doctor_id = fields.Many2one('doctor.doctor')

    _sql_constraints=[
        ('email_unique_constraint', 'UNIQUE(email)', 'Email is already exists')
    ]
    @api.onchange('birthdate')
    def _onchange_birthday(self):
        if self.birthdate:
            self.age = date.today().year - self.birthdate.year
            return {
                'warning':{
                    'title': 'Alert',
                    'message': 'Age has been Modefied'
                }
            }
    @api.onchange('age')
    def _onchange_pcr(self):
        if self.age < 30:
            self.pcr = True
            return {
                'warning':{
                    'title': 'Alert',
                    'message': 'PCR has changed'
                }
            }

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')