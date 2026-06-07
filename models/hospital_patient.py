

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'


    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    note = fields.Text(string='Notes')
    date_of_birth = fields.Date(string='Date of Birth')
    responsible_id = fields.Many2one('res.partner', string='Responsible Person')
    appointment_date = fields.Datetime(string='Appointment Date')
    image = fields.Image(string='Patient Image')
    is_discharged = fields.Boolean(string='Discharged', default=False)

    active = fields.Boolean(string='Active', default=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)


    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Patient name must be unique!'),
    ]
