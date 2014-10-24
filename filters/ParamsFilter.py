# -*- coding: utf-8 -*-

"""
***************************************************************************
    QGIS Server Plugin Filters: this test filter changes the SERVICE params
    in the request, tests that the parameter was changed and then restores
    it to its original value
    ---------------------
    Date                 : October 2014
    Copyright            : (C) 2014 by Alessandro Pasotti
    Email                : apasotti at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.server import *
from qgis.core import *

class ParamsFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(ParamsFilter, self).__init__(serverIface)

    def requestReady(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap( )
        original = params['SERVICE']
        request.setParameter('SERVICE', 'ParamsFilter')
        params = request.parameterMap( )
        if params['SERVICE'] == 'ParamsFilter':
            QgsMessageLog.logMessage("SUCCESS - ParamsFilter.responseReady", 'plugin', QgsMessageLog.INFO)
        else:
            QgsMessageLog.logMessage("FAIL    - ParamsFilter.responseReady", 'plugin', QgsMessageLog.CRITICAL)
        request.setParameter('SERVICE', original)
