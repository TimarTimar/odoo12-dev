from odoo import models, api, fields


class book(models.Model):
    _name = 'book.book'

    name = fields.Char(string="Book's name")
    author_ids = fields.Many2many('book.author', string="Author(s)")
    # show customers readonly
    # customer_ids = fields.Many2many('customer.customer', string="Customer(s)")
    # book_id = fields.Many2one('rent.rent', readonly=True)
    rent_ids = fields.Many2many('rent.rent', string='Rents', readonly=True)
    publisher_id = fields.Many2one('book.publisher')


class publisher(models.Model):
    _name = 'book.publisher'
    name = fields.Char(string="Publisher name")


# TODO one2many: Danger Because a One2many is a virtual relationship, there must be a Many2one field in the other_model, and its name must be related_field. rly?


class author(models.Model):
    _name = 'book.author'

    name = fields.Char(string="name")


class customer(models.Model):
    _name = 'customer.customer'

    name = fields.Char(string="name")
    phone_number = fields.Char()
    email = fields.Char()
    # show rented books
    customer_ids = fields.One2many('rent.rent', 'customer_id', string="Customers", readonly="True")


class rent(models.Model):
    _name = "rent.rent"
    customer_id = fields.Many2one('customer.customer', string="Customer", required=True)
    book_ids = fields.Many2many('book.book', string="Books rented")
    return_date = fields.Date(string="Return Date")
    customer_phone_number = fields.Char(compute='_phone_number')
    customer_email = fields.Char(compute='_email')

    # TODO try with many2many fields or with onchange and loop
    # book_publishers = fields.Many2many(compute='_list_publishers')
    book_publishers = fields.Many2many('book.book', related='book_ids')

    @api.depends('customer_id')
    def _phone_number(self):
        self.customer_phone_number = self.customer_id.phone_number

    @api.depends('customer_id')
    def _email(self):
        self.customer_email = self.customer_id.email

    # Expected singleton. I could try to solve this with domain sql/python or maybe with api.multi
    @api.depends('book_ids')
    def _list_publishers(self):
        for record in self:
            # record.book_publishers=record.book_ids.publisher_id.name
            pass
