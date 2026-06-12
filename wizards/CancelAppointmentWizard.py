from typing import Sequence

from odoo import models, fields, api
from odoo.orm.types import ValuesType


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    reason = fields.Text(string="Cancel Reason", required=True)
    appointment_id = fields.Many2one('hospital.appointment')

    @api.model
    def default_get(self, fields):
        res=super(CancelAppointmentWizard, self).default_get(fields)
        active_id=self.env.context.get('active_id')
        res['appointment_id'] = active_id


        return res

    def confirm_button(self):
        self.ensure_one()

        if self.appointment_id:
            self.appointment_id.state = 'cancel'
            self.appointment_id.notes = (
                    (self.appointment_id.notes or '') +
                    f"\nCancel reason: {self.reason}"
            )
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }