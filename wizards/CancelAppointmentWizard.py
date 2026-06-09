from odoo import models, fields

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    reason = fields.Text(string="Cancel Reason", required=True)
    appointment_id = fields.Many2one('hospital.appointment')

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