# -*- coding: utf-8 -*-
# ######################################################################
# © 2015-2018 Marcos Organizador de Negocios SRL. (https://marcos.do/)
#             Eneldo Serrata <eneldo@marcos.do>
# © 2018 SoftNet Team SRL. (https://www.softnet.do/)
#             Manuel Gonzalez <manuel@softnet.do>
# This file is part of NCF DGII Reports

# NCF DGII Reports is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# NCF DGII Reports is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with NCF DGII Reports.  If not, see <http://www.gnu.org/licenses/>.
# ######################################################################

{
    'name': "Reportes de Comprobantes Fiscales (NCF DGII Reports)",
    'version': '10.0.1.0.0',
    'summary': u"""
        Este módulo implementa los reportes de los números de
         comprobantes fiscales para el cumplimento de la norma 06-18 de la
         Dirección de Impuestos Internos en la República Dominicana.
    """,
    'author': "Marcos Organizador de Negocios SRL, "
              "SoftNet Team SRL, "
              "Odoo Dominicana (ODOM) ",
    'category': 'Localization',

    'external_dependencies': {
        'python': [
            'stdnum.do',
        ],
    },

    # any module necessary for this one to work correctly
    'depends': ['ncf_manager'],

    'data': [
        'security/ir.model.access.csv',
        'views/dgii_report_view.xml',
        'views/account_view.xml',
    ]
}
