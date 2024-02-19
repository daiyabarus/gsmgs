import datetime
import csv
import os


class UtilFunc:
    @staticmethod
    def get_current_datetime():
        now = datetime.datetime.now()
        return now.strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def get_current_datetime_MMDDYYYY():
        now = datetime.datetime.now()
        return now.strftime("%m/%d/%Y")

    @staticmethod
    def txtfile_to_list(txtpath: str) -> list:
        reader_line = []

        with open(txtpath, "r") as fl:
            liner = fl.readlines()

            for line in liner:
                cline = line.rstrip()

                reader_line.append(cline)

        return reader_line

    @staticmethod
    def csv_to_list(csv_file: str, delimiter: str = ";") -> list:

        if not os.path.exists(csv_file):
            return [f"{csv_file} File not Exists!"]

        list_of_mos: list = []
        with open(csv_file) as f:
            file_reader = csv.reader(f, delimiter=delimiter)
            for row in file_reader:
                if len(row) > 0:
                    list_of_mos.append(row)

        return list_of_mos
