# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, exceptions, _


class WizEventAppendAssistant(models.TransientModel):
    _inherit = 'wiz.event.append.assistant'

    def _create_account_for_not_employee_from_wizard(
            self, event, registration):
        account_obj = self.env['account.analytic.account']
        analytic_invoice_line_obj = self.env['account.analytic.invoice.line']
        if event.sale_order.payer == 'school':
            super(WizEventAppendAssistant,
                  self)._create_account_for_not_employee_from_wizard(
                event, registration)
        else:
            vals = self._prepare_data_for_account_not_employee(event,
                                                               registration)
            new_account = account_obj.create(vals)
            registration.analytic_account = new_account.id
            lines = event.event_ticket_ids.filtered(
                lambda x: x.is_pa_partner ==
                registration.partner_id.commercial_partner_id.is_pa_partner)
            if not lines:
                raise exceptions.Warning(
                    _('Ticket not found for %s') %
                    (registration.partner_id.name))
            line_vals = {'analytic_account_id': new_account.id,
                         'name': (lines[0].sale_line.name or
                                  lines[0].product_id.name),
                         'price_unit': lines[0].price,
                         'price_subtotal': lines[0].sale_line.price_subtotal,
                         'product_id': lines[0].product_id.id,
                         'quantity': lines[0].sale_line.product_uom_qty,
                         'uom_id': (lines[0].sale_line.product_uom.id or
                                    lines[0].product_id.uom_id.id)}
            analytic_invoice_line_obj.create(line_vals)
