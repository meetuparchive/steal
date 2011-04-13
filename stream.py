import pycurl, json

def jsonizer(event_callback):
    """Passes json dicts to the given callback"""
    last = [""]
    def consume(data):
        """Buffers data and invokes event_callback on completed lines"""
        lines = (last[0] + data).split("\n")
        for l in lines[:-1]:
            event_callback(json.loads(l))
        last[0] = lines[-1]

    conn = pycurl.Curl()
    conn.setopt(pycurl.URL, "http://stream.meetup.com/2/open_events")
    conn.setopt(pycurl.WRITEFUNCTION, consume)
    # perform() blocks until interrupted or connection is lost
    conn.perform()
