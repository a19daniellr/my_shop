from odoo import models, fields, api
from odoo.exceptions import ValidationError


class VideogameCreator(models.Model):
    _name = 'shop.videogame.creator'

    name = fields.Char('Creator')
    country = fields.Char('Country')
    date_born = fields.Date('Date born')
    date_dead = fields.Date('Date dead')