# -*- coding: utf-8 -*-
from openerp import models, fields, api


class BookCategory(models.Model):
    _name = 'library.book.category'
    name = fields.Char('Category')
    parent_id = fields.Many2one(
        comodel_name="library.book.category",
        string="Parent Category",
        ondelete='restrict',
        index=True)
    child_ids = fields.One2many(
        comodel_name="library.book.category",
        inverse_name="parent_id",
        string="Child Categories")
    _parent_store = True
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! You cannot create recuisive categories.'
            )