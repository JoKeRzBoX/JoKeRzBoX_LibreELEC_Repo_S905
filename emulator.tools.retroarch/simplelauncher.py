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
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_1_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_2_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_2_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_2_lib"))
          myParam['l'] = util.getConfig("core_2_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_2_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_3_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_3_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_3_lib"))
          myParam['l'] = util.getConfig("core_3_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_3_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_4_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_4_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_4_lib"))
          myParam['l'] = util.getConfig("core_4_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_4_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_5_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_5_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_5_lib"))
          myParam['l'] = util.getConfig("core_5_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_5_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_6_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_6_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_6_lib"))
          myParam['l'] = util.getConfig("core_6_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_6_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_7_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_7_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_7_lib"))
          myParam['l'] = util.getConfig("core_7_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_7_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_8_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_8_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_8_lib"))
          myParam['l'] = util.getConfig("core_8_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_8_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_9_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_9_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_9_lib"))
          myParam['l'] = util.getConfig("core_9_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_9_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_10_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_10_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_10_lib"))
          myParam['l'] = util.getConfig("core_10_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_10_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_11_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_11_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_11_lib"))
          myParam['l'] = util.getConfig("core_11_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_11_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_12_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_12_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_12_lib"))
          myParam['l'] = util.getConfig("core_12_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_12_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_13_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_13_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_13_lib"))
          myParam['l'] = util.getConfig("core_13_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_13_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_14_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_14_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_14_lib"))
          myParam['l'] = util.getConfig("core_14_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_14_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     if util.getConfig("core_15_lib"):
          myParam = {}
          myParam['f'] = util.getConfig("core_15_folder")
          myParam['c'] = util.getCoreName(util.getConfig("core_15_lib"))
          myParam['l'] = util.getConfig("core_15_lib")
          myIcon = util.getCoreIcon(myParam['l'])
          util.addMenuItem(util.getCoreNiceName(util.getConfig("core_15_lib")), util.makeLink(myParam), icon=myIcon, thumbnail=None, folder=True, fanart=fanart)

     # Add direct call to retroarch menu
     myParam = {}
     myParam['m'] = "show+menu"
     util.addMenuItem(EMU_MENU_LABEL, util.makeLink(myParam), icon=None, thumbnail=None, folder=True, fanart=fanart)


	 
def listGames(params, fanart=None, my_string=None):
    emu_core = params['c']
    roms_folder = params['f']
    #pattern = ".*\.(jpg|png|JPG|PNG|txt|TXT|nfo|NFO)$"
    pattern = "^.*\.(?!jpg$|png$|JPG$|PNG$|txt$|TXT$|nfo$|NFO$).+$"
    if os.path.isdir(roms_folder):	
       for file in sorted(os.listdir(roms_folder)):
           if emu_core == "scummvm":
               pattern = "^.*\.(exe|scum|scummvm|ap|sou|map|sm0|sm1|rsc|ims|dat|lfl|lec|blk|out|gme|voc|000|001|002|003|004|005|006|007|008|009|010|011|1|100|101|1C|455|512|(a)|ad|add|aif|ald|all|ang|ask|aud|avd|avi|b25c|babayaga|bak|bbm|bdf|bin|blb|brs|c00|cab|cat|cel|cfg|chk|clg|clm|clt|clu|cps|csc|cup|d64|dcp|dll|dmu|dnr|drv|dsk|dum|ega|egg|ex1|flac|fmc|fnt|fon|gjd|gmc|gra|grv|he0|he2|hep|hpf|hrs|ico|imd|img|in|ine|inf|ini|itk|la0|la1|lic|man|map|mdi|mdt|mhk|mid|mor|mpc|mpc|msg|mus|nib|nl|nut|obj|ogg|ovr|pak|pat|pcx|pe2|pic|pix|pkd|pmv|prc|prg|qa|raw|rbt|rec|res|rl2|rlb|rom|san|sav|scn|scr|seq|set|smk|smp|snd|sng|sound|sp|spr|stk|stk|str|syn|sys|sys16|tab|tex|tga|tlk|tmi|txt|v16|v56|vga|vmd|w32|wav|win|z|zfs)$"
               if os.path.isdir(os.path.join(roms_folder,str(file))):
                   for file2 in os.listdir(os.path.join(roms_folder,str(file))):
                       if re.match(pattern, file2): 
                           myParam = {}
                           myParam['c'] = emu_core
                           myParam['r'] = os.path.join(roms_folder,str(file),str(file2))
                           util.addMenuItem(util.getScummNiceName(str(file)), util.makeLink(myParam), icon=util.findIcon(roms_folder,str(file)), thumbnail=None, folder=True, fanart=fanart)
                           break
           else:
               pattern = "^.*\.(?!jpg$|png$|JPG$|PNG$|txt$|TXT$|nfo$|NFO$).+$"
               if re.match(pattern, file) and not os.path.isdir(os.path.join(roms_folder,str(file))):
                   myParam = {}
                   myParam['c'] = emu_core
                   myParam['r'] = os.path.join(roms_folder,str(file))
                   util.addMenuItem(util.removeExtensions(str(file)), util.makeLink(myParam), icon=util.findIcon(roms_folder,str(file)), thumbnail=None, folder=True, fanart=fanart)
    else:
        util.okDialog("Roms folder not found.", "Please review Simple Launcher configuration.")

def playGame(params):
    emu_core = params['c']
    rom_file = params['r']
    util.addMenuItem(EMU_WILL_RUN_MESSAGE,link=None,icon=None, thumbnail=None, folder=True, fanart=None)
    util.runEmulator(emu_core, rom_file)
    
def launchMenu(params):
    util.addMenuItem(EMU_WILL_RUN_MESSAGE,link=None,icon=None, thumbnail=None, folder=True, fanart=None)
    util.runRetroarchMenu()



