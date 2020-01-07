# -*- coding: utf-8 -*-
"""
/***************************************************************************
 traccar
                                 A QGIS plugin
 Qgis plugin for Traccar, the open source system for various GPS tracking devices
                             -------------------
        begin                : 2015-03-09
        copyright            : (C) 2015 by Leonidas Liakos
        email                : leonidas_liakos@yahoo.gr
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
    """Load traccar class from file traccar.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .traccar_mod import traccar
    return traccar(iface)
