from odoo import api, models, fields

class CandidatInfo(models.Model):
    _name = "candidat.info"
    _description = "candidat information"

    first_name = fields.Char(String = "Email")
    last_name = fields.Char(String = "Password")
    birth_date = fields.Date(String = "Birth date")
    bac_year = fields.Integer(String ="Bac year")
    bac_n = fields.Char(String = "")
    phone_number = fields.Char(String = "phone number")
    wilaya = fields.Char(String = "wilaya")
    study_years = fields.Integer(String = "Study years")
    catch_up_times = fields.Integer(String = "")
    exception_year = fields.Boolean(String = "Exception year")
    wanted_speciality = fields.Char(String = "wanted speciality")
    s1_score = fields.Float(Strin = "first semester score")
    s2_score = fields.Float(Strin = "second semester score")
    s3_score = fields.Float(Strin = "third semester score")
    s4_score = fields.Float(Strin = "fourth semester score")
    s5_score = fields.Float(Strin = "fifth semester score")
    s6_score = fields.Float(Strin = "sixth semester score")