import sys, urllib, urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import util
import re, os

EMU_MENU_LABEL="<<< RetroArch Menu >>>"
EMU_WILL_RUN_MESSAGE="Please wait while RetroArch starts..."

 
def buildMenu(fanart=None, searchString='SEARCH'):
     
     if util.getConfig("core_1_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_1_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_1_lib"))
          myParam['l'] = util.getConfig("core_1_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_1_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_2_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_2_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_2_lib"))
          myParam['l'] = util.getConfig("core_2_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_2_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_3_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_3_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_3_lib"))
          myParam['l'] = util.getConfig("core_3_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_3_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_4_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_4_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_4_lib"))
          myParam['l'] = util.getConfig("core_4_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_4_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_5_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_5_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_5_lib"))
          myParam['l'] = util.getConfig("core_5_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_5_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_6_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_6_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_6_lib"))
          myParam['l'] = util.getConfig("core_6_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_6_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_7_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_7_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_7_lib"))
          myParam['l'] = util.getConfig("core_7_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_7_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_8_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_8_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_8_lib"))
          myParam['l'] = util.getConfig("core_8_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_8_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_9_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_9_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_9_lib"))
          myParam['l'] = util.getConfig("core_9_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_9_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_10_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_10_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_10_lib"))
          myParam['l'] = util.getConfig("core_10_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_10_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_11_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_11_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_11_lib"))
          myParam['l'] = util.getConfig("core_11_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_11_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_12_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_12_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_12_lib"))
          myParam['l'] = util.getConfig("core_12_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_12_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_13_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_13_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_13_lib"))
          myParam['l'] = util.getConfig("core_13_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_13_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_14_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_14_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_14_lib"))
          myParam['l'] = util.getConfig("core_14_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_14_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_15_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_15_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_15_lib"))
          myParam['l'] = util.getConfig("core_15_lib")
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_15_lib")), util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)

     # Add direct call to retroarch menu
     myParam = {}
     myParam['m'] = "show+menu"
     util.addMenuItem(EMU_MENU_LABEL, util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)


	 
def listGames(params, fanart=None, my_string=None):
    emu_core = params['c']
    roms_folder = params['f']
    #pattern = ".*\..*"
    #pattern = ".*\.(jpg|png|JPG|PNG|txt|TXT|nfo|NFO)$"
    pattern = "^.*\.(?!jpg$|png$|JPG$|PNG$|txt$|TXT$|nfo$|NFO$).+$"
	
    #regexObj = re.compile(".*\.so")
    for root, dirs, files in os.walk(roms_folder, topdown=False):
        for file in filter(lambda x: re.match(pattern, x), files):
            myParam = {}
            myParam['c'] = emu_core
            myParam['r'] = os.path.join(roms_folder,str(file))
			
            util.addMenuItem(util.removeExtensions(str(file)), util.makeLink(myParam), icon=util.findIcon(roms_folder,str(file)), thumbnail=None, folder=True, fanart=fanart)
	

def playGame(params):
    emu_core = params['c']
    rom_file = params['r']
    util.addMenuItem(EMU_WILL_RUN_MESSAGE,link=None,icon=None, thumbnail=None, folder=True, fanart=None)
    util.runEmulator(emu_core, rom_file)
    
def launchMenu(params):
    util.addMenuItem(EMU_WILL_RUN_MESSAGE,link=None,icon=None, thumbnail=None, folder=True, fanart=None)
    util.runRetroarchMenu()



