# coding: utf-8

import os
import sys
from time import sleep
from twitter import *
from connect import twitter_rest, twitter_stream
from analyze import analyze_output
from settings import REST_POLLING_INTERVAL



since_id = None                             # last processed status id
rest_total = 0                              # total statuses received by the rest api
strm_total = 0                              # total statuses received by the streaming api
rest_out = open('out/rest.csv', 'wa+b')     # file where to write rest api status ids
strm_out = open('out/stream.csv', 'wa+b')   # file whare to write streaming api status ids

keywords = 'maradona'


def refresh_console():
    ''' Refreshes the info in console '''

    sys.stdout.write('\rREST\t\t' + str(rest_total) + ' vs. STREAM\t\t' + str(strm_total))
    sys.stdout.flush()

def run_rest():

    global since_id
    global rest_total
    global rest_out

    l = keywords.split(",")
    q = '"%s"' % l.pop()

    for k in l:
        q += ' OR "%s"' % k

    # search api call kwargs
    kwargs = {
        'q': q,
        'result_type': 'recent',
        'count': 100,
    }

    if since_id is not None:
        kwargs['since_id'] = since_id

    res = twitter_rest.search.tweets(**kwargs)

    metadata = res['search_metadata']
    since_id = metadata['max_id_str']

    statuses = res['statuses']
    rest_total += len(statuses)

    # writing status ids to file
    for s in statuses:
        rest_out.write('%i\n' % s['id'])

    refresh_console()



def run_strm():

    global strm_total
    
    iterator = twitter_stream.statuses.filter(track=keywords)
    
    for tweet in iterator:

        # You must test that your tweet has text. It might be a delete
        # or data message.

        if tweet.get('text'):
            strm_total += 1
            strm_out.write('%i\n' % tweet['id'])
            refresh_console()


if __name__ == '__main__':
    import sys
    import threading

    if len(sys.argv) > 1:
        keywords = sys.argv[1]


    print "\nStarting test, hit CTRL+C to end."

    print "\nFiltering search api and streaming api for keywords '%s'..\n" % keywords

    try:

        # streaming api thread
        threading.Thread(target=run_strm).start()

        # rest api thread interval
        while 1:
            threading.Thread(target=run_rest).start()
            sleep(REST_POLLING_INTERVAL)

    except KeyboardInterrupt:
        print "\n\nstopping..\n"

        rest_out.close()
        strm_out.close()


        print "RESULT:\n"

        analyze_output()

        os._exit(1)
