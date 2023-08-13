# -*- coding: utf-8 -*-
# from odoo import http


# class Cashierr(http.Controller):
#     @http.route('/cashierr/cashierr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cashierr/cashierr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cashierr.listing', {
#             'root': '/cashierr/cashierr',
#             'objects': http.request.env['cashierr.cashierr'].search([]),
#         })

#     @http.route('/cashierr/cashierr/objects/<model("cashierr.cashierr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cashierr.object', {
#             'object': obj
#         })
