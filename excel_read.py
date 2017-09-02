# -*- coding: utf-8 -*-
# reference:https://automatetheboringstuff.com/chapter12/

import openpyxl

wb = openpyxl.load_workbook(
    r'G:\MyCode\Python\auto-python-tools\automate_online-materials\censuspopdata.xlsx')
# the two dic key is :STATE
sheet = wb.active
trace_count_dic = {}
pop_count_dict = {}
for row in sheet.rows:
    # ignore the column header row
    # another way to do : for row in range(2, sheet.max_row + 1)
    if row[0].row == 1:
        continue
    trace = row[0].value
    state = row[1].value
    country = row[2].value
    popnum = row[3].value
    if state not in trace_count_dic:
        trace_count_dic[state] = 0
    if state not in pop_count_dict:
        pop_count_dict[state] = 0

    trace_count_dic[state] += 1
    pop_count_dict[state] += popnum

for i in trace_count_dic:
    print 'state Trace:{},trace count :{}'.format(i, trace_count_dic[i])
for i in pop_count_dict:
    print "state:{}, population:{}".format(i, pop_count_dict[i])
print 'All the state Count is:' + str(len(trace_count_dic))
