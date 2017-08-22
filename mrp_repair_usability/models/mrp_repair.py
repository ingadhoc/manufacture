# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api, _
from openerp.exceptions import ValidationError


class MrpRepair(models.Model):

    _inherit = "mrp.repair"

    @api.multi
    def action_invoice_create(self, group=False):
        for repair in self:
            if repair.state != '2binvoiced':
                raise ValidationError(
                    _('You can not create the invoice for '
                      'a reparation order "%s" that is not'
                      ' in "To be Invoiced" state!') % (repair.name))
        return super(MrpRepair, self).action_invoice_create(group=group)
