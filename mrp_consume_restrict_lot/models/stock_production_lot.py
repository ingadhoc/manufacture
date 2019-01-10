from odoo import models, api, _
from odoo.exceptions import UserError
from odoo.tools import float_compare


class StockProductionlot(models.Model):

    _inherit = 'stock.production.lot'

    @api.multi
    def validate_lot_quantity(self, quantity, reserved_qty, location):
        self.ensure_one()
        precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure')
        qty = self.env['stock.quant']._get_available_quantity(
            self.product_id, location, lot_id=self)
        real_qty = qty + reserved_qty
        if float_compare(real_qty, quantity, precision_rounding=precision) < 0:
            raise UserError(_(
                'Sending amount can not exceed the quantity in '
                'stock for this product in the lot.\n'
                '* Product: %s\n'
                '* Lot: %s\n'
                '* Stock: %s') % (
                    self.product_id.name, self.name, real_qty))
