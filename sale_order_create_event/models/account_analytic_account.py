# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields, api


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    sale = fields.Many2one('sale.order', string='Sale order')

    @api.multi
    def write(self, vals):
        if (self.env.context.get('without_sale_name', False) and
                vals.get('name', False)):
            vals.pop('name')
        return super(AccountAnalyticAccount, self).write(vals)
