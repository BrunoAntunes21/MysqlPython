import MySQLdb

host="localhost"
user=""
password="123456"
db="escola"
port= 3306

con=MySQLdb.connect(host,user,password,db,port)
c=con.cursor()

def select(fields,table,where=None):
    global c
    query="SELECT "+fields+"FROM"+table
    if(where):
        query=query+"WHERE"+where
    c.execute(query)
    return c.fetchall()

def insert(values,table,fields=None):
    global c,con

    query="INSERT INTO"+table
    if(fields):
        query=query+"("+fields+")"
        query=query+"values"+",".join(["("+v+")"for v in values])
        values=["default",'bruno antunes',]
        c.execute(query)
        con.commit()


