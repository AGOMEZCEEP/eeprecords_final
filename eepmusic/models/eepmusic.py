
#-*- coding: utf-8 -*-
from odoo import models, fields, api
class EepMusic(models.Model):
   _name = 'cantante'
   _inherit = ['cantante','mail.thread']
   puntuacion = fields.Integer('Puntuación')
   user_id = fields.Many2one('res.users', 'Productor')
   plataforma = fields.Char('Plataforma')
   date_deadline = fields.Date('Disponible Desde:')
   date_deadline2 = fields.Date('Disponible Hasta:')
   name = fields.Char(help="Lista de Artistas.")

   def do_marcar(self):
      if self.user_id != self.env.user:
     	  raise Exception('Solo el Productor puede marcar su la canción esta Disponible o no')
      else:
         return super(TodoMusic, self).do_marcar()

   def do_limpiar(self):
      domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
      done_recs = self.search(domain)
      done_recs.write({'active': False})
      return True

  
