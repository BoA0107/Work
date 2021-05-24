# -*- coding:utf-8 -*-

from openpyxl import *


def basic(filename, sheetname):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    x = sheet.max_row
    y = sheet.max_column
    a = []

    for i in range(0, x):
        b = []
        for j in range(0, y):
            b.append(sheet.cell(i + 1, j + 1).value)
        a.append(b)
    print(a)


# basic("doc/release.xlsx", "links")


def info(filename, sheetname, max_line=0):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    x = sheet.max_row
    y = sheet.max_column
    infos = []
    title = []

    if max_line == 0:
        for j in range(0, y):
            title.append(sheet.cell(1, j + 1).value)
        infos.append(title)

        for i in range(1, x):
            content = []
            for j in range(0, y):
                content.append(sheet.cell(i + 1, j + 1).value)
            infos.append(content)
        return infos

    else:
        for j in range(0, y):
            title.append(sheet.cell(1, j + 1).value)
        infos.append(title)

        for i in range(x - max_line, x):
            content = []
            for j in range(0, y):
                content.append(sheet.cell(i + 1, j + 1).value)
            infos.append(content)
        return infos

#######################################################

def basic(filename, sheetname):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    x = sheet.max_row
    y = sheet.max_column
    a = []

    for i in range(0, x):
        b = []
        for j in range(0, y):
            b.append(sheet.cell(i + 1, j + 1).value)
        a.append(b)
    return a


def make_dct(lst):
    dct = {}
    for i in range(len(lst)):
        x, y = lst[i]
        if y == None:
            key = x
            dct[key] = {}
            for j in range(i + 1, len(lst)):
                x, y = lst[j]
                if y != None:
                    dct[key][x] = y
                else:
                    break
    return dct

# if __name__ == "__main__":
#     x = info(filename="doc/release.xlsx", sheetname="plan")
#     print(x)
