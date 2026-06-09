from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    name = fields.Char(string="Appointment Reference", required=True, default="New")

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('res.partner', string="Doctor")
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    is_paid = fields.Boolean(string="Paid")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status")

    notes = fields.Text(string="Notes")
    appointment_phamacy_line_ids = fields.One2many('appointment.phamacy.line','appointment_id')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'


class Appointment_phamacy_line(models.Model):
    _name = 'appointment.phamacy.line'
    _description = 'Appointment Phamacy Line'
    appointment_id = fields.Many2one('hospital.appointment')

    product_id=fields.Many2one('product.product')
    price=fields.Float(string='Price',related='product_id.lst_price',)
    qty=fields.Integer(string='Quantity',default=1)