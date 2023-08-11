import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
INTERP = "/home/dnpdata/dnpdata.com/public/dnpdata/venv"

#INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from app import app as application