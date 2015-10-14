# -*- coding: utf-8 -*-
"""
/***************************************************************************
 vmmQry
                                 A QGIS plugin
 Bevraag de database van VMM
                             -------------------
        begin                : 2015-10-07
        copyright            : (C) 2015 by VMM
        email                : kaywarrie@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load vmmQry class from file vmmQry.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .vmmQry import vmmQry
    return vmmQry(iface)
