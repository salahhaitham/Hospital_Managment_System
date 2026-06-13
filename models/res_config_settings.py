from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    cancel_day = fields.Integer(
        string="Cancel Days",
        config_parameter='hospital.cancel_day'
    )
