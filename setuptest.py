import sqlite3


class sugarDatabase:

    def __init__(self) -> None:
        self.database = "sugarDataMonitor.db"
        # self.tablename = "sugarinsulin"
        self.tablename = "sugardatainsulin"

    def Insert_data(self, datalist: list):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'INSERT INTO {self.tablename} (sValue, interval, dose, iType, date) VALUES ("{datalist[0]}","{datalist[1]}",{datalist[2]},"{datalist[3]}", "{datalist[4]}")'
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()

    def get_data(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT * FROM {self.tablename} ORDER BY date ASC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data

    def delete_record(self, cellid: int):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'DELETE FROM {self.tablename} WHERE id = {cellid}'
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()

    def get_single(self, cellid: int):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT * FROM {self.tablename} WHERE id = {cellid}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data

    def update_value(self, data: list, id: int):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'UPDATE {self.tablename} SET dose="{data[0]}", iType="{data[1]}", interval="{data[2]}", date="{data[3]}", sValue="{data[4]}" WHERE id = {id}'
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()

    def avg_sugar_value(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT AVG(sValue) FROM {self.tablename}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data

    def max_sugar_value(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT MAX(sValue) FROM {self.tablename}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data

    def min_sugar_value(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT MIN(sValue) FROM {self.tablename}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data


if __name__ == '__main__':
    h = sugarDatabase()
    # h.delete_record(2)
    print(h.avg_sugar_value())
