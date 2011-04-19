Steal This Database
===================

This is an example application for the Meetup
[OpenEvents stream][doc]. It requires Python 2.5 or higher, PycURL,
sqlite3.

On first run `steal.py` creates database "meetups.sqlite" in the
current directory, then proceeds to insert or update events as they
arrive. Event names are printed to stdout.

[doc]: http://www.meetup.com/meetup_api/docs/stream/2/open_events/
