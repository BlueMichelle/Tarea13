from odoo import fields, models

class ModeloParent(models.Model):
    _name = "modelo.parent"
    _description = "Modelo Parent"
    _rec_name = "campo1"

    campo1 = fields.Char(string="Campo 1")
