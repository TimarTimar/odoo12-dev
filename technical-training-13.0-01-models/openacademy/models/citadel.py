from odoo import models, api, fields


class Classes(models.Model):
    _name = 'classes.classes'

    name = fields.Char(string="name")
    level = fields.Integer(string="level")
    is_active = fields.Boolean(string="active")


class Maesters(models.Model):
    _name = 'maesters.maesters'

    name = fields.Char(string="name")
    # m_session_id = fields.Many2One(sessions.sessions)


class Students(models.Model):
    _name = 'students.students'

    name = fields.Char(string="name")

    session_id = fields.Many2one('sessions.sessions')
    # related_field=fields.Char()


class Sessions(models.Model):
    _name = 'sessions.sessions'
    # TODO add selection field
    student_ids = fields.Many2many('students.students', string="Participants")
    maesters_id = fields.Many2one('maesters.maesters', string="Teacher")
    classes_id = fields.Many2one('classes.classes', ondelete='cascade', string="Class")

    # students_session_ids=fields.One2Many(students.students, session_id, string="Students/Participants")
    # participants=fields.One2Many(students.students, students.students.related_field)

    # maesters_session_ids = fields.One2Many(maesters.maesters, m_session_id, string="Maesters/Teachers")
