import sqlite3

conn = sqlite3.connect("meetups.sqlite")

def setup():
    with conn:
        if not conn.execute(
            "select name from sqlite_master where type='table' and name='event'"
            ).fetchall():
            conn.execute("create table event (id text, name text)")

setup()

def event_callback(event):
    with conn:
        conn.execute("""insert into event values (?, ?)""",
                  (event['id'], event['name']))
        print("added %s" % event['name'])
