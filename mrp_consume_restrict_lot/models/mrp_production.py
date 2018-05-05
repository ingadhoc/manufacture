##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class MrpProductProduce(models.TransientModel):

    _inherit = 'mrp.product.produce'

    @api.multi
    @api.constrains('consume_lines')
    def validate_quantity(self):
        for rec in self:
            for line in rec.consume_lines:
                location_id = self._context.get('location_src', False)
                if location_id and line.lot_id:
                    line.lot_id.validate_lot_quantity(
                        line.product_qty, [
                            ('location_id', '=', location_id),
                            ('reservation_id', '=', False)])
