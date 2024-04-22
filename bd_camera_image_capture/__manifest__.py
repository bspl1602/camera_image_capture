# -*- coding: utf-8 -*-
###############################################################################
#
#    BeyonData Solutions Private Limited
#
#    Copyright (C) 2024-TODAY BeyonData Solutions Private Limited
#    Author: Mittal Nayar
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#
###############################################################################
{
    'name': "Camera Image Capture",
    'summary': "Camera Image Capture",

    'description': """
Long description of module's purpose
    """,
    'author': 'BeyonData Solutions Private Limited',
    'website': 'https://erp.beyondatagroup.com/',
    'license': 'LGPL-3',
    'version': '17.0.0.0',
    # 'price': '00.00',
    # 'currency': 'USD',
    'depends': ['base','product','stock'],
    'assets': {
        'web.assets_backend': [
            'bd_camera_image_capture/static/src/xml/image_upload.xml',
            'bd_camera_image_capture/static/src/js/image_upload.js',
            'bd_camera_image_capture/static/src/xml/camera_dialog.xml',
            'bd_camera_image_capture/static/src/js/camera_dialog.js'
        ]
    },

    'installable': True,
    'auto_install': True,
}

