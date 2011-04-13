import pycurl, json

last = ""

def jsonizer(event_callback):
    """Passes json dicts to the given callback"""
    def consume(data):
        """Buffers data and invokes event_callback on completed lines"""
        global last
        lines = (last + data).split("\n")
        for l in lines[:-1]:
            event_callback(json.loads(l))
        last = lines[-1]

    conn = pycurl.Curl()
    conn.setopt(pycurl.URL, "http://stream.meetup.com/2/open_events")
    conn.setopt(pycurl.WRITEFUNCTION, consume)
    # perform() blocks until interrupted or connection is lost
    conn.perform()
