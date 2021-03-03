# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)


class VideogameShop(models.Model):

    _name = 'shop.videogame'
    _description = 'Shop Videogame'

    name = fields.Char('Name', required=True)
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated', copy=False)
    creators_id = fields.Many2one('shop.videogame.creator', string='Creator')
    genre_id = fields.Many2one('shop.videogame.genre', string='Genre')
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed')],
        'State', default="draft")

     
    is_lent = fields.Boolean('Lent', compute='check_lent', default=False)

    
    loan_ids = fields.One2many('shop.loan', inverse_name='videogame_id')

    videogame_image = fields.Binary('Cover')

    @api.onchange('name')
    def onchange_field_name(self):
        if self.name != False:
            self.env['ir.config_parameter'].set_param('name_videogame', self.name)
        else:
            self.env['ir.config_parameter'].set_param('name_videogame', '')

    @api.multi
    def check_lent(self):
        for videogame in self:    
            domain = ['&',('videogame_id.id', '=', videogame.id), ('date_end', '>=', datetime.now())]
            videogame.is_lent = self.env['shop.loan'].search(domain, count=True) > 0
            
            self.env['ir.config_parameter'].set_param('name_videogame', videogame.name)

            if videogame.state == 'borrowed' and not videogame.is_lent:
                videogame.is_lent = True
            elif videogame.state == 'available' and videogame.is_lent:
                videogame.is_lent = False    

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed','draft'),
                   ('available','draft'),
                   ('borrowed', 'available')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for videogame in self:
            domain = ['&',('videogame_id.id', '=', videogame.id), ('date_end', '>=', datetime.now())]
            if not videogame.is_lent and videogame.state == 'available' and new_state == 'borrowed':
                videogame.is_lent = True

            if self.env['shop.loan'].search(domain, count = True) > 0:
                if videogame.is_lent and videogame.state == 'borrowed':
                    raise models.ValidationError('Videogame is borrowed !')

            if videogame.is_allowed_transition(videogame.state, new_state):
                videogame.state = new_state
            else:
                message = _('Moving from %s to %s is not allowed !') % (videogame.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_draft(self):
        self.change_state('draft')

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(VideogameShop, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        self.create_genre()
        self.create_creators()
        return res

    def create_creators(self):
        if not self.env['shop.videogame.creator'].search(([])):
            creator1 = {
                'name' : 'Tom Hall',
                'country' : 'United States',
                'date_born' : '09/02/1964'
            }
            creator2 = {
                'name' : 'John Romero',
                'country' : 'United States',
                'date_born' : '10/28/1967'
            }
            creator3 = {
                'name' : 'Yū Suzuki',
                'country' : 'Japan',
                'date_born' : '06/10/1958'
            }
            creator4 = {
                'name' : 'Peter Molyneux',
                'country' : 'England',
                'date_born' : '05/05/1959'
            }
            creator5 = {
                'name' : 'Paco Menéndez',
                'country' : 'Spain',
                'date_born' : '07/04/1965',
                'date_dead' : '10/08/1999'
            }

            record = self.env['shop.videogame.creator'].create(creator1)
            record = self.env['shop.videogame.creator'].create(creator2)
            record = self.env['shop.videogame.creator'].create(creator3)
            record = self.env['shop.videogame.creator'].create(creator4)
            record = self.env['shop.videogame.creator'].create(creator5)

            return True

    def create_genre(self):
        if not self.env['shop.videogame.genre'].search(([])):
            genre1 = {
                'name': 'One vs One',
                'description': 'Fight with another one or against a CPU'
            }
            genre2 = {
                'name': 'Arena fighting',
                'description': 'Battle royal, Fighting with everyone, free on stage, high interaction with the stage, various usable objects spread out on the stage'
            }
            parent_genre_val = {
                'name': 'Fighting videogame',
                'description': 'Managing a fighter or a group of them, either by hitting, using magical power, weapons...',
                'child_ids': [
                    (0, 0, genre1),
                    (0, 0, genre2),
                ]
            }
            
            genre3 = {
                'name': 'Simulation',
                'description': 'Is (generally) more realistic than the other sports videogames'
            }
            genre4 = {
                'name': 'Fantasy Sports',
                'description': 'Fictional sports, like Quidditch (Harry Potter)'
            }
            parent_genre_val2 = {
                'name': 'Sport',
                'description': 'Simulates traditional (or invented) sports field: Basketball, football...',
                'child_ids': [
                    (0, 0, genre3),
                    (0, 0, genre4),
                ]
            }

            genre5 = {
                'name': 'Conversational adventure',
                'description': 'The player plays a protagonist who usually must solve unknows and puzzles with various objects'
            }
            genre6 = {
                'name': 'Survival Horror',
                'description': 'The protagonists live adventures where they must come out of situations typical of a horror movie'
            }
            parent_genre_val3 = {
                'name': 'Adventure',
                'description': 'They are video games in which the protagonist must advance in the plot interacting with various characters and objects',
                'child_ids': [
                    (0, 0, genre5),
                    (0, 0, genre6),
                ]
            }

            record = self.env['shop.videogame.genre'].create(parent_genre_val)
            record = self.env['shop.videogame.genre'].create(parent_genre_val2)
            record = self.env['shop.videogame.genre'].create(parent_genre_val3)

            return True

    @api.multi
    def change_update_date(self):
        self.ensure_one()
        self.date_updated = fields.Datetime.now()

    @api.multi
    def find_videogame(self):
        domain = [
            '|',
                '&', ('name', 'ilike', 'Vdeogame Name'),
                     ('genre_id.name', '=', 'Genre Name'),
                '&', ('name', 'ilike', 'Genre Name 2'),
                     ('genre_id.name', '=', 'Genre Name 2')
        ]
        videogames = self.search(domain)
        logger.info('Videogame found: %s', videogames)
        return True

    @api.model
    def get_all_videogame(self):
        shop_videogame_model = self.env['shop.videogame']
        return shop_videogame_model.search([])

    @api.model
    def get_all_videogame_clients(self):
        shop_client_model = self.env['shop.client']
        return shop_client_model.search([])



class ShopClient(models.Model):
    _name = 'shop.client'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Client Since')
    date_end = fields.Date('Termination Date')
    client_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')

class ShopLoan(models.Model):
    _name = 'shop.loan'
    _description = 'Videogame Loan'
    _rec_name = 'videogame_id'
    _order = 'date_end desc'

    videogame_id = fields.Many2one('shop.videogame', required=True, default=lambda self: self.env['shop.videogame'].search([('name', '=', self.env['ir.config_parameter'].get_param('name_videogame'))]))

    client_id = fields.Many2one('shop.client', required=True)
    #videogame_id =  fields.Many2one('shop.videogame', default='', required=True)
    date_start = fields.Date('Loan Start', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    date_end = fields.Date('Loan End', default=lambda *a:(datetime.now() + timedelta(days=(6))).strftime('%Y-%m-%d'))

    client_image = fields.Binary('Client Image', related='client_id.partner_id.image')

    

    @api.constrains('videogame_id')
    def _check_videogame_id(self):
        for loan in self:
            videogame = loan.videogame_id
            if not videogame.state == 'borrowed' and not videogame.state == 'draft':
                videogame.state = 'borrowed'
            else:
                raise models.ValidationError('Videogame needs to be Available !') 

            domain = ['&',('videogame_id.id', '=', videogame.id), ('date_end', '>=', datetime.now())]
            videogame.is_lent = self.search(domain, count=True) > 1 
            if videogame.is_lent:
                raise models.ValidationError('Videogame is Lent!') 
    
    @api.constrains('date_end', 'date_start')
    def _check_dates(self):
        for loan in self:
            if loan.date_start > loan.date_end:
                raise models.ValidationError('Start date After end date!')
