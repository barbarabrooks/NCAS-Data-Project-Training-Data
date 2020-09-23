# R
def radiation(meta, mode, nc, ver):
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
   v = nc.createVariable('downwelling_longwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'downwelling_longwave_flux_in_air'
   v.long_name = 'Downwelling Longwave Radiation in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)   
   
   v = nc.createVariable('upwelling_longwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'upwelling_longwave_flux_in_air'
   v.long_name = 'Upwelling Longwave Radiation in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('downwelling_shortwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'downwelling_shortwave_flux_in_air'
   v.long_name = 'Downwelling Shortwave Radiation in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 
   
   v = nc.createVariable('upwelling_shortwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'upwelling_shortwave_flux_in_air'
   v.long_name = 'Upwelling Shortwave Radiation in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('radiometer_body_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Radiometer Body Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('qc_flag_upwelling_shortwave', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Upwelling shortwave'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_downwelling_shortwave', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Downwelling shortwave'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_upwelling_longwave', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Upwelling longwave'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_downwelling_longwave', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Downwelling longwave'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_body_temperature', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Body Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_cleaning', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Sensor Cleaning'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d    
         
def radon_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_radon_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_radon_in_air'
   v.long_name = 'Mole Fraction of Radon in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'Ra'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_radon_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_radon_in_air'
   v.long_name = 'Mass Fraction of Radon in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'Ra'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_radon_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_radon_in_air'
   v.long_name = 'Mole Concentration of Radon in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'Ra'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_radon_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_radon_in_air'
   v.long_name = 'Mass Concentration of Radon in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'Ra'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag', np.int8, ('time',))
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
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d          
         
def rain_lwc_velocity_reflectivity(meta, mode, nc, ver, vocab_ver):
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
      v = nc.createVariable('rainfall_rate', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('rainfall_rate', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.standard_name = 'rainfall_rate'
   v.long_name = 'Rainfall Rate'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d) 
   
   if '1' in vocab_ver:
      v = nc.createVariable('rain_liquid_water_content', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('rain_liquid_water_content', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'g m-3'
   v.long_name = 'Rain Liquid Water Content'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)  

   if '1' in vocab_ver:
      v = nc.createVariable('rainfall_velocity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('rainfall_velocity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Rainfall Velocity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)   
   
   if '1' in vocab_ver:
      v = nc.createVariable('radar_reflectivity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('radar_reflectivity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dBZ'
   v.long_name = 'Radar Reflectivity (Z)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('attenuated_radar_reflectivity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('attenuated_radar_reflectivity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dBZ'
   v.long_name = 'Attenuated Radar Reflectivity (z)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('path_integrated_attenuation', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('path_integrated_attenuation', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Path Integrated Attenuation'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in vocab_ver:
      v = nc.createVariable('qc_flag', np.int8, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag', np.int8, ('time', 'altitude',))
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