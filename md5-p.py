import os
import pathlib
import hashlib
import sqlite3

def md5_db(md5str,dep=3):
    dep=dep*2
    path='.'
    ii=0
    while(ii<dep):
        path=path+os.sep+md5str[ii:ii+2]
        ii=ii+2
    file=path+os.sep+md5str[ii:ii+2]+".db"
    if not os.path.exists(path):
        os.makedirs(path)
        print(path,'create success')
        pathlib.Path(file).touch()
        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('''CREATE TABLE md5 
        (MD5 CHAR(32) PRIMARY KEY     NOT NULL,
         KEY           CHAR(50)    NOT NULL );''')
        conn.commit()
        conn.close()
    else:
        if not os.path.exists(file):
            pathlib.Path(file).touch()
            conn = sqlite3.connect(file)
            c = conn.cursor()
            c.execute('''CREATE TABLE md5 
             (MD5 CHAR(32) PRIMARY KEY     NOT NULL,
              KEY           CHAR(50)    NOT NULL );''')
            conn.commit()
            conn.close()
        print(path,'dir exists')
    return file


iiii=0
with open('0551hefei.txt','r',encoding='utf-8') as f:
    for line in f:
        md5str=hashlib.md5(line[0:-1].encode('utf-8')).hexdigest()
        print(line[0:-1],md5str,len(md5str))
        dep=3
        file=md5_db(md5str,dep)
        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute("insert or ignore into md5 (MD5,KEY) values ('"+md5str+"','"+line[0:-1]+"')")
        conn.commit()
        conn.close()

       
        
