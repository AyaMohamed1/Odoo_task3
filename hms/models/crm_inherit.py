from odoo import models, fields

class CrmInherit(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Char()