import sqlite3

conn = sqlite3.connect("meetups.sqlite")

# create tables if not already there
with conn:
    conn.execute("""create table if not exists event 
                    (id text, name text, description text, url text, time integer)""")
    conn.execute("create unique index if not exists event_id on event (id)")

def event_callback(event):
    """Passed event dictionaries as they are streamed in"""
    with conn:
        values = [event.get(k, None) for k in ['id', 'name', 'description', 'event_url', 'time']]
        conn.execute("""insert or replace into event values
                        (?, ?, ?, ?, ?)""", values)
        print("added %s" % event['name'])
