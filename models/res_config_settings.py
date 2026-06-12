from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    consultation_fee = fields.Float(
        string="Default Consultation Fee",
        config_parameter='hospital.default_fee'
    )
    enable_patient_approval = fields.Boolean(
        string="Enable Patient Approval",
        config_parameter='hospital.enable_patient_approval'
    )
