# -*- coding: utf-8 -*-
from PyQt4 import QtSql

class MyDatabaseModel:
    """Custom Database model"""
    def __init__(self,qsqldatabasename):
        self.model = QtSql.QSqlQueryModel()
        self.db = QtSql.QSqlDatabase.database(qsqldatabasename)  # ανοίγει ταυτόχρονα και η σύνδεση:
        print "DB is already opened:", self.db.isOpen()
        if not self.db.isOpen():
            ok = self.db.open()
            if ok:
                print "Database just opened now!"
        else:
            print "Failed to open database!"
            error = self.db.lastError()
            print error.text()

    def set_mymodel(self, query):
        self.model.setQuery(query, self.db)
        if self.model.lastError().isValid():
            print("Error during at devices selection")
        return self.model