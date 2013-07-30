

def analyze_output():
    rest_file = open('out/rest.csv')
    stream_file = open('out/stream.csv')

    rest_ids = set([int(id) for id in rest_file.readlines()])
    stream_ids = set([int(id) for id in stream_file.readlines()])

    dif1 = rest_ids.difference(stream_ids)
    dif2 = stream_ids.difference(rest_ids)

    print "REST has %i tweets that STREAMING doesn't" % len(dif1)
    print "STREAMING has %i tweets that REST doesn't" % len(dif2)
    print "Both have in common %i tweets" % len(rest_ids.intersection(stream_ids))
    print " "

    rest_file.close()
    stream_file.close()

