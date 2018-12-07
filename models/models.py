# -*- coding: utf-8 -*-

from odoo import models, fields, api

class electric_meter(models.Model):
    _name = 'electric.meter'

    name = fields.Char()
    elec_id = fields.Integer(string='编号')
    elec_current = fields.Float(default=0, string='电流')
    elec_voltage = fields.Float(default=0, string='电压')
    elec_electricity = fields.Float(default=0, string='电量')
    elec_date = fields.Datetime()
    elec_str = fields.Char(string='日期')


