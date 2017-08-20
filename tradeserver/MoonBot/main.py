#Copyright (c) 2017 LiTao
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#@author litao

#a command line app first to test poloniex api

import time
import sys, getopt
import datetime
from moonBot import moonBot

def main(argv):
    period, pair, apiKey, secret = readCommandLineOpts(argv)
    moon = moonBot(period, pair, apiKey, secret)
    moon.moonWatch()
    
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
    main(sys.argv[1:])