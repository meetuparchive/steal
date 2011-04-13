#!/usr/bin/env python

import stream, storage

if __name__ == "__main__":
    # start piping the stream to our storage
    stream.jsonizer(storage.event_callback)
