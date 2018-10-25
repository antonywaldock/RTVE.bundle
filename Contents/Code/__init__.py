import content
import config

TITLE  = "RTVE"
PREFIX = "/video/rtve"
ART = 'rtve.png'
ICON = 'rtve.png'

##########################################################################################
def Start():

    ObjectContainer.title1 = TITLE

    HTTP.CacheTime = CACHE_1HOUR
    HTTP.Headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:22.0) Gecko/20100101 Firefox/22.0"

##########################################################################################
@handler(PREFIX, TITLE, art=ART, thumb=ICON)
def MainMenu():

    oc = ObjectContainer()

    title = "Directos"
    oc.add(
        DirectoryObject(
            key = 
                Callback(
                    Live,
                    title = title
                ),
            title = title,
            thumb = R('directos.png')

        )
    )

    return oc

##########################################################################################
@route(PREFIX + '/live')
def Live(title):

    oc = ObjectContainer(title2 = title)

    for channel_id in content.ordered_tv_channels:

        channel = content.tv_channels[channel_id]

        try:
            mdo = URLService.MetadataObjectForURL(channel.live_url())
            mdo.title = channel.title 
                
            oc.add(mdo)
        except:
            pass # Live stream not currently available

    if len(oc) < 1:
        return NoProgrammesFound(oc, title)

    return oc     

##########################################################################################
def NoProgrammesFound(oc, title):

    oc.header  = title
    oc.message = "No programmes found."
    return oc

