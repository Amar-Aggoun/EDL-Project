from odoo import api, models, fields

class Specialiies(models.Model):
    _name = "specialities"
    _description = "specialities available"

    name = fields.Char(String = "Speciality name")
    s_level = fields.Char(String = "Speciality study year")
    university = fields.Char(String = "Speciality university")
    admission_score = fields.Float(String = "Admission score for this year")
    available_positions = fields.Integer(String = "Available positions in a spciality")
    position_availibility = fields.Boolean(String = "Does this speciality accepts transfer students")