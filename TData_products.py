import os
from datetime import datetime

from netCDF4 import Dataset


def create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode):
   
   try:
      # create nc file
      from netCDF4 import Dataset
      dout = 'Data'
      f1 = nm # instrument name
      if mode == 'land':
         f2 = 'ral' # platform name
      if mode == 'sea':
         f2 = 'ral-sea' # platform name   
      if mode == 'air':
         f2 = 'ral-air' # platform name      
      f3 = '29001225' # date
      f4 = dp # data product
      f5 = 'v' + ver # version number
      f6 = '.nc'
      
      if ((len(opt1)<1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+f5+f6         
      if ((len(opt1)>1) and (len(opt2)<1) and (len(opt3)<1)):
         fn = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)<1)):
         fn = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+f5+f6
      if ((len(opt1)>1) and (len(opt2)>1) and (len(opt3)>1)):
         fn = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt1+chr(95)+opt2+chr(95)+opt3+chr(95)+f5+f6

      output = os.path.join(dout, fn)
      nc = Dataset(output, "w", format="NETCDF4_CLASSIC") 
   except:
      # exit if problem encountered
      err_msg = f'Unable to create: {output} . This program will terminate'
      print(err_msg)
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + err_msg + '\n')
      g.close()
      exit()
      
      del Dataset, datetime

   return nc
