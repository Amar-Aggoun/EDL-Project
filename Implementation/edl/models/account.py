from odoo import api, models, fields

class CandidatAccounts(models.Model):
    _name = "candidat.accounts"
    _description = "transfer accounts"

    email = fields.Char(String = "Email")
    password = fields.Char(String = "Password")
    account_type = fields.Selection([("candidat", "Candidat"), ("agent", "Agent")], String = "Type")