import pandas as pd
from sqlalchemy import create_engine
import hashlib

dbUser = "root"
dbPassword = "admin"
dbHost = "localhost"
dbName = "relatorio_xavier"
dbTable = "chamados_soma"
excelFile = "teste.xlsx"

def readExcel(excelFile):
    try:
        dataFrame = pd.read_excel(excelFile)
        return dataFrame
    except:
        exit()

def connectDb(dbUser,dbPassword,dbHost,dbName):
    try:
        engine = create_engine("mysql://"+dbUser+":"+dbPassword+"@"+dbHost+"/"+dbName)
        return engine
    except:
        exit()

def writeDataframe(dataFrame,engine,dbTable):
    try:
        dataFrame.to_sql(dbTable, con=engine, if_exists="append", index=False)
    except:
        exit()

def getMD5(excelFile):
    md5Hash = hashlib.md5()
    file = open(excelFile, "rb")
    readFile = file.read()
    md5Hash.update(readFile)
    hashString = md5Hash.hexdigest()
    return hashString

def checkDuplicate(hashString, filename, engine):
    conn = engine.connect()
    conn.execute('SELECT checksum FROM hash_arquivo WHERE checksum = '+hashString)

def insertMd5(hashString, engine):
    conn = engine.connect()
    conn.execute("INSERT INTO hash_arquivo (filename, checksum) VALUES ("+excelFile+","+hashString+")")

dataFrame = readExcel(excelFile)
engine = connectDb(dbUser,dbPassword,dbHost,dbName)


try:
    writeDataframe(dataFrame,engine,dbTable)
    hashString = getMD5(excelFile)
    insertMd5(hashString,engine)
except:
    exit()

