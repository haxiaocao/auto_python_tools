# https://automatetheboringstuff.com/chapter14/

import csv


def Read_file_1():
    example_csv = open('example.csv')
    example_reader = csv.reader(example_csv)
    for row in example_reader:
        print 'Row #{} Value: {}'.format(example_reader.line_num, row)
    example_csv.close()


def Read_file_2():
    # The Reader object can be looped over only once. To reread the CSV file, you must call csv.reader to create a Reader object.
    example_csv = open('example.csv')
    example_reader = csv.reader(example_csv)
    exampleData = list(example_reader)
    print exampleData
    example_csv.close()


def write_file():
    # this will cause the extral blank line
    output_file = open('output.csv', 'w')
    # output_file=open('output.csv','a')
    # output_writer=csv.writer(output_file)
    output_writer = csv.writer(
        output_file, delimiter='\t', lineterminator='\n')
    output_writer.writerow(['spam', 'eggs', 'bacon'])
    output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
    output_writer.writerow([1, 2, 3556, 22])
    output_file.close()

# https://stackoverflow.com/questions/29840849/writing-a-csv-file-in-python-that-works-for-both-python-2-7-and-python-3-3-in


def write_by_header():
    items = [{'header1': 'value', 'header2': 'value2'},
             {'header1': 'blah1', 'header2': 'blah2'},
             {'header1': 'row3', 'header2': 'row32'}]
    import sys
    if sys.version_info[0] == 2:
        access = 'wb'
        kwargs = {}
    else:
        access = 'wt'
        kwargs = {'newline': ''}
    with open('output.csv', access, **kwargs) as f:
        writer = csv.DictWriter(f, ['header1', 'header2'])
        writer.writeheader()
        for item in items:
            writer.writerow(item)

# Read_file_1()
# Read_file_2()
# write_file()
# write_by_header()
# TODO: have a good night to see it.
