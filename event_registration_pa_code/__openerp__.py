# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Event Registration PA Code",
    "version": "8.0.1.1.0",
    "category": "Custom Module",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Alfredo de la Fuente <alfredodelafuente@avanzosc.es>",
    ],
    "depends": [
        "event_registration_analytic",
        "event_planned_by_sale_line",
    ],
    "data": [
        "views/event_event_view.xml",
        "views/res_partner_view.xml",
    ],
    "installable": True,
}
