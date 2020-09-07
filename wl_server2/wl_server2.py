from aiohttp import web
from datetime import datetime
import mysql.connector

# datetime object containing current date and time
now = datetime.now()

# DB connection
mydb = mysql.connector.connect(host="10.44.30.32",user="lozik",password="lozik",database="test")
if (mydb):
    print ("DB connection successfull", now.strftime("%d/%m/%Y %H:%M:%S"))
else:
    print ("DB connection fail")

def do_something(unit, unit_id, ign):
    try:
        mycursor = mydb.cursor()
    except SQLAlchemyError:
        mydb = mysql.connector.connect(
        host="10.44.30.32",
        user="lozik",
        password="lozik",
        database="test")

    sql = "INSERTs INTO test (idtest, testcol) VALUES (%s, %s);"
    val = (unit, unit_id)
    mycursor.execute(sql, val)
    mydb.commit()
    if (mydb):
        mydb = mysql.connector.connect(host="10.44.30.32",user="lozik",password="lozik",database="test")
        if(my):
            print ("DB reconected")
        else:
            print ("DB Connection fail")
    else:
        print ("DB Connection fail")

    print(mycursor.rowcount, "record inserted.")

    print(unit)
    print(unit_id)
    print(ign)

async def call_answer(request):
    global unit, unit_id, ign
    params = request.rel_url.query
    unit=params['unit']
    unit_id=params['unit_id']
    ign=params['ign']
    do_something(unit, unit_id, ign)
    return web.Response(text='\n'.join([
        'unit = ' + params['unit'],
        'unit_id = ' + params['unit_id'],
        'ign = ' + params['ign'],
    ]))


app = web.Application()
app.router.add_get('/', call_answer)
web.run_app(app,host='10.44.30.57', port=57002)
    