

from odoo import models, fields, api


class cash(models.Model):
     _name = 'cashier.cash'
     _description = 'cashier.cash'
      
     name = fields.Char(string="name") 
     date = fields.Date(string="date", required=True)
     amount = fields.Float(string="amount", required=True)
     payment_method = fields.Selection([('cash', 'cash'), ('credit_card', 'credit_card'), ('debit_card', 'debit_card'), ('check', 'check'), ('transfer', 'transfer')], string="payment_method", required=True)
     cashier_id = fields.Many2one('cashier.cashier', string="cashier_id")
     tc_id = fields.Many2one('cashier.tc', string="tc_id")
     transf2 = fields.Many2one('cashier.transf', string="transf")
     terminal_id = fields.Many2one('cashier.terminal', string="terminal_id")
     m2000 = fields.Integer(string="2000")
     m1000 = fields.Integer(string="1000")
     m500 = fields.Integer(string="500")
     m200 = fields.Integer(string="200")
     m100 = fields.Integer(string="100")
     m50 = fields.Integer(string="50")
     m20 = fields.Integer(string="20")
     m10 = fields.Integer(string="10")
     m5 = fields.Integer(string="5")    
    
 #    value = fields.Integer()
 #    value2 = fields.Float(compute="_value_pc", store=True)
 #    description = fields.Text()

 #    @api.depends('value')
 #    def _value_pc(self):
 #        for record in self:
 #            record.value2 = float(record.value) / 100

class transf(models.Model):
     _name = 'cashier.transf'
     _description = 'cashier.transf'

     date = fields.Date(string="date", required=True)
     amount = fields.Float(string="amount", required=True)
     bank = fields.Char(string="bank", required=True)
     parner_id = fields.Many2one('res.partner', string="parner_id")

class tc(models.Model):
     _name = 'cashier.tc'
     _description = 'cashier.tc'

     date = fields.Date(string="date", required=True)
     amount = fields.Float(string="amount", required=True)
     authorization = fields.Char(string="authorization", required=True)
     terminal = fields.Many2one('cashier.terminal', string="terminal", required=True)

class terminal(models.Model):
     _name = 'cashier.terminal'
     _description = 'cashier.terminal'

     name = fields.Char(string="name", required=True)
     code = fields.Char(string="code", required=True)
     description = fields.Text(string="description", required=True)
     account_id = fields.Many2one('account.account', string="account_id", required=True)

