from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import readonly


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True)
    ref=fields.Char(readonly=1,default='New')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    parent=fields.Char(string='Parent Patient')

    marital_status = fields.Selection([('married','Married'),('single','Single')], string='Marital Status')

    partner_name=fields.Char(string='Partner Name')

    note = fields.Text(string='Notes')

    date_of_birth = fields.Date(string='Date of Birth')

    doctor_id=fields.Many2one('res.users','Doctor')

    responsible_id = fields.Many2one('res.partner', string='Responsible Person')

    appointment_date = fields.Datetime(string='Appointment Date')
    image = fields.Image(string='Patient Image')
    is_discharged = fields.Boolean(string='Discharged', default=False)
    age=fields.Integer(string='Age',compute='_compute_age',inverse='_inverse_age')
    active = fields.Boolean(string='Active', default=True)
    tag_ids=fields.Many2many('hospital.tag')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    appointment_ids=fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    patient_count = fields.Integer(string="Patient Count", compute="_compute_patient_count")
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High')
    ], default='0')

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        if self.date_of_birth and self.date_of_birth > fields.Date.today():
            raise ValidationError('Date of Birth cannot be greater than today')


    # compute patient count______________________
    @api.depends('appointment_ids')
    def _compute_patient_count(self):
        for rec in self:
            rec.patient_count=self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
    #add sequence _____________________________

    @api.model
    def create(self, vals):
        res = super().create(vals)
        self.env['hospital.tag'].search([('name', '=', 'VIP')]).unlink()
        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code('patient_seq')
        return res
    # compute age _______________________________
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = fields.Date.today()
                rec.age = relativedelta(today, rec.date_of_birth).years
            else:
                rec.age = 0

    def _inverse_age(self):
        for rec in self:
            if rec.age:
                rec.date_of_birth = fields.Date.today() - relativedelta(years=rec.age)


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

    def click_test(self):
        print("click")








