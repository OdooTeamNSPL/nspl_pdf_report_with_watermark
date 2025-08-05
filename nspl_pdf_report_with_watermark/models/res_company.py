
from odoo import fields, models


class ResCompany(models.Model):
    """Introduce watermark in pdf reports"""
    _inherit = 'res.company'

    watermark = fields.Boolean(string='Watermark',
                               help='Enable it, if you want to apply watermark '
                                    'on all your pdf reports')
    content_text = fields.Char(string='Text',
                               help="Enter the text You want to display")
    watermark_type = fields.Selection([('image', 'Image'),
                                       ('text', 'Text'), ('logo', 'Logo'),],
                                      default='text',
                                      help='Select the Type of watermark')
    color_picker = fields.Char(string='Color Picker', help='Select the Color')
    font_size = fields.Integer(string='Font size', default=20,
                               help="Enter the font size for the text")
    background_image = fields.Image(string='Image',
                                    help='Set an image to display')
    rotating_angle = fields.Float(string='Angle of Rotation',
                                  help='Enter the angle of rotation')
