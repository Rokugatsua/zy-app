#import scr.dacon as dacon

import os
import csv

class Handler:
    def io(self):
        pass

class Csv(Handler):
    def __init__(self, csv_dir_file):
        self.csv_dir_file =  csv_dir_file

    def open_file(self, limiter):
        data_raw = []
        with open(self.csv_dir_file) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=limiter)
            for rows in csv_reader:
                data_raw.append(rows)
        return data_raw

class Efaktur_Export:
    def __init__(self, csv_dir_file):
        self.csv_dir_file = csv_dir_file
        self.__open_file()

    def __open_file(self):
        csv_h = Csv(self.csv_dir_file)
        self.datali = csv_h.open_file(limiter=",")

    def filter_data(self, datali):
        fk_list = [li for li in datali if "FK" in li]
        enofa_list = [li[3] for li in fk_list if li[3] != "NOMOR_FAKTUR"]
        return enofa_list

    def get(self):
        ixdata = self.filter_data(self.datali)
        return ixdata

if __name__ == "__main__":
    dir = os.getcwd()
    csv_name ='big2019.csv'
    csv_dir = os.path.join(dir,"_file","csv",csv_name)
    ee = Efaktur_Export(csv_dir)
    datali = ee.get()
