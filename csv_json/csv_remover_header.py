# https://automatetheboringstuff.com/chapter14/
import csv


source = 'output.csv'
dest = 'output_1.csv'

d = open(dest, 'wb')
d_writer = csv.writer(d)
with open(source) as s:
    s_reader = csv.reader(s)
    for row in s_reader:
        if s_reader.line_num != 1:
            d_writer.writerow(row)

d.close()
