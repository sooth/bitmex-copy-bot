TESTNET_URL = "https://testnet.bitmex.com/api/v1/"
MAINNET_URL = "https://www.bitmex.com/api/v1/"

LEADERS = {
    'LEADER_A' : {

        # My Bitfinex paper trading keys, aasooth+bitmextest
        'API_KEY' : 'VUuNNLmOs3K3goU-s9hL05YX',
        'API_SECRET' : '71yS_FJpituHRTcGODbpNy2xM3Ov85gRkSbXulWLRQIJ0xYa',
        'ENDPOINT' : TESTNET_URL

    }
}

FOLLOWERS = {
    'FOLLOWER_A' : {

        'API_KEY': 's-r6PL1cisQuyhA16yxi7zOp',
        'API_SECRET': 'F0PHllc3s8a9t78-ULwXSMi5CiqU1jcJcU-LTmJ_uXSAvpfP',
        'ENDPOINT': TESTNET_URL,
        'FOLLOWS' : {
            'LEADER_A' : '20%'
        }

    }
}

#add symbols as needed

SYMBOLS = ['XBTUSD','ETHUSD','LTCUSD','XBTH21', 'XRPUSDT']