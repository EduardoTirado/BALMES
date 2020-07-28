# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    blm_documento = fields.Char(string='Enlace a Documento')


