class TV:
    def __init__(self):
        self.__channel = 1  # Default channel is 1
        self.__volume_level = 1  # Default volume level is 1
        self.__on = False  # By default, TV is off

    def turn_on(self):
        self.__on = True

    def turn_off(self):
        self.__on = False

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel):
        if self.__on and 1 <= self.__channel <= 120:
            self.__channel = channel

    def get_volume_level(self):
        return self.__volume_level

    def set_volume(self, volume_level):
        if self.__on and 1 <= self.__volume_level <= 7 and 0 <= volume_level <= 7:
            self.__volume_level = volume_level

    def channel_up(self):
        if self.__on and self.__channel < 120:
            self.__channel += 1

    def channel_down(self):
        if self.__on and self.__channel > 1:
            self.__channel -= 1

    def volume_up(self):
        if self.__on and self.__volume_level < 7:
            self.__volume_level += 1

    def volume_down(self):
        if self.__on and self.__volume_level > 1:
            self.__volume_level -= 1


tv = TV()
# print(tv.__channel)  # AttributeError: 'TV' object has no attribute '__channel'
tv.set_volume(-100)
print(tv.get_channel())
