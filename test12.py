import sqlite3

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
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('myImage.png'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('myMovie.mpg'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('World.txt'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                ('myPhoto.jpg'))
    conn.commit()
conn.close()


conn = sqlite3.connect('cool.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT file_name WHERE file_name = [txt]")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "File Name: {}".format(item[0])
    print(msg)
