# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import werkzeug
from openerp import http
from openerp.addons.website_sale.controllers.main import website_sale
from openerp.exceptions import UserError
from openerp.http import request
from openerp.tools.translate import _


class WebsiteSale(website_sale):

    @http.route()
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):        
        ProductProduct = request.env['product.product']
        product = ProductProduct.browse(int(product_id))
        check_not_availability = product.check_product_not_available(
            int(add_qty))
        if check_not_availability:
            values = {
                'title': _('Product not available'),
                'message': check_not_availability,
            }
            return request.website.render(
                "website_sale_product_stock.product_not_available", values)
        else:
            return super(WebsiteSale, self).cart_update(
                product_id, add_qty, set_qty, **kw)
