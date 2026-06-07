from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    name = fields.Char(string="Appointment Reference", required=True, default="New")

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    appointment_date = fields.Datetime(string="Appointment Date", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status")

    notes = fields.Text(string="Notes")


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'