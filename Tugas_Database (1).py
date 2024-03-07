#!/usr/bin/env python
# coding: utf-8

# In[22]:


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2024")


# In[23]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2024"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATKUL_YANG_DIIKUTI VARCHAR(10),
                    SEMESTER INT NOT NULL
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()



# In[14]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2024"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATKUL_YANG_DIIKUTI, SEMESTER) VALUES (%s, %s, %s, %s,%s)"
val = [("V3923004",  "Aulia Diva Sukmadevi", "Pilangkenceng", "Python","2"),
       ("V3923008",  "Erista Devi Fitriani", "Mejayan", "BasisData","2"),
       ("V3923009",  "Gita Latifa Dinar", "Ngawi", "Statistika","2"),
       ("V3923013",  "Lia Fitriani", "Sukoharjo", "Wireless","2"),
       ("V3923015",  "Puput Surya Ningtyas", "Saradan", "PromWeb","2")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[15]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2024"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Dosen (
                    NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATKUL_YANG_DIAJAR VARCHAR(50)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()



# In[16]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2024"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATKUL_YANG_DIAJAR) VALUES (%s, %s, %s)"
val = [("1991091420200801",  "Darmawan Lahru Riatma", "PBO"),
       ("1994062420210701",  "Yusuf Fadlila Rachman", "PYTHON"),
       ("1987052520200801",  "Masbahah", "BASIS DATA"),
       ("1993010520210701",  "Trisna Ari Roshinta","STATISTIKA DAN PROBABILITAS"),
       ("1992092420200901",  "Nur Azizul Haqimi", "PRAKTIK SISTEM OPERASI")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()



# In[17]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2024"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    KODE_MATKUL VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATKUL VARCHAR(50) NOT NULL,
                    NAMA_DOSEN VARCHAR(20),
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[19]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2024"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_kuliah (KODE_MATKUL, NAMA_MATKUL, NAMA_DOSEN, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s, %s)"
val = [("242012",  "PBO", "Darmawan Lahru", "2024-3-7", "L2R1"),
       ("241020",  "PYTHON", "Yusuf Fadila", "2024-3-6", "L2R2"),
       ("241013",  "BASIS DATA", "Masbahah", "2024-3-5", "L2R3"),
       ("241008",  "STATISTIKA DAN PROBABILITAS", "Trisna Ari", "2024-3-4", "R. Mikro"),
       ("241018",  "PRAKTIK SISTEM OPERASI", "Nur Azizul", "2024-3-3", "L2R2")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[24]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2024"
)

cursorObject = dataBase.cursor()

# executing the SELECT query for mahasiswa data
select_mahasiswa_query = """SELECT *
                            FROM MATA_KULIAH"""

cursorObject.execute(select_mahasiswa_query)

# fetching all rows
mahasiswa_rows = cursorObject.fetchall()

# displaying the data
for row in mahasiswa_rows:
    print(row)

# disconnecting from server
dataBase.close()


# In[ ]:




