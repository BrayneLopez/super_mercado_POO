from datetime import datetime

def converter_format(date_format):
    new_date_format = datetime.strptime(date_format, '%d/%m/%Y')
    return new_date_format
 