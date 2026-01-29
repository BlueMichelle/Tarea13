from odoo import fields, models

class ModeloExtensor(models.Model):
    _inherit = "modelo.parent"

    campo1 = fields.Char(string="Nuevo Campo 1")
    campo2 = fields.Char(string="Campo 2")
