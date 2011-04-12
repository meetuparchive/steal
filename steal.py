#!/usr/bin/env python

import pycurl
import json

class Consumer:
    def __init__(self):
        self.buffer = ""
        conn = pycurl.Curl()
        conn.setopt(pycurl.URL, "http://stream.meetup.com/2/open_events")
        conn.setopt(pycurl.WRITEFUNCTION, self.consume)
        conn.perform()

    def consume(self, data):
        self.buffer = self.buffer + data
        if data.endswith("\n"):
            event = json.loads(self.buffer)
            self.buffer = ""
            print event

Consumer()
