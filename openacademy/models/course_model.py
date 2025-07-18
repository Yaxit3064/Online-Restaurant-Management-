from odoo import models
from odoo import fields, api

class CourseModel(models.Model):
    _name = 'course.model'
    _description = "All Academic Courses"
    _rec_name = "title"


    title=fields.Char(string="Course Name",required=True)
    user=fields.Many2one('res.users',string="Users")
    responsible_id = fields.Many2one('res.users', string='Responsible')
    description=fields.Text(string="Description")
    additional_information=fields.Text(string="Additional Information")
    session_ids=fields.One2many('session.model','course_id', string="Sessions")

    _sql_constraints = [
        ('check_title_description', 'CHECK(title != description)',
         'the title and description can not match'),
        ('unique_title', 'UNIQUE(title)', 'This course is already listed'),
    ]

    def copy(self, default=None):
        if default is None:
            default={}
        if not default.get('title'):
            default['title'] = f"Copy of {self.title}"
        return super(CourseModel,self).copy(default)