import os

URLS = [
    "https://docs.pi-hole.net/ftldns/compatibility/",
    "http://192.168.1.28/admin/groups-adlists.php",
    "http://192.168.1.28/admin/settings.php?tab=piholedhcp",
    "http://192.168.1.28/admin/gravity.php",
    "http://192.168.1.28/admin/groups-domains.php?type=white",
    "http://192.168.1.28/admin/groups-domains.php?type=black",
    "https://github.com/espressif/esp-iot-solution/blob/master/documents/evaluation_boards/ESP-Prog_guide_en.md",
    "https://www.mouser.ch/ProductDetail/Adafruit/3416?qs=F5EMLAvA7ICYzX4Av%252BhRHw==&countrycode=CH&currencycode=CHF",
    "http://s.click.aliexpress.com/e/bQ91w8QM",
    "https://poe.olin.edu/2017/Bounce/",
    "https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_à_CSS/La_syntaxe",
    "https://www.banggood.com/MG995-High-Torgue-Mental-Gear-Analog-Servo-p-73885.html",
    "https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_à_CSS/Les_sélecteurs",
    "https://developer.mozilla.org/fr/Apprendre/CSS/Introduction_à_CSS/La_cascade_et_l_héritage",
    "https://stringfixer.com/fr/Stewart_platform",
    "https://corpus.ulaval.ca/jspui/bitstream/20.500.11794/23444/1/28962.pdf",
    "http://cdn2.boxtec.ch/pub/didel/WS2813MiniStrip.pdf",
    "http://cdn2.boxtec.ch/pub/diverse/WS2813.pdf",
    "http://s.click.aliexpress.com/e/ZvFYzNZFq",
    "https://www.infinitypv.com/images/HeLi-on_manual_v1.pdf",
    "http://nodemcu.com/index_en.html",
    "http://nodemcu.com/index_en.html",
    "https://tmrh20.github.io/RF24Network/Zigbee.html",
    "https://www.banggood.com/10Pcs-NRF24L01-SI24R1-2_4G-Wireless-Power-Enhanced-Communication-Receiver-Module-p-1059602.html?p=0431091025639201412F",
    "https://www.hackster.io/rayburne/esp8266-01-using-arduino-ide-67a124",
    "https://github.com/TMRh20/RF24/blob/master/examples/pingpair_ack/pingpair_ack.ino",
    "https://tmrh20.github.io/RF24/",
    "https://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo",
    "http://www.banggood.com/DC-Power-Male-Female-5_5X-2_1mm-Connector-Adapter-Plug-Cable-Pressed-connected-for-LED-Strips-12V-p-998683.html?p=0431091025639201412F",
    "http://www.banggood.com/4-in-1-Temperature-Pressure-Altitude-Light-Sensor-Module-p-965547.html?p=0431091025639201412F",
    "http://www.wemos.cc/wiki/",
    "http://ip.cadence.com/uploads/pdf/LX3.pdf",
    "http://www.wemos.cc/wiki/uploads/Tutorial/ch341ser_mac_new.zip",
    "http://jmkikori.no-ip.org/jmk/joomla-static/index.php/2-uncategorised/1-introduction-bluetooth-low-energy.html",
    "http://www.banggood.com/USB-Detector-Current-Voltage-Tester-Double-USB-Row-Shows-p-973712.html?p=0431091025639201412F",
    "http://www.wemos.cc/wiki/Tutorial/Downloads",
    "http://www.bluetooth.com/Pages/Bluetooth-Smart-Devices-List.aspx",
    "http://redbearlab.com/nrf51822/",
    "http://www.seeedstudio.com/depot/MDBT40P%C2%A0%C2%A0nRF51822%C2%A0based%C2%A0BLE%C2%A0module-p-2503.html",
    "http://bbs.espressif.com",
    "http://www.raytac.com/download/MDBT40/MDBT40%20spec-Version%20A3.pdf",
    "http://www.banggood.com/NRF51822-2_4GHz-Network-Bluetooth-Serial-Module-Support-For-Apple-Android-p-992468.html?p=0431091025639201412F",
    "http://www.banggood.com/HM-10-Bluetooth-4_0-Module-Transparent-Serial-Port-p-967059.html?p=0431091025639201412F",
    "https://github.com/adafruit/ESP8266-Arduino",
    "https://github.com/esp8266/Arduino/blob/master/doc/libraries.md",
    "https://www.ec086.com/Technical_support.html",
    "https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/screen.1.html",
    "http://neilkolban.com/tech/esp8266/",
    "https://www.hackster.io/rayburne/esp8266-01-using-arduino-ide",
    "http://192.168.1.28/admin/",
    "https://www.mcufriend.com",
    "https://www.banggood.com/8GB-Micro-SDTF-Memory-Card-For-Cell-Phone-PDA-MP3-Player-p-926928.html?p=0431091025639201412F",
    "https://www.smokeandwires.co.nz/blog/a-2-4-tft-touchscreen-shield-for-arduino/",
    "https://mixture.io",
    "https://www.microduino.cc/wiki/images/d/d1/AM2321.pdf",
    "http://66.175.219.73/downloads/ch340/CH341SER_MAC66972.ZIP",
    "https://evothings.com",
    "http://www.espruino.com/",
    "https://www.banggood.com/DC-Power-Male-Female-5_5X-2_1mm-Connector-Adapter-Plug-Cable-Pressed-connected-for-LED-Strips-12V-p-998683.html?p=0431091025639201412F",
    "https://www.banggood.com/USB-Port-to-5_5mm-2_1mm-5V-DC-Barrel-Jack-Power-Cable-Connector-p-997025.html?p=0431091025639201412F",
    "http://www.ikalogic.com/ikalogic-products/scanalogic-2/",
    "https://s.click.aliexpress.com/e/J2zVfYFAq",
    "https://goo.gl/hKB7W1",
    "https://www.mouser.ch/ProductDetail/Espressif-Systems/ESP32-DevKitC-VIB?qs=sGAEpiMZZMve4%2fbfQkoj%252bOPQQxxv5be9DpEa9draprU=",
    "https://bgd.onl/21",
    "https://www.logicpoet.com/scansion/",
    "https://s.click.aliexpress.com/e/aY3Jamyr3",
    "https://www.fablab-chene20.ch",
    "https://www.fablab-chene20.ch",
    "https://wiki.seeedstudio.com/images/7/7c/CH340DS1_EN.PDF",
    "http://www.wemos.cc/downloads",
    "https://class.coursera.org/microcontroleurs-004/forum/thread?thread_id=327",
    "https://www.mon-club-elec.fr/pmwiki_reference_arduino/pmwiki.php?n=Main.PortManipulation",
    "https://dropplets.com",
    "https://www.szjdf.net/Private/ProductFiles/595775de665f4acba6a1.pdf",
    "https://letsmakerobots.com/node/31422",
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
{:rel=“nofollow”}
"""
