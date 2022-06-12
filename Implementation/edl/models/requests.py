from odoo import fields, models, api

class Requests(models.Model):
    _name = "requests"
    _description = "Requests list"

    request_type = fields.Selection([("transfer", "Transfer"), ("inscription", "Inscription")], String ="Type of the request")
    candidat_id = fields.Integer(String = "Candidat ID")
    current_speciality = fields.Integer(String = "Current speciality")
    wanted_speciality = fields.Integer(String = "Wanted speciality")