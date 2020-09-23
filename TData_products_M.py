# M
def mean_co2_h2o(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
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
   v = nc.createVariable('air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'air_temperature'
   v.long_name = 'Air Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Divergence of Air Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('air_pressure', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hPa'
   v.standard_name = 'air_pressure'
   v.long_name = 'Air Pressure'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_air_pressure', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hPa'
   v.long_name = 'Divergence of Air Pressure'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mmol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_mole_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mmol m-3'
   v.long_name = 'Divergence of mole concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mmol m-3'
   v.standard_name = 'mole_concentration_of_water_vapor_in_air'
   v.long_name = 'Mole Concentration of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_mole_concentration_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mmol m-3'
   v.long_name = 'Divergence of mole concentration of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('specific_humidity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg kg-1'
   v.standard_name = 'specific_humidity'
   v.long_name = 'Specific_humidity (Q)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_specific_humidity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg kg-1'
   v.long_name = 'Divergence of Specific Humidity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('humidity_mixing_ratio', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.standard_name = 'humidity_mixing_ratio'
   v.long_name = 'Humidity Mixing Ratio'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('divergence_of_humidity_mixing_ratio', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Divergence of Humidity Mixing Ratio'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_pressure', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Pressure'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_co2_concentration', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Carbon Dioxide concentration'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_h2o_concentration', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Water Vapor concentration'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d            
         
def mean_winds(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
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
   
   v = nc.createVariable('wind_speed', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Mean Wind Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_speed_of_gust', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed_of_gust'
   v.long_name = 'Maximum Wind Speed Observed in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_from_direction', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'wind_from_direction'
   v.long_name = 'Wind From Direction'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_speed_of_gust_from_direction', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Direction of Maximum Wind Speed Observed in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('eastward_wind', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'eastward_wind'
   v.long_name = 'Eastward Wind Component (V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('northward_wind', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'northward_wind'
   v.long_name = 'Northward Wind Component (V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('upward_air_velocity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'upward_air_velocity'
   v.long_name = 'Upward Air Velocity Component (W)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('divergence_of_wind', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'divergence_of_wind'
   v.long_name = 'Divergence of Horizontal Winds Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('divergence_of_wind_from_direction', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Divergence of Wind from Direction'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('divergence_of_eastward_wind', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Eastward Wind Component (Sigma U)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('divergence_of_northward_wind', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Northward Wind Component (Sigma V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('divergence_of_upward_air_velocity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Upward Air Velocity (Sigma W)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 
 
   v = nc.createVariable('sonic_air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Air Temperature Retrieved from Sonic Anemometry'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 
   
   v = nc.createVariable('divergence_of_sonic_air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Divergence of Air Temperature Retrieved from Sonic Anemometry'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('qc_flag_sonic_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Sonic Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_wind_speed', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Wind Speed'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_wind_direction', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Wind Direction'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_wind_component_eastward', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Eastward Wind Component (U)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_wind_component_northward', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Northward Wind Component (V)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_wind_component_upward_air_velocity', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Upward Air Velocity Component (W)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d   
         
def mean_winds_profile(meta, mode, nc, ver, vocab_ver):
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
      v = nc.createVariable('wind_speed', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('wind_speed', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Mean Wind Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('wind_speed_of_gust', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('wind_speed_of_gust', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed_of_gust'
   v.long_name = 'Maximum Wind Speed Observed in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('wind_from_direction', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('wind_from_direction', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'wind_from_direction'
   v.long_name = 'Wind From Direction'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('wind_speed_of_gust_from_direction', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('wind_speed_of_gust_from_direction', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Direction of Maximum Wind Speed Observed in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('eastward_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('eastward_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'eastward_wind'
   v.long_name = 'Eastward Wind Component (V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)

   if '1' in vocab_ver:
      v = nc.createVariable('northward_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('northward_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'northward_wind'
   v.long_name = 'Northward Wind Component (V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)

   if '1' in vocab_ver:
      v = nc.createVariable('upward_air_velocity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('upward_air_velocity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'upward_air_velocity'
   v.long_name = 'Upward Air Velocity Component (W)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('divergence_of_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('divergence_of_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'divergence_of_wind'
   v.long_name = 'Divergence of Horizontal Winds Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('divergence_of_wind_from_direction', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('divergence_of_wind_from_direction', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Divergence of Wind from Direction'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('divergence_of_eastward_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('divergence_of_eastward_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Eastward Wind Component (Sigma U)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('divergence_of_northward_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('divergence_of_northward_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Northward Wind Component (Sigma V)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)

   if '1' in vocab_ver:
      v = nc.createVariable('divergence_of_upward_air_velocity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('divergence_of_upward_air_velocity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Divergence of Upward Air Velocity (Sigma W)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d) 
 
   if '1' in vocab_ver:
      v = nc.createVariable('qc_flag', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('qc_flag', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_2d, flag_2d
         
def moisture_profiles(meta, mode, nc, ver, vocab_ver):
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
      v = nc.createVariable('relative_humidity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('relative_humidity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.standard_name = 'relative_humidity'
   v.long_name = 'Relative Humidity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d) 
   
   if '1' in vocab_ver:
      v = nc.createVariable('absolute_humidity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('absolute_humidity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'g m-3'
   v.long_name = 'Absolute Humidity'
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