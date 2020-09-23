# B
def boundary_layer_temperature_profiles(meta, mode, nc, ver, vocab_ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 100; dg = 30;
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   range_1d = dat.create_data_range(gates, dg)
   
   # Create altitude wrt to wgs84
   alt_1d = range_1d + 130 # adding the platform height
   
   # create 2d data
   data_2d = np.empty([len(ET), gates])
   flag_2d = np.empty([len(ET), gates])
   alt_2d = np.empty([len(ET), gates])
         
   for x in range(0, len(ET)):
      for y in range(0, gates):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x] 
         alt_2d[x,y] = alt_1d[y]
   
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.featureType = 'timeSeriesProfile'
   nc.product_version = ver
      
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   if '1' in vocab_ver:
      index = nc.createDimension('index', gates)
   else:
      altitude = nc.createDimension('altitude', gates) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)   

   # write specific variables
   if '1' in vocab_ver:
      v = nc.createVariable('altitude', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('altitude', np.float32, ('altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.standard_name = 'altitude'
   v.long_name = 'Geometric height above geoid (WGS84).'
   v.axis = 'Z'
   v.valid_min = np.float32(min(range_1d))
   v.valid_max = np.float32(max(range_1d))
   v.coordinates = 'latitude longitude'
   #write data
   if '1' in vocab_ver:
      v[:,:] = np.float32(alt_2d)
   else:
      v[:] = np.float32(alt_1d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('air_temperature', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('air_temperature', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'air_temperature'
   v.long_name = 'Air Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('qc_flag_surface_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_relative_humidity', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Relative Humidity'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_surface_pressure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Pressure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_precipitation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Precipitation'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_1_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 1 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_2_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 2 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_3_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 3 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_4_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 4 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_5_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_6_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_7_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 7 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_8_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 8 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_9_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 9 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_10_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 10 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_11_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 11 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_12_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 12 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_13_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 13 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_14_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 14 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_t_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of temperature receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_rh_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of moisture receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_2d, flag_2d     
            
def boundary_layer_thickness(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create data and flags
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver
   
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('atmosphere_boundary_layer_thickness', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.standard_name = 'atmosphere_boundary_layer_thickness'
   v.long_name = 'Atmospheric Boundary Layer Thickness'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_surface_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_relative_humidity', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Relative Humidity'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_surface_pressure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Pressure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_precipitation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Precipitation'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_1_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 1 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_2_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 2 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_3_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 3 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_4_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 4 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_5_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_6_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_7_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 7 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_8_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 8 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_9_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 9 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_10_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 10 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_11_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 11 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_12_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 12 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_13_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 13 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_14_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 14 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_t_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of temperature receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_rh_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of moisture receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d 
          
def brightness_temperature(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create data and flags
   [ET, DT, DoY] = dat.create_time(meta)   
   freq = 14;
   ff = np.empty([freq])
   for x in range(0,freq):
      ff[x] = x + 20
      
   [lat, lon] = dat.create_pos(ET, mode)   
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   data_2d = np.empty([len(ET), freq])
   flag_2d = np.empty([len(ET), freq])
         
   for x in range(0, len(ET)):
      for y in range(0, freq):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x] 
   
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver 
   
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   radiation_frequency = nc.createDimension('radiation_frequency', freq)
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('radiation_frequency', np.float32, ('radiation_frequency',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.standard_name = 'radiation_frequency'
   v.long_name = 'Receiver Channel Centre Frequency'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(ff)
   
   v = nc.createVariable('brightness_temperature', np.float32, ('time','radiation_frequency',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'brightness_temperature'
   v.long_name = 'Brightness Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'teim: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('atmospheric_attenuation', np.float32, ('time','radiation_frequency',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Atmospheric Attenuation'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'teim: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('qc_flag_surface_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_relative_humidity', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Relative Humidity'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_surface_pressure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Surface Pressure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_precipitation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Precipitation'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_1_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 1 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_2_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 2 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_3_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 3 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_4_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 4 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_5_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_6_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 5 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_7_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 7 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_8_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 8 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_9_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 9 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_10_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 10 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_11_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 11 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_12_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 12 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_13_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 13 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_channel_14_failure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Receiver channel 14 failure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_t_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of temperature receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_rh_receiver_temperature_stability', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Thermal stability of moisture receiver bank'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, ff, data_1d, flag_1d, data_2d, flag_2d 