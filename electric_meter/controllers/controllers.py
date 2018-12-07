# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ElectricMeter(http.Controller):
    @http.route('/electric_meter/data/', type='http', auth='public')
    def index(self, **kw):
        elec_current = kw['elec_current']
        elec_voltage = kw['elec_voltage']
        elec_electricity = kw['elec_electricity']
        elec_str = kw['elec_str']
        request.env['electric.meter'].create({'elec_current': elec_current, 'elec_voltage': elec_voltage, 'elec_electricity': elec_electricity, 'elec_str': elec_str})
        return "success"
