# -*- coding: utf-8 -*-

from odoo import models, fields, api

class electric_meter(models.Model):
    _name = 'electric.meter'

    name = fields.Char()
    elec_current = fields.Integer(default=0, string='电流')
    elec_voltage = fields.Integer(default=0, string='电压')
    elec_electricity = fields.Integer(default=0, string='电量')
