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
    session_date = fields.Datetime(string="Starts from")
    room_size = fields.Integer()

    @api.onchange('room_size', 'student_ids')
    def _verify_valid_seats(self):
        if self.room_size < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats must be >=0",
                },
            }
        if self.room_size < len(self.student_ids):
            return {
                'warning': {
                    'title': "Room is full",
                    'message': "Increase room_size or remove participants",
                },
            }




