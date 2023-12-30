Upcycle Zeppelin Air with ZOUDIO aio4ch and Raspberry Pi Zero 2 W. All digital stream allows seamless Airplay 2, with close amplifier integration and great sound.

The ZOUDIO amplifier is connected to the Raspberry Pi over UART and I2S. The UART
connection allows `ZOUDIO_daemon.py` to control the amplifier depending on the
Airplay 2 stream state.

Setup the ZOUDIO amplifier with the provide EQ profile, and send `BT DISABLE` to the amplifier to disable the builtin Bluetooth Module. See more about this command here [ZOUDIO / AIO438-firmware-releases](https://github.com/ZOUDIO/AIO438-firmware-releases).

Then setup a newer Raspberry Pi with Raspberry Pi OS Lite, and follow the instructions in [INSTALL.MD](INSTALL.md).