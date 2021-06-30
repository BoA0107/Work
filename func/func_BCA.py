from flask import *
from read_doc import *
from func.info import *

# UAT on BC
UAT_BC = read_doc(filename=F_BCA,sheetname=BCA_UAT_BC)
BCA_02 = read_doc(filename=F_BCA,sheetname=BCA_2)
BCA_01 = read_txt(BCA_SQL)