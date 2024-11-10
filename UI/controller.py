from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql

class MainWindow_Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_Controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = pymysql.connect(host='localhost', user='root', passwd='', db='pillstore', charset='utf8')
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton.clicked.connect(lambda: self.open(self.ui.table.currentText()))

    def getItem(self):
        cursor = self.db.cursor()
        cursor.execute(f'select * from {self.table}')
        result = cursor.fetchall()
        row = cursor.rowcount
        col = len(result[0])
        self.second.table.setRowCount(row)
        self.second.table.setColumnCount(col)
        self.second.table.setHorizontalHeaderLabels(self.tableHeader)  # 設定表頭

        self.items = []
        for i in range(row):
            item = []
            for j in range(col):
                data = QTableWidgetItem(str(result[i][j]))
                item.append(str(result[i][j]))
                data.setTextAlignment(Qt.AlignCenter)
                self.second.table.setItem(i, j, data)
            self.items.append(item)

    def open(self, table):
        import subwindow
        self.second = subwindow.SubWindow()
        self.table = table
        cursor = self.db.cursor()

        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'pillstore' AND table_name = '{self.table}'")
        tableHeader = cursor.fetchall()
        self.tableHeader = [i[0] for i in tableHeader]

        self.getItem()

        if self.table == '藥品':  # 設定表格寬度
            self.second.table.setColumnWidth(1,500) 
            self.second.table.setColumnWidth(2,800)
            self.second.table.setColumnWidth(5,200)
            self.second.table.setColumnWidth(6,400)
        elif self.table == '主要成分' or self.table == '適應症' or self.table == '包裝':
            self.second.table.setColumnWidth(0,400)
        else: 
            self.second.table.setColumnWidth(0,400)
            self.second.table.setColumnWidth(1,1070)
        self.second.table.resizeRowsToContents()

        self.second.show()
        self.second.addrow.clicked.connect(self.addRow_func)
        self.second.submit.clicked.connect(self.update)
        self.second.delbut.clicked.connect(self.delRow)

    def addRow_func(self):
        rowCount = self.second.table.rowCount()
        colCount = self.second.table.columnCount()
        self.second.table.setRowCount(rowCount+1)  # 增加表格列數

        data = QTableWidgetItem(str(rowCount+1))
        data.setTextAlignment(Qt.AlignCenter)
        self.second.table.setItem(rowCount, 0, data)  # 設定編號
        for i in range(1, colCount):                  # 設定其餘內容為""
            data = QTableWidgetItem("")
            data.setTextAlignment(Qt.AlignCenter)
            self.second.table.setItem(rowCount, i, data)
        cursor = self.db.cursor()
        tmp = '\'\''
        sql = f"INSERT INTO {self.table}({', '.join(self.tableHeader)}) VALUES({rowCount+1}, {(i*(tmp+', '))[:-2]})"
        cursor.execute(sql)
        self.db.commit()

        self.getItem()  # 重新設定表格內容

    def update(self):
        rowCount = self.second.table.rowCount()
        colCount = self.second.table.columnCount()
        
        newitems = []
        for i in range(rowCount):  # 取得新表格內容
            newitems.append([self.second.table.item(i, j).text() for j in range(colCount)])

        cursor = self.db.cursor()
        for i, itemlist in enumerate(self.items):  # 更新資料庫表格
            for j, item in enumerate(itemlist):
                if item != newitems[i][j]:  # 判斷與原本內容不同
                    sql = f"UPDATE {self.table} SET {self.tableHeader[j]}='{newitems[i][j]}' WHERE {self.tableHeader[0]}='{i+1}';"
                    cursor.execute(sql)

        cursor.close()
        self.db.commit()

    def delRow(self):
        num = self.second.lineEdit.text() if self.second.lineEdit.text() != '' else '0'  # =0 防止空點出錯
        cursor = self.db.cursor()
        sql = f"DELETE FROM `{self.table}` WHERE "
        for i in num.split():
            sql += f"{self.tableHeader[0]}={i} OR "
        sql = sql[:-4]

        cursor.execute(sql)
        cursor.close()
        self.db.commit()

        self.getItem()  # 更新畫面