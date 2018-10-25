class Channel(object):
    def __init__(self, title, thumb, channel_id, region_id, live_id):
        self.title = title
        self.thumb = thumb
        self.channel_id = channel_id
        self.live_id = live_id

        self.schedule_url = "http://www.bbc.co.uk/iplayer/schedules/%s" % (self.channel_id)

        thumb_url = """http://www.irtve.es/css/rtve.commons/rtve.multisign2014/custom/CTV_{0}/i/mosca_CTV_{0}.png"""
            
        self.thumb_url = thumb_url.format(self.thumb)

    def live_url(self):
        return "http://www.rtve.es/directo/%s" % self.channel_id

tv_channels = {
    #                           title                thumb               channel_id       region_id  live_id
    'la1':           Channel('La 1',           'LA1',          'la-1',       '',  ''),
    'c24h':          Channel('Canal 24H',      'C24H',    'canal-24h',       '',  '')
}
ordered_tv_channels = ['la1','c24h']

