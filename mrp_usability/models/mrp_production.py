##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields
# from odoo.exceptions import ValidationError


class MrpProduction(models.Model):

    _inherit = "mrp.production"

    date_planned = fields.Datetime(readonly=False)
