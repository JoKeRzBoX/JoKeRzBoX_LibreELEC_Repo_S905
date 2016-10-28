#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC; see the file COPYING. If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# http://www.gnu.org/copyleft/gpl.html
#
import os, stat
import xbmc
import xbmcgui
import xbmcaddon


def makeFilesExecutable():
	scriptPath = xbmc.translatePath(xbmcaddon.Addon(id = 'emulator.tools.retroarch').getAddonInfo('path'))
	scriptPath = os.path.join(scriptPath, 'bin')
	file1 = os.path.join(scriptPath, 'retroarch.sh')
	file2 = os.path.join(scriptPath, 'retroarch.start')
	file3 = os.path.join(scriptPath, 'retroarch')

	try:
		os.chmod(file1, stat.S_IRWXU|stat.S_IRWXG|stat.S_IROTH|stat.S_IXOTH)
		os.chmod(file2, stat.S_IRWXU|stat.S_IRWXG|stat.S_IROTH|stat.S_IXOTH)
		os.chmod(file3, stat.S_IRWXU|stat.S_IRWXG|stat.S_IROTH|stat.S_IXOTH)
		d = xbmcgui.Dialog()
		d.ok('RetroArch', 'File permissions applied', 'scripts should now be executable')        
	except:
		d = xbmcgui.Dialog()
		d.ok('RetroArch', 'Failed to apply permissions', 'Please try again later or do it manualy via ssh')            

if __name__ == '__main__':
	makeFilesExecutable()

