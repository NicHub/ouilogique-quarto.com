import os

URLS = [
    "http://www.gearbest.com/batteries/pp_241348.html",
    "https://www.infinitypv.com/images/HeLi-on_manual_v1.pdf",
    "http://nodemcu.com/index_en.html",
    "https://www.banggood.com/10Pcs-NRF24L01-SI24R1-2_4G-Wireless-Power-Enhanced-Communication-Receiver-Module-p-1059602.html?p=0431091025639201412F",
    "https://tmrh20.github.io/RF24Network/Zigbee.html",
    "https://github.com/TMRh20/RF24/blob/master/examples/pingpair_ack/pingpair_ack.ino",
    "https://tmrh20.github.io/RF24/",
    "https://www.hackster.io/rayburne/esp8266-01-using-arduino-ide-67a124",
    "https://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo",
    "http://www.banggood.com/DC-Power-Male-Female-5_5X-2_1mm-Connector-Adapter-Plug-Cable-Pressed-connected-for-LED-Strips-12V-p-998683.html?p=0431091025639201412F",
    "http://www.banggood.com/4-in-1-Temperature-Pressure-Altitude-Light-Sensor-Module-p-965547.html?p=0431091025639201412F",
    "https://www.microduino.cc/wiki/images/d/d1/AM2321.pdf",
    "http://www.wemos.cc/wiki/",
    "http://66.175.219.73/downloads/ch340/CH341SER_MAC66972.ZIP",
    "http://jmkikori.no-ip.org/jmk/joomla-static/index.php/2-uncategorised/1-introduction-bluetooth-low-energy.html",
    "http://www.wemos.cc/wiki/uploads/Tutorial/ch341ser_mac_new.zip",
    "http://www.banggood.com/USB-Detector-Current-Voltage-Tester-Double-USB-Row-Shows-p-973712.html?p=0431091025639201412F",
    "http://www.wemos.cc/wiki/Tutorial/Downloads",
    "http://bbs.espressif.com/",
    "https://www.ec086.com/Technical_support.html",
    "https://evothings.com/",
    "http://www.bluetooth.com/Pages/Bluetooth-Smart-Devices-List.aspx",
    "http://redbearlab.com/nrf51822/",
    "https://www.mcufriend.com/",
    "http://www.raytac.com/download/MDBT40/MDBT40%20spec-Version%20A3.pdf",
    "http://www.banggood.com/NRF51822-2_4GHz-Network-Bluetooth-Serial-Module-Support-For-Apple-Android-p-992468.html?p=0431091025639201412F",
    "https://github.com/adafruit/ESP8266-Arduino",
    "https://dropplets.com/",
    "http://www.banggood.com/HM-10-Bluetooth-4_0-Module-Transparent-Serial-Port-p-967059.html?p=0431091025639201412F",
    "https://github.com/esp8266/Arduino/blob/master/doc/libraries.md",
    "https://www.banggood.com/8GB-Micro-SDTF-Memory-Card-For-Cell-Phone-PDA-MP3-Player-p-926928.html?p=0431091025639201412F",
    "https://www.smokeandwires.co.nz/blog/a-2-4-tft-touchscreen-shield-for-arduino/",
    "https://www.szjdf.net/Private/ProductFiles/595775de665f4acba6a1.pdf",
    "https://goo.gl/hKB7W1",
    "https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/screen.1.html",
    "http://www.ikalogic.com/ikalogic-products/scanalogic-2/",
    "https://mixture.io/",
    "https://www.banggood.com/DC-Power-Male-Female-5_5X-2_1mm-Connector-Adapter-Plug-Cable-Pressed-connected-for-LED-Strips-12V-p-998683.html?p=0431091025639201412F",
    "https://www.openhomeautomation.net/internet-of-things-dashboard/",
    "https://www.banggood.com/USB-Port-to-5_5mm-2_1mm-5V-DC-Barrel-Jack-Power-Cable-Connector-p-997025.html?p=0431091025639201412F",
    "http://neilkolban.com/tech/esp8266/",
    "https://www.hackster.io/rayburne/esp8266-01-using-arduino-ide",
    "https://letsmakerobots.com/node/31422",
    "https://www.logicpoet.com/scansion/",
    "https://bgd.onl/21",
    "https://www.fablab-chene20.ch/",
    "https://wiki.seeedstudio.com/images/7/7c/CH340DS1_EN.PDF",
    "https://www.wemos.cc/wiki/uploads/Tutorial/ch341ser_mac_new.zip",
    "http://www.wemos.cc/downloads",
    "https://www.mon-club-elec.fr/pmwiki_reference_arduino/pmwiki.php?n=Main.PortManipulation",
    "https://class.coursera.org/microcontroleurs-004/forum/thread?thread_id=327",
]

SOURCE_PATH_POSTS = os.path.expanduser("~/kdnicomac/sites/ouilogique.com/_posts/")

files = sorted(os.listdir(SOURCE_PATH_POSTS), reverse=True)
for file in files:
    fpath = f"{SOURCE_PATH_POSTS}{file}"
    with open(fpath, "rt", encoding="utf-8") as _f:
        for line in _f:
            for url in URLS:
                if url in line:
                    if "nofollow" not in line:
                        print(file)
                        print(line)
"""
{rel=“nofollow”}
"""
