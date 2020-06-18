import csv
import re


def get_data(file):
    with open(file, 'r') as file_read:
        os_manufacturer = re.match(r'^Изготовитель системы:\s*(.*)$', )
        # os_name =
        # os_id =
        # os_type =
