from configuration import Config
# import urequests
import network


def connet_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(Config.SSID, Config.WIFI_PWK)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


connet_to_wifi()