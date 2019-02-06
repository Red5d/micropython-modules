import network

# Example Usage:
#
# import bestwifi
# wlan = network.WLAN()
# wlan.active(True)
# netpws = {'network1': 'network1password', 'network2': 'network2password'}
# bestwifi.connect(wlan, netpws)

def connect(wlan, netpws):
    nets = wlan.scan()
    bestnet = ''
    bestsig = -500
    print("found "+str(len(nets))+" networks")
    for net in nets:
        if net[0].decode('utf-8') in netpws.keys():
            if net[3] > bestsig:
                bestsig = net[3]
                bestnet = net[0].decode('utf-8')
    print("Using "+bestnet)
    if bestnet != '':
        print('connecting to network '+bestnet+' ...')
        wlan.connect(bestnet, netpws[bestnet])
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())

    return wlan.ifconfig()
