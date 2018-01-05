# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields
# from openerp.exceptions import ValidationError


class MrpProduction(models.Model):

    _inherit = "mrp.production"

    date_planned = fields.Datetime(readonly=False)
