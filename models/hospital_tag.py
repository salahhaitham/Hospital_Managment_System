from odoo import models, fields

class HospitalTag(models.Model):
    _name = 'hospital.tag'
    _description = 'Hospital Tag'
    _rec_name = 'name'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color')
    active = fields.Boolean(default=True)

