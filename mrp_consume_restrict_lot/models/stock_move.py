##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class StockMoveConsume(models.TransientModel):

    _inherit = 'stock.move.consume'

    @api.multi
    @api.constrains('restrict_lot_id')
    def validate_quantity(self):
        for rec in self:
            if rec.restrict_lot_id and rec.location_id:
                rec.restrict_lot_id.validate_lot_quantity(
                    rec.product_qty, [
                        ('location_id', '=', rec.location_id.id),
                        ('reservation_id', '=', False)])
