##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class MrpProductProduce(models.TransientModel):

    _inherit = 'mrp.product.produce'

    @api.constrains('produce_line_ids')
    def validate_quantity(self):
        location_id = self._context.get('location_src', False)
        location = self.env['stock.location'].browse(location_id)
        for produce_line in self.produce_line_ids:
            if location_id and produce_line.lot_id:
                produce_line.lot_id.validate_lot_quantity(
                    produce_line.qty_done,
                    produce_line.move_id.reserved_availability,
                    location)
