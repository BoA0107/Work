from flask import *
from read_doc import *
from func.info import *

# deploy_info
plan_info = read_doc(filename=F_home, sheetname=Home_deploy_plan, max_line=16)

# links
links = read_doc(filename=F_home, sheetname=Home_links)
links_dct = make_dct(links)

# career_level
career_level = read_doc(filename=F_home, sheetname=Home_level_info)

# other
others = read_singel(filename=F_home, sheetname=Home_others)
