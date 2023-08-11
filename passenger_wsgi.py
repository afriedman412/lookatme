import os,sys,os.path

errfile = open( '/home/dnpdata/error.log','a+')
os.close(sys.stderr.fileno())
os.dup2(errfile.fileno(), sys.stderr.fileno())

cwd = os.getcwd()
sys.path.append(cwd)
INTERP = "/home/dnpdata/dnpdata.com/public/venv"

#INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from app import app as application