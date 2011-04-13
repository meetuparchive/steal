import sqlite3

conn = sqlite3.connect("meetups.sqlite")

def setup():
    with conn:
            conn.execute("create table if not exists event (id text, name text)")
            conn.execute("create unique index if not exists event_id on event (id)")

setup()

def event_callback(event):
    with conn:
        conn.execute("""insert or replace into event values (?, ?)""",
                  (event['id'], event['name']))
        print("added %s" % event['name'])
