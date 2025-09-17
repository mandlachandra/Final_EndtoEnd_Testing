# In Michaels, data may come from CSV, Excel, Database, or API.
# Instead of hardcoding, you can abstract data source:

from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def read_data(self):
        pass


class ExcelData(DataSource):
    def read_data(self):
        print("Read data from Excel")


class DBData(DataSource):
    def read_data(self):
        print("Read data from Database")
#Your test doesn’t care where data comes from — Excel or DB. It only calls read_data().