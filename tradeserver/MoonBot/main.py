import sys, getopt
from moonBot import moonBot


def readCommandLineOpts(argv):
    period = 300 #seconds
    pair = "BTC_ETH"
    
    try:
        opts, args = getopt.getopt(argv, "hp:t:a:s:")
    except getopt.GetoptError:
        print 'foo!YOU ARE NOT PREPARED!'
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print 'think twice before u Hodl: main.py -p 3 -t <trade pair> -a <apiKey> -s <secret>'
            sys.exit()
        elif opt in ("-p"):
            if (int(arg) in [3, 300,900,1800,7200,14400,86400]): #pre defined time period required by polonix and me
                period = arg
            else:
                print 'think twice before u Hodl'
                sys.exit(2)
        elif opt in ("-t"):
            pair = arg
        elif opt in ("-a"):
            apiKey = arg
        elif opt in ("-s"):
            secret = arg
    return period, pair, apiKey, secret

if __name__ == "__main__":
    args = readCommandLineOpts(sys.argv[1:])
    bot = moonBot(args[0], args[1], args[2], args[3])
    print bot.queryCurrentTicker();