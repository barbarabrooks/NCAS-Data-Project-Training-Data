def global_attributes(nc, meta, ET, mode):
   from datetime import datetime
  
   for x in range(0,len(meta[:,0])):
      nc.setncattr(meta[x,0], meta[x,1])
   
   # write specific global attribute
   nc.last_revised_date = datetime.utcnow().isoformat()  
   nc.time_coverage_start = datetime.utcfromtimestamp(ET[0]).isoformat()
   nc.time_coverage_end = datetime.utcfromtimestamp(ET[len(ET)-1]).isoformat()
   if 'land' in mode:
      nc.deployment_mode = 'land'
      nc.platform_type = 'stationary_platform'
      nc.geospatial_bounds = '51.5733N -1.3147E'
   if 'sea' in mode:
      nc.deployment_mode = 'sea'
      nc.platform_type = 'moving_platform'   
      nc.geospatial_bounds = '50.1514N -11.1214E, 51.1514N -10.1214E'
   if 'air' in mode:
      nc.deployment_mode = 'air'
      nc.platform_type = 'moving_platform'
      nc.geospatial_bounds = '51.5733N -1.3147E, 52.5733N -0.3147E'
      
   del datetime
   
def global_attributes_sonde(nc, meta, ET, mode):
   from datetime import datetime
  
   for x in range(0,len(meta[:,0])):
      nc.setncattr(meta[x,0], meta[x,1])
   
   # write specific global attribute
   nc.last_revised_date = datetime.utcnow().isoformat()  
   nc.time_coverage_start = datetime.utcfromtimestamp(ET[0]).isoformat()
   nc.time_coverage_end = datetime.utcfromtimestamp(ET[len(ET)-1]).isoformat()
   nc.geospatial_bounds = '51.5733N -1.3147E'
   nc.featureType = 'trajectory'
   if 'land' in mode:
      nc.deployment_mode = 'land'
      nc.platform_type = 'stationary_platform'
      nc.platform = 'ral'
   if 'sea' in mode:
      nc.deployment_mode = 'sea'
      nc.platform_type = 'moving_platform'   
      nc.platform = 'ral-sea'      
   if 'air' in mode:
      nc.deployment_mode = 'air'
      nc.platform_type = 'moving_platform'
      nc.platform = 'ral-air'
      
   del datetime   
      
def dimensions(nc, ET, lat, lon):
   import numpy as np
   time = nc.createDimension('time', len(ET))
   if np.isscalar(lat):
      latitude = nc.createDimension('latitude', 1)
      longitude = nc.createDimension('longitude', 1)
   else:
      latitude = nc.createDimension('latitude', len(lat))
      longitude = nc.createDimension('longitude', len(lon)) 
      
   del np
   
def dimensions_sonde(nc, ET):
   time = nc.createDimension('time', len(ET))
   
def variables(nc, ET, DT, DoY, lat, lon, mode):
   import numpy as np
   
   #time
   v = nc.createVariable('time', np.float64, ('time',))
   #variable attributes
   v.units = 'seconds since 1970-01-01 00:00:00'
   v.standard_name = 'time'
   v.long_name = 'Time (seconds since 1970-01-01 00:00:00)'
   v.axis = 'T'
   v.valid_min = np.float64(min(ET))
   v.valid_max = np.float64(max(ET))
   v.calendar = 'standard'
   #write data
   v[:] = np.float64(ET)
   
   if mode == 'land':
      #lat
      v = nc.createVariable('latitude', np.float32, ('latitude',))
      #variable attributes
      v.units = 'degrees_north'
      v.standard_name = 'latitude'
      v.long_name = 'Latitude'
      #write data
      v[:] = np.float32(lat)
   
      #lon
      v = nc.createVariable('longitude', np.float32, ('longitude',))
      #variable attributes
      v.units = 'degrees_east'
      v.standard_name = 'longitude'
      v.long_name = 'Longitude'
      #write data
      v[:] = np.float32(lon)
   
   #doy
   v = nc.createVariable('day_of_year', np.float32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Day of Year'
   v.valid_min = np.float32(min(DoY))
   v.valid_max = np.float32(max(DoY))
   #write data
   v[:] = np.float32(DoY)
   
   #year
   v = nc.createVariable('year', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Year'
   v.valid_min = np.int32(min(DT[:,0]))
   v.valid_max = np.int32(max(DT[:,0])) 
   #write data
   v[:] = np.int32(DT[:,0])
   
   #month
   v = nc.createVariable('month', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Month'
   v.valid_min = np.int32(min(DT[:,1]))
   v.valid_max = np.int32(max(DT[:,1])) 
   #write data
   v[:] = np.int32(DT[:,1])
   
   #day
   v = nc.createVariable('day', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Day'
   v.valid_min = np.int32(min(DT[:,2]))
   v.valid_max = np.int32(max(DT[:,2]))
   #write data
   v[:] = np.int32(DT[:,2])
   
   #hour
   v = nc.createVariable('hour', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Hour'
   v.valid_min = np.int32(min(DT[:,3]))
   v.valid_max = np.int32(max(DT[:,3])) 
   #write data
   v[:] = np.int32(DT[:,3])
   
   #minute
   v = nc.createVariable('minute', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Minute'
   v.valid_min = np.int32(min(DT[:,4]))
   v.valid_max = np.int32(max(DT[:,4]))  
   #write data
   v[:] = np.int32(DT[:,4])
   
   #second
   v = nc.createVariable('second', np.float32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Second'
   v.valid_min = np.float32(min(DT[:,5]))
   v.valid_max = np.float32(max(DT[:,5])) 
   #write data
   v[:] = np.float32(DT[:,5])
   
   if ((mode == 'air') or ((mode == 'sea'))):
      import TData_data as dat
      
      [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
      
      v = nc.createVariable('latitude', np.float32, ('latitude',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degrees_north'
      v.standard_name = 'latitude'
      v.long_name = 'Latitude'
      v.axis = 'Y'
      v.valid_min = np.float32(min(lat))
      v.valid_max = np.float32(max(lat))
      v.cell_methods = 'time: mean'
      #write data
      v[:] = np.float32(lat)
      
      v = nc.createVariable('longitude', np.float32, ('longitude',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degrees_east'
      v.standard_name = 'longitude'
      v.long_name = 'Longitude'
      v.axis = 'X'
      v.valid_min = np.float32(min(lon))
      v.valid_max = np.float32(max(lon))
      v.cell_methods = 'time: mean'
      #write data
      v[:] = np.float32(lon)
      
      v = nc.createVariable('platform_speed_wrt_ground', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'm s-1'
      v.standard_name = 'platform_speed_wrt_ground'
      v.long_name = 'Platform speed with respect to ground'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('platform_course', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.standard_name = 'platform_course'
      v.long_name = 'Direction in which the platform is travelling'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('platform_orientation', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.standard_name = 'platform_orientation'
      v.long_name = 'Direction in which "front" of platform is pointing'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_pitch_angle', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Pitch Angle'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_pitch_rate', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree s-1'
      v.long_name = 'Instrument Pitch Angle Rate of Change'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_pitch_minimum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Pitch Angle Minimum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: minimum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_pitch_maximum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Pitch Angle Maximum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: maximum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_pitch_standard_deviation', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Pitch Standard Deviation'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: standard_deviation'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_roll_angle', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Roll Angle'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_roll_rate', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree s-1'
      v.long_name = 'Instrument Roll Angle Rate of Change'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_roll_minimum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Roll Angle Minimum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: minimum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_roll_maximum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Roll Angle Maximum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: maximum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_roll_standard_deviation', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Roll Standard Deviation'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: standard_deviation'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_yaw_angle', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Yaw Angle'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_yaw_rate', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree s-1'
      v.long_name = 'Instrument Yaw Angle Rate of Change'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_yaw_minimum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Yaw Angle Minimum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: minimum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_yaw_maximum', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Yaw Angle Maximum'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: maximum'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('instrument_yaw_standard_deviation', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'degree'
      v.long_name = 'Instrument Yaw Standard Deviation'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: standard_deviation'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)      
      
      del dat
   
   if mode == 'air':
      v = nc.createVariable('platform_speed_wrt_air', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'm s-1'
      v.standard_name = 'platform_speed_wrt_air'
      v.long_name = 'Platform speed with respect to air'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
      
      v = nc.createVariable('altitude', np.float32, ('time',), fill_value=-1.00e+20)
      #variable attributes
      v.units = 'm'
      v.standard_name = 'altitude'
      v.long_name = 'Geometric height above geoid (WGS84).'
      v.axis = 'Z'
      v.valid_min = np.float32(min_dat)
      v.valid_max = np.float32(max_dat)
      v.cell_methods = 'time: mean'
      v.coordinates = 'latitude longitude'
      #write data
      v[:] = np.float32(data_1d)
   
   del np
   
def variables_sonde(nc, ET, DT, DoY):
   import numpy as np
   
   #time
   v = nc.createVariable('time', np.float64, ('time',))
   #variable attributes
   v.units = 'v since 1970-01-01 00:00:00'
   v.standard_name = 'time'
   v.long_name = 'Time (v since 1970-01-01) 00:00:00'
   v.axis = 'T'
   v.valid_min = np.float64(min(ET))
   v.valid_max = np.float64(max(ET))
   v.calendar = 'standard'
   #write data
   v[:] = np.float64(ET)
   
   #doy
   v = nc.createVariable('day_of_year', np.float32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Day of Year'
   v.valid_min = np.float32(min(DoY))
   v.valid_max = np.float32(max(DoY))
   #write data
   v[:] = np.float32(DoY)
   
   #year
   v = nc.createVariable('year', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Year'
   v.valid_min = np.int32(min(DT[:,0]))
   v.valid_max = np.int32(max(DT[:,0])) 
   #write data
   v[:] = np.int32(DT[:,0])
   
   #month
   v = nc.createVariable('month', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Month'
   v.valid_min = np.int32(min(DT[:,1]))
   v.valid_max = np.int32(max(DT[:,1])) 
   #write data
   v[:] = np.int32(DT[:,1])
   
   #day
   v = nc.createVariable('day', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Day'
   v.valid_min = np.int32(min(DT[:,2]))
   v.valid_max = np.int32(max(DT[:,2]))
   #write data
   v[:] = np.int32(DT[:,2])
   
   #hour
   v = nc.createVariable('hour', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Hour'
   v.valid_min = np.int32(min(DT[:,3]))
   v.valid_max = np.int32(max(DT[:,3])) 
   #write data
   v[:] = np.int32(DT[:,3])
   
   #minute
   v = nc.createVariable('minute', np.int32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Minute'
   v.valid_min = np.int32(min(DT[:,4]))
   v.valid_max = np.int32(max(DT[:,4]))  
   #write data
   v[:] = np.int32(DT[:,4])
   
   #second
   v = nc.createVariable('second', np.float32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Second'
   v.valid_min = np.float32(min(DT[:,5]))
   v.valid_max = np.float32(max(DT[:,5])) 
   #write data
   v[:] = np.float32(DT[:,5])