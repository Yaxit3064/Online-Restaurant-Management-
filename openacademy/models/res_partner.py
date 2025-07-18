from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"



    instructor=fields.Boolean(string="Instructor")
    session_ids=fields.Many2many('session.model',string="Sessions")
