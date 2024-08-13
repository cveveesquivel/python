class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL= 3

    def __init__(self, status = False, muted = False, volume=MIN_VOLUME, channel=MIN_CHANNEL):

        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self):
        if self.__status == False:
            self.__status = True
            return self.__status
        elif self.__status == True:
            self.__status = False
            return self.__status

    def mute(self):
        if self.__status == False:
            return self.__muted
        elif self.__muted == False:
            self.__muted = True
            return self.__muted
        return self.__muted

    def channel_up(self):
        if self.__status == False:
            return self.__channel
        self.__channel += 1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        return self.__channel

    def channel_down(self):
        if self.__status == False:
            return self.__channel
        self.__channel -= 1
        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        return self.__channel

    def volume_up(self):
        if self.__status == False:
            return self.__volume
        self.__volume += 1
        self.__muted = False
        if self.__volume >= Television.MAX_VOLUME:
            self.__volume = Television.MAX_VOLUME
        return self.__volume

    def volume_down(self):
        if self.__status == False:
            return self.__volume
        self.__volume -= 1
        self.__muted = False
        if self.__volume <= Television.MIN_VOLUME:
            self.__volume = Television.MIN_VOLUME
        return self.__volume

    def __str__(self):
        stat = self.__status
        vol = self.__volume
        if self.__muted == True:
            vol = 0
        chan = self.__channel

        return f'Power = {stat}, Channel = {chan}, Volume = {vol}'
