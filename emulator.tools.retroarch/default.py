################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2014 Stephan Raue (stephan@openelec.tv)
#
#  OpenELEC is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  OpenELEC is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import os

import util, simplelauncher

ADDON_ID = 'emulator.tools.retroarch'

addon = xbmcaddon.Addon(id=ADDON_ID)
addon_dir = xbmc.translatePath( addon.getAddonInfo('path') )
addonfolder = addon.getAddonInfo('path')

icon    = addonfolder + '/icon.png'
fanart  = addonfolder + '/fanart.jpg'

if util.getConfig("simple_launcher_enabled") == "true":
    
    # Parse parameters
    parameters = util.parseParameters()
    
    if 'm' in parameters:
        simplelauncher.launchMenu(parameters)
    elif 'r' in parameters:
        simplelauncher.playGame(parameters)
    elif 'f' in parameters:
        simplelauncher.listGames(parameters, fanart, addon.getLocalizedString(30005))
    else:
        simplelauncher.buildMenu(fanart, addon.getLocalizedString(30004))
    # Ends list of items for xbmc
    util.endListing()

else:
    util.runRetroarchMenu()