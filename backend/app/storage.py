import sqlite3, json, os
DB=os.getenv("REACHPILOT_DB","reachpilot.db")
def init():
    with sqlite3.connect(DB) as c:
        c.execute("""create table if not exists saved_opportunities(
        id integer primary key autoincrement, topic text not null, platform text not null,
        payload text not null, created_at datetime default current_timestamp)""")
def save(topic,platform,payload):
    init()
    with sqlite3.connect(DB) as c:
        cur=c.execute("insert into saved_opportunities(topic,platform,payload) values(?,?,?)",
                      (topic,platform,json.dumps(payload)))
        return cur.lastrowid
def list_saved():
    init()
    with sqlite3.connect(DB) as c:
        rows=c.execute("select id,topic,platform,payload,created_at from saved_opportunities order by id desc limit 100").fetchall()
    return [{"id":r[0],"topic":r[1],"platform":r[2],"payload":json.loads(r[3]),"created_at":r[4]} for r in rows]
