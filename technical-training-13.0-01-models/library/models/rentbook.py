from odoo import models, api, fields


class book(models.Model):
    _name = 'book.book'

    name = fields.Char(string="name")
    author_ids = fields.Many2many('author.author', string="Author(s)")
    #show customers readonly
    #customer_ids = fields.Many2many('customer.customer', string="Customer(s)")
    customer_ids=fields.One2many('rent.rent', 'customer_id', string="Customers", readonly="True")
#TODO one2many: Danger Because a One2many is a virtual relationship, there must be a Many2one field in the other_model, and its name must be related_field. rly?


class author(models.Model):
    _name = 'author.author'

    name = fields.Char(string="name")


class customer(models.Model):
    _name = 'customer.customer'

    name = fields.Char(string="name")
    #show rented books
    book_ids=fields.Many2many('rent.rent', string="Books rented by customer")

class rent(models.Model):
    _name = "rent.rent"

    customer_id = fields.Many2one('customer.customer', string="Customer")
    book_ids = fields.Many2many('book.book', string="Books rented")
    return_date=fields.Date(string="Return Date")
