import sys, urllib, string, os, subprocess, re
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

ADDON_ID = 'emulator.tools.retroarch'
CORE_LIB_POSTFIX="_libretro.so"
BIN_FOLDER="bin"
RES_FOLDER="resources"
RETROARCH_EXEC="retroarch.sh"

addon = xbmcaddon.Addon(id=ADDON_ID)

def runRetroarchMenu():
    addon_dir = xbmc.translatePath( addon.getAddonInfo('path') )
    bin_folder = os.path.join(addon_dir,BIN_FOLDER)
    retroarch_exe = os.path.join(bin_folder,RETROARCH_EXEC)
    os.system(retroarch_exe)
    #subprocess.call(retroarch_exe, shell=True)

def runEmulator(core, rom_file):
    addon_dir = xbmc.translatePath( addon.getAddonInfo('path') )
    retroarch_exe = os.path.join(addon_dir,BIN_FOLDER,RETROARCH_EXEC)
    os.system(retroarch_exe + " " + core + " \"" + rom_file + "\"")
    #subprocess.call(retroarch_exe + " " + core + " \"" + rom_file + "\"", shell=True)
    #System.Exec(retroarch_exe)


def getConfig(setting_name):
    return addon.getSetting(setting_name)

def getCoreNiceName(library_name):
    nice_name = getCoreName(library_name)
    addon_dir = xbmc.translatePath( addon.getAddonInfo('path') )
    info_file = os.path.join(addon_dir, "lib", "libretro", removeExtensions(library_name) + ".info")
    if os.path.exists(info_file):
        with open(info_file) as fp:
            for line in fp:
                if re.match("display_name = ",line):
		             nice_name = re.sub("display_name *= *\"","",line)
		             nice_name = re.sub("\".*","",nice_name)				 
		    	     break
    return nice_name
	
def getScummNiceName(scumm_short_name):
    d = {}
    addon_dir = xbmc.translatePath( addon.getAddonInfo('path') )
    if os.path.isfile(os.path.join(addon_dir,RES_FOLDER,"scumm_map.txt")):
       with open(os.path.join(addon_dir,RES_FOLDER,"scumm_map.txt")) as f:
          for line in f:
              (key, val) = line.split("|")
              d[key] = val
    try:
        if d[scumm_short_name.lower()]:
            return d[scumm_short_name.lower()]
        else:
            return scumm_short_name
    except:
        pass
    return scumm_short_name




def getCoreName(library_name):
    return string.replace(library_name,CORE_LIB_POSTFIX,"")
	
def removeExtensions(file_name):
    return  re.sub("\..*","",file_name)

def findIcon2(folder_to_look, file_name):
    return os.path.join(folder_to_look, removeExtensions(file_name) + ".png")
	
def findIcon(folder_to_look, file_name):
    iconFound = None
    iconFilePath1 = os.path.join(folder_to_look, removeExtensions(file_name))
    iconFilePath2 = os.path.join(folder_to_look, file_name)
    if os.path.exists(iconFilePath1 + ".png"):
         iconFound = iconFilePath1 + ".png"
    elif os.path.exists(iconFilePath1 + ".jpg"):
         iconFound = iconFilePath1 + ".jpg"
    elif os.path.exists(iconFilePath1 + ".PNG"):
         iconFound = iconFilePath1 + ".PNG"
    elif os.path.exists(iconFilePath1 + ".JOG"):
         iconFound = iconFilePath1 + ".JPG"
    elif os.path.exists(iconFilePath2 + ".png"):
         iconFound = iconFilePath2 + ".png"
    elif os.path.exists(iconFilePath2 + ".jpg"):
         iconFound = iconFilePath2 + ".jog"
    elif os.path.exists(iconFilePath2 + ".PNG"):
         iconFound = iconFilePath2 + ".PNG"
    elif os.path.exists(iconFilePath2 + ".JOG"):
         iconFound = iconFilePath2 + ".JPG"
    return iconFound

def playMedia(title, thumbnail, link, mediaType='Video') :
    """Plays a video

    Arguments:
    title: the title to be displayed
    thumbnail: the thumnail to be used as an icon and thumbnail
    link: the link to the media to be played
    mediaType: the type of media to play, defaults to Video. Known values are Video, Pictures, Music and Programs
    """
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)

def parseParameters(inputString=sys.argv[2]):
#def parseParameters(inputString=""):
    """Parses a parameter string starting at the first ? found in inputString
    
    Argument:
    inputString: the string to be parsed, sys.argv[2] by default
    
    Returns a dictionary with parameter names as keys and parameter values as values
    """
    parameters = {}
    p1 = inputString.find('?')
    if p1 >= 0:
        splitParameters = inputString[p1 + 1:].split('&')
        for nameValuePair in splitParameters:
            if (len(nameValuePair) > 0):
                pair = nameValuePair.split('=')
                key = pair[0]
                value = urllib.unquote(urllib.unquote_plus(pair[1])).decode('utf-8')
                parameters[key] = value
    return parameters

def notify(addonId, message, timeShown=5000):
    """Displays a notification to the user
    
    Parameters:
    addonId: the current addon id
    message: the message to be shown
    timeShown: the length of time for which the notification will be shown, in milliseconds, 5 seconds by default
    """
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))


def showError(addonId, errorMessage):
    """
    Shows an error to the user and logs it
    
    Parameters:
    addonId: the current addon id
    message: the message to be shown
    """
    notify(addonId, errorMessage)
    xbmc.log(errorMessage, xbmc.LOGERROR)

def extractAll(text, startText, endText):
    """
    Extract all occurences of a string within text that start with startText and end with endText
    
    Parameters:
    text: the text to be parsed
    startText: the starting tokem
    endText: the ending token
    
    Returns an array containing all occurences found, with tabs and newlines removed and leading whitespace removed
    """
    result = []
    start = 0
    pos = text.find(startText, start)
    while pos != -1:
        start = pos + startText.__len__()
        end = text.find(endText, start)
        result.append(text[start:end].replace('\n', '').replace('\t', '').lstrip())
        pos = text.find(startText, end)
    return result

def extract(text, startText, endText):
    """
    Extract the first occurence of a string within text that start with startText and end with endText
    
    Parameters:
    text: the text to be parsed
    startText: the starting tokem
    endText: the ending token
    
    Returns the string found between startText and endText, or None if the startText or endText is not found
    """
    start = text.find(startText, 0)
    if start != -1:
        start = start + startText.__len__()
        end = text.find(endText, start + 1)
        if end != -1:
            return text[start:end]
    return None
    
def makeLink(params, baseUrl=sys.argv[0]):
    """
    Build a link with the specified base URL and parameters
    
    Parameters:
    params: the params to be added to the URL
    BaseURL: the base URL, sys.argv[0] by default
    """
    #return baseUrl + '?' +urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
    return baseUrl + '?' +urllib.urlencode(dict([k.encode('utf-8'),unicode(v).encode('utf-8')] for k,v in params.items()))
    # JoKeRz
    #return 'hahah'
    
def addMenuItem(caption, link, icon=None, thumbnail=None, folder=False, fanart=None):
    """
    Add a menu item to the xbmc GUI
    
    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item
    
    Returns True if the item is successfully added, False otherwise
    """
    #listItem = xbmcgui.ListItem(unicode(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem = xbmcgui.ListItem(str(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Game", infoLabels={ "Title": caption })
    listItem.setProperty('fanart_image', fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=folder)

def endListing():
    """
    Signals the end of the menu listing
    """
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

