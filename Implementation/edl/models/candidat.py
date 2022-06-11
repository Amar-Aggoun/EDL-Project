from odoo import api, models, fields

class CandidatInfo(models.Model):
    _name = "candidat.info"
    _description = "candidat information"

    first_name = fields.Char(String = "Email")
    last_name = fields.Char(String = "Password")
    birth_date = fields.date(String = "Birthday")
    bac_date = fields.date(String = "Bac year")
    bac_n = fields.Char(String = "")
    phone_number = fields.Char(String = "phone number")
    wilaya = fields.Char(String = "wilaya")
    study_years = fields.Integer(String = "Study years")
    catch_up_times = fields.Integer(String = "")
    exception_year = fields.boolean(String = "Exception year")
    wanted_speciality = fields.Char(String = "wanted speciality")
    s1_score = fields.float(Strin = "first semester score")
    s2_score = fields.float(Strin = "second semester score")
    s3_score = fields.float(Strin = "third semester score")
    s4_score = fields.float(Strin = "fourth semester score")
    s5_score = fields.float(Strin = "fifth semester score")
    s6_score = fields.float(Strin = "sixth semester score")