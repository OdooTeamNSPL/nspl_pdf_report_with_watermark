
from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    watermark = fields.Boolean(related='company_id.watermark',
                               help='Enable it, if you want to apply watermark '
                                    'on all your pdf reports'
                               )
    content_text = fields.Char(related='company_id.content_text',
                               help="Enter the text You want to display")
    watermark_type = fields.Selection(related='company_id.watermark_type',
                                      help='Select the Type of watermark')
    color_picker = fields.Char(related='company_id.color_picker',
                               help='Select the Color')
    font_size = fields.Integer(related='company_id.font_size',
                               help="Enter the font size for the text")
    background_image = fields.Image(related='company_id.background_image',
                                    help='Set an image to display')
    rotating_angle = fields.Float(related='company_id.rotating_angle',
                                  help='Enter the angle of rotation')
