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
    for item in fileList:
        if item.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(file_name) VALUES(?)", (item,))
            conn.commit()
conn.close()

conn = sqlite3.connect('cool.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files ")
    varPerson = cur.fetchall()
    print(varPerson)
conn.close()
