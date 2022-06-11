from odoo import api, models, fields

class Accounts(models.Model):
    _name = "transfer.account"
    _description = "transfer accounts"

    email = fields.Char(String = "Email")
    password = fields.Char(String = "Password")
    account_type = fields.Selection([("candidat", "Candidat"), ("agent", "Agent")], String = "Type")