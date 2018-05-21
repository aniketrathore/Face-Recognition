import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="aniket", host="localhost", port="5432")
"""
if conn:
    print("connected")
    cursor = conn.cursor()
    # query = "INSERT INTO detail VALUES (5,'Mam','A50105214060','CSE')"
    # ids = 1
    query = "CREATE table detail(id int,name varchar(20),enroll varchar (20),course varchar (20))"
    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()
    for row in rows:
        print("Id : " + str(row[0]))
        print("Name : " + row[1])
        print("Enroll : " + row[2])
        print("Course : " + row[3] + "\n")
    print("Succesfully Save")
    conn.close()
else:
    print("Not")
"""


def getLastID():
    try:
        conns = psycopg2.connect(database="postgres", user="postgres", password="ani120000", host="localhost",
                                 port="5432")
        curs = conns.cursor()
        query0 = "SELECT id FROM detail"
        curs.execute(query0)
        rown = curs.fetchall()
        for ro in rown:
            abd = ro

        conns.close()
        return abd[-1]
    except:
        return 0


def getDetails(ids):
    conn = psycopg2.connect(database="postgres", user="postgres", password="ani120000", host="localhost", port="5432")
    cur = conn.cursor()
    query1 = "SELECT * FROM detail WHERE id=" + str(ids)
    cur.execute(query1)
    rowe = cur.fetchall()
    for rowse in rowe:
        return str(rowse[0]), rowse[1], rowse[2], rowse[0]


def getLastID():
    try:
        abd = 0
        conns = psycopg2.connect(database="postgres", user="postgres", password="ani120000", host="localhost",
                                 port="5432")
        curs = conns.cursor()
        query0 = "SELECT id FROM detail"
        curs.execute(query0)
        rown = curs.fetchall()
        for ro in rown:
            abd = ro
        conns.close()
        if not abd:
            return abd[-1]
        else:
            return 0
    except:
        return 0


print(getLastID())
