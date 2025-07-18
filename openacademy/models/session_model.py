from odoo import models, fields, api
from datetime import date

from odoo.addons.web_editor.models.ir_qweb_fields import Duration
from odoo.exceptions import ValidationError


class SessionModel(models.Model):
    _name = 'session.model'
    _description = "Courses Session"

    name = fields.Char(string="Session On", required=True)
    course_id = fields.Many2one('course.model', string="Course")
    instructor = fields.Many2one('res.partner', string="Instructor",
                                 domain="[('instructor','=',True), '|', ('category_id.name','=','Teacher / Level 1'), ('category_id.name','=','Teacher / Level 2')]")
    start_date = fields.Date(string="Start Date", default=date.today())
    end_date = fields.Date(string="End Date")
    active = fields.Boolean(string="Active", default=True)

    duration_id = fields.Integer(string="Duration", compute="_compute_duration_cal")
    seats = fields.Integer(string="Total Seats")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats_percent = fields.Float(string="Taken Seats (%)", compute="_compute_taken_seats_percent", store=True)


    @api.depends('end_date')
    def _compute_duration_cal(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.duration_id= (rec.end_date - rec.start_date).days
            else:
                rec.duration_id=0

    @api.depends('attendee_ids', 'seats')
    def _compute_taken_seats_percent(self):
        for record in self:
            if record.seats:
                record.taken_seats_percent = (100.0 * len(record.attendee_ids)) / record.seats
            else:
                record.taken_seats_percent = 0.0

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0 or self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': 'seats cannot be negative',
                    'message': 'please enter valid seats',
                }
            }

    #
    @api.constrains('instructor', 'attendee_ids')
    def check_instructor_in_attendee(self):
        for rec in self:
            if rec.instructor and rec.instructor in rec.attendee_ids:
                raise ValidationError("Instructor can not be attendee")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'This course is already exists...')
    ]
