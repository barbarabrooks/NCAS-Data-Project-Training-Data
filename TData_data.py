def create_time(meta):
   import time
   import calendar
   import numpy as np
   
   # start time 
   tt_st = time.strptime('2900-12-25T00:00:00','%Y-%m-%dT%H:%M:%S')
   ep_st = calendar.timegm(tt_st) 
   
   # sample interval
   for x in range (0, len(meta[:,0])):
      if 'sampling_interval' in meta[x,0]:
         tp = meta[x,1]
   
   # value spearated from units by white space
   x = int(tp[0:(tp.find(' '))]);
   
   # create time axis
   if 'hour' in tp:
      lt = int(24/x)
      ET = np.empty([lt])
      DT = np.empty([lt,6])
      DOY = np.empty([lt])
      # time increment in seconds
      dt = x * 60 * 60
      for x in range(0, lt):
         ET[x] = ep_st + (dt * x)    
         tt = time.gmtime(ET[x])
         DT[x,:] = tt[0:6]
         DOY[x] = float(tt[7])+((float(tt[3])+float(tt[4]/(60))+float(tt[5]/(60*60)))/24)

   if 'min' in tp:
      lt = int((24 * 60)/x)
      ET = np.empty([lt])
      DT = np.empty([lt,6])
      DOY = np.empty([lt])
      # time increment in seconds
      dt = x * 60      
      for x in range(0, lt):
         ET[x] = ep_st + (dt * x)    
         tt = time.gmtime(ET[x])
         DT[x,:] = tt[0:6]
         DOY[x] = float(tt[7])+((float(tt[3])+float(tt[4]/(60))+float(tt[5]/(60*60)))/24)
   else:
      lt = int((24 * 60 * 60)/x)
      ET = np.empty([lt])
      DT = np.empty([lt,6])
      DOY = np.empty([lt])
      # time increment in seconds
      dt = x
      for x in range(0, lt):
         ET[x] = ep_st + (dt * x)    
         tt = time.gmtime(ET[x])
         DT[x,:] = tt[0:6]
         DOY[x] = float(tt[7])+((float(tt[3])+float(tt[4]/(60))+float(tt[5]/(60*60)))/24)
  
   del time, calendar, np    
   
   return ET, DT, DOY
   
def create_data_flag(ET):
   # data_1d is a sinusoid
   # 1 cycle per day
   # amplitude 0 to 1
   import numpy as np
   
   Time = np.empty([len(ET)]) 
   dt = (2 * np.pi)/len(ET)
   for x in range(0, len(ET)):
      Time[x] = dt * x 
   
   amp = np.sin(Time)
   data = (amp + 1) / 2
   flag = np.ones([len(ET)])  
   for x in range(0, len(amp)):
      if amp[x] < -0.85:
         flag[x] = 2
      if amp[x] > 0.85:
         flag[x] = 3
      if amp[x] == 0:
         flag[x] = 4    
   
   #find min and max of data with flag 1
   XX = data
   np.putmask(XX, flag != 1, np.nan)
   min_dat = np.nanmin(XX)
   max_dat = np.nanmax(XX)
   
   del np

   return data, flag, min_dat, max_dat
      
def create_data_range(gates, dg):   
   # data_alt is altidude 
   # gates number of gates
   # dalt gate length
   import numpy as np
   
   data = np.empty([gates])
   for x in range(0, gates):
      data[x] = dg + (dg * x)
      
   del np

   return data
   
def create_pos(ET, mode): 
   import numpy as np
   
   if 'land' in mode:
      lat = 51.5733; lon = -1.3147
   if 'air' in mode:
      lat = np.empty([len(ET)])
      lon = np.empty([len(ET)])
      lat1 = 51.5733; lon1 = -1.3147
      lat2 = 52.5733; lon2 = -0.3147
      for x in range(0, len(ET)):
         lat[x] = lat1 + ((lat2-lat1)/len(ET)) * x
         lon[x] = lon1 + ((lon2-lon1)/len(ET)) * x
   if 'sea' in mode:
      lat = np.empty([len(ET)])
      lon = np.empty([len(ET)])
      lat1 = 50.1514; lon1 = -11.0717
      lat2 = 51.1514; lon2 = -10.0717
      for x in range(0, len(ET)):
         lat[x] = lat1 + ((lat2-lat1)/len(ET)) * x
         lon[x] = lon1 + ((lon2-lon1)/len(ET)) * x
   
   del np
   
   return lat, lon
   