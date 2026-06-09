from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    note = fields.Text(string='Notes')
    date_of_birth = fields.Date(string='Date of Birth')
    doctor_id=fields.Many2one('res.users','Doctor')
    responsible_id = fields.Many2one('res.partner', string='Responsible Person')
    appointment_date = fields.Datetime(string='Appointment Date')
    image = fields.Image(string='Patient Image')
    is_discharged = fields.Boolean(string='Discharged', default=False)
    age=fields.Integer(string='Age',compute='_compute_age')
    active = fields.Boolean(string='Active', default=True)
    tag_ids=fields.Many2many('hospital.tag')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High')
    ], default='0')
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Patient name must be unique!'),
    ]

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = fields.Date.today()
                rec.age = relativedelta(today, rec.date_of_birth).years
            else:
                rec.age = 0

    def confirm_button(self):
        for rec in self:
            rec.state = 'confirm'

    def done_button(self):
        for rec in self:
            rec.state = 'done'

    def draft_button(self):
        for rec in self:
            rec.state = 'draft'

    def cancel_button(self):
        for rec in self:
            rec.state = 'cancel'








