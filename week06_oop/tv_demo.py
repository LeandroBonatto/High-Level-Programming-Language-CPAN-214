from tv import TV

def main():
    tv1 = TV(10, 5)
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)

    tv2 = TV(6)
    tv2.turn_on()
    tv2.channel_up()
    tv2.channel_up()
    tv2.volume_up()
    tv2.volume_level = -100

    print("tv1's channel is", tv1.get_channel(),
          "and volume level is", tv1.get_volume_level())
    print("tv2's channel is", tv2.get_channel(),
          "and volume level is", tv2.get_volume_level())

main()  # Call the main function
