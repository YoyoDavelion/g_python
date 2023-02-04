import sys, os
from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage
extension_info = {
    "title": "Market offers parser",
    "description": "Parse offers",
    "version": "1.0",
    "author": "YoyoDavelion"
}

ext = Extension(extension_info, sys.argv, {"use_click_trigger": True})
ext.start()


def market(message):
    offers = message.packet.read('i')[0]
    for i in range(0, offers):
        offer_id,status,furni_type,furni_id = message.packet.read('iiii')
        if furni_type == 1:
            stuff_category = message.packet.read('i')[0]
            if stuff_category == 0:
                message.packet.read('s')
            elif stuff_category == 1:
                message.packet.read('issssss')
            elif stuff_category == 7:
                message.packet.read('sii')
            elif stuff_category == 2:
                message.packet.read('isssss')
            elif stuff_category == 5:
                message.packet.read('iiiii')
        elif furni_type == 2:
            extraData = message.packet.read('s')
        
        elif furni_type == 3:
            uniqueSerialNumber,uniqueSeriesSize = message.packet.read('ii')
        price,timeLeftMinutes,averagePrice,offerCount = message.packet.read('iiii')
        print(offer_id,furni_id,price, averagePrice)
ext.intercept(Direction.TO_CLIENT, market, 'MarketPlaceOffers')

