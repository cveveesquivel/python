class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self, status: bool = False, muted: bool = False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        """

        :param status: Determines if TV is on (True) or off (False
        :param muted: Determines if volume is muted (True) or not muted (False)
        :param volume: Gives volume of TV. Is affected by muted status
        :param channel: Gives channel of TV.
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> bool:
        if self.__status == False:
            self.__status = True
            return self.__status
        elif self.__status == True:
            self.__status = False
            return self.__status

    def mute(self) -> bool:
        if self.__status == False:
            return self.__muted
        elif self.__muted == False:
            self.__muted = True
            return self.__muted
        return self.__muted

    def channel_up(self) -> int:
        if self.__status == False:
            return self.__channel
        self.__channel += 1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        return self.__channel

    def channel_down(self) -> int:
        if self.__status == False:
            return self.__channel
        self.__channel -= 1
        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        return self.__channel

    def volume_up(self) -> int:
        if self.__status == False:
            return self.__volume
        self.__volume += 1
        self.__muted = False
        if self.__volume >= Television.MAX_VOLUME:
            self.__volume = Television.MAX_VOLUME
        return self.__volume

    def volume_down(self) -> int:
        if self.__status == False:
            return self.__volume
        self.__volume -= 1
        self.__muted = False
        if self.__volume <= Television.MIN_VOLUME:
            self.__volume = Television.MIN_VOLUME
        return self.__volume

    def __str__(self) -> str:
        stat = self.__status
        vol = self.__volume
        if self.__muted == True:
            vol = 0
        chan = self.__channel

        return f'Power = {stat}, Channel = {chan}, Volume = {vol}'
