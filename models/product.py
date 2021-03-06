# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models
from openerp.tools.translate import _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def check_product_not_available(self, product_qty):
        """Checks availability from a product in stock, returns a warning
        message if the product has no availaility"""

        self.ensure_one()

        if self.type == 'product':
            if product_qty > (self.sudo().qty_available -
                              self.sudo().outgoing_qty):

                qty_available = self.sudo().qty_available - self.sudo().outgoing_qty

                message = _('No availability for this product')
                return message

        return False
