import sqlite3
fileList = [('information.docx'),
            ('Hello.txt'),
            ('myImage.png'),
            ('myMovie.mpg'),
            ('World.txt'),
            ('data.pdf'),
            ('myPhoto.jpg')]
conn = sqlite3.connect('cool.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('cool.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files WHERE tbl_files = 'txt'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "File Name: {}".format(item[0])
    print(msg)
