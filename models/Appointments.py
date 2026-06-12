from pip._internal.utils._jaraco_text import _

from odoo import models, fields, api
from odoo.exceptions import ValidationError, AccessError
from odoo.orm.decorators import readonly


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'name'

    name= fields.Char(string="Appointment Reference", required=True, default="New",readonly= True)
    age2=fields.Integer(string="Age")
    age22 = fields.Integer(string="Age")
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True,ondelete='restrict')
    doctor_id = fields.Many2one('res.partner', string="Doctor")
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    is_paid = fields.Boolean(string="Paid")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In_consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], default='draft', string="Status")

    notes = fields.Text(string="Notes")
    appointment_phamacy_line_ids = fields.One2many('appointment.phamacy.line','appointment_id')


    #copy_method

    def copy(self, default=None):
       if not default:
           default={}
       if not default.get('name'):
           default['name']=f"{self.name} (copy) "
       return super().copy(default)


    def action_confirm(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'


    def action_cancel(self):
        if self.appointment_date.date() == fields.Date.today() or self.appointment_date.date() < fields.Date.today():
            raise ValidationError(
                'You cannot cancel an appointment scheduled for today.'
            )


        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Cancel Appointment',
            'res_model': 'cancel.appointment.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_appointment_id': self.id,
                'default_reason': "test",
            }
        }

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.name == "New":
            res.name = self.env['ir.sequence'].next_by_code('patient_seq')
        return res

class Appointment_phamacy_line(models.Model):
    _name = 'appointment.phamacy.line'
    _description = 'Appointment Phamacy Line'
    appointment_id = fields.Many2one('hospital.appointment')

    product_id=fields.Many2one('product.product')
    price=fields.Float(string='Price',related='product_id.lst_price',)
    qty=fields.Integer(string='Quantity',default=1)