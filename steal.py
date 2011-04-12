#!/usr/bin/env python

import pycurl
import json

class Consumer:
    def __init__(self, event_callback):
        self.last = ""
        self.event_callback = event_callback
        conn = pycurl.Curl()
        conn.setopt(pycurl.URL, "http://stream.meetup.com/2/open_events")
        conn.setopt(pycurl.WRITEFUNCTION, self.consume)
        conn.perform()

    def consume(self, data):
        lines = (self.last + data).split("\n")
        for l in lines[:-1]:
            self.event_callback(json.loads(l))
        self.last = lines[-1]

def cb(event):
    print event

Consumer(cb)
