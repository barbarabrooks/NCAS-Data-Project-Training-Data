# S
def sf6_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_sulfur_hexafluoride_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.long_name = 'Mole Fraction of Sulphur Hexafluoride in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SF6'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_sulfur_hexafluoride_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.long_name = 'Mass Fraction of Sulphur Hexafluoride in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SF6'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_sulfur_hexafluoride_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.long_name = 'Mole Concentration of Sulphur Hexafluoride in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SF6'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_sulfur_hexafluoride_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.long_name = 'Mass Concentration of Sulphur Hexafluoride in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SF6'
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
         
def size_concentration_spectra(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 100; dg = 30;
   bins = 32; db = 1
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   range_1d = dat.create_data_range(gates, dg)
   
   # Create altitude wrt to wgs84
   alt_1d = range_1d + 130 # adding the platform height
   
   # create 2d data
   alt_2d = np.empty([len(ET), gates])
         
   # create 3d data
   data_3d = np.empty([len(ET), gates, bins])
   flag_3d = np.empty([len(ET), gates, bins])
         
   for x in range(0, len(ET)):
      for y in range(0, gates):
         alt_2d[x,y] = alt_1d[y]
         for z in range(0, bins):
            data_3d[x, y, z] = data_1d[x]
            flag_3d[x, y, z] = flag_1d[x]

   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.featureType = 'timeSeriesProfile'
   nc.product_version = ver
      
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   index_bin = nc.createDimension('index_bin', bins)
   if '1' in ver:
      index_range = nc.createDimension('index_range', gates)
   else:
      altitude = nc.createDimension('altitude', gates) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)  

   if '1' in ver:
      v = nc.createVariable('altitude', np.float32, ('time', 'index_range',), fill_value=-1.00e+20)
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
   if '1' in ver:
      v[:,:] = np.float32(alt_2d)
   else:
      v[:] = np.float32(alt_1d)  

   if '1' in ver:
      v = nc.createVariable('spectral_reflectivity', np.float32, ('time', 'index_range', 'index_bin',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('spectral_reflectivity', np.float32, ('time', 'altitude', 'index_bin',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Spectral Reflectivity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:,:] = np.float32(data_3d)  

   if '1' in ver:
      v = nc.createVariable('rain_drop_diameter', np.float32, ('time', 'index_range', 'index_bin',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('rain_drop_diameter', np.float32, ('time', 'altitude', 'index_bin',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.long_name = 'Rain Drop Diameter'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:,:] = np.float32(data_3d)  

   if '1' in ver:
      v = nc.createVariable('drop_size_distribution', np.float32, ('time', 'index_range', 'index_bin',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('drop_size_distribution', np.float32, ('time', 'altitude', 'index_bin',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-3 mm-1'
   v.long_name = 'Rain Drop Diameter'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:,:] = np.float32(data_3d)   
   
   if '1' in ver:
      v = nc.createVariable('qc_flag', np.int8, ('time', 'index_range', 'index_bin',))
   else:
      v = nc.createVariable('qc_flag', np.int8, ('time', 'altitude', 'index_bin',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Mean Winds'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:,:] = np.int8(flag_3d)

   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_3d, flag_3d     
         
def snr_winds(meta, mode, nc, ver):
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
   if '1' in ver:
      index = nc.createDimension('index', gates)
   else:
      altitude = nc.createDimension('altitude', gates) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('time_minutes_since_start_of_day', np.float32, ('time',))
   #variable attributes
   v.units = '1'
   v.long_name = 'Time in Minutes Since Start of Day'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('size_of_gate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.long_name = 'Size of Gate.'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
    
   if '1' in ver:
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
   if '1' in ver:
      v[:,:] = np.float32(alt_2d)
   else:
      v[:] = np.float32(alt_1d)
   
   if '1' in ver:
      v = nc.createVariable('wind_speed', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('wind_speed', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Wind Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
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
   
   if '1' in ver:
      v = nc.createVariable('eastward_wind', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('eastward_wind', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'eastward_wind'
   v.long_name = 'Eastward Wind Component (U)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
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
   
   if '1' in ver:
      v = nc.createVariable('upward_air_velocity', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('upward_air_velocity', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'upward_air_velocity'
   v.long_name = 'Upward Air Velocity (W)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_1', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_1', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Signal to Noise Ratio of beam 1 (back panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_2', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_2', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Signal to Noise Ratio of beam 2 (side panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_3', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('signal_to_noise_ratio_of_beam_3', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Signal to Noise Ratio of beam 3 (vertical beam from centre panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('signal_to_noise_ratio_minimum', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('signal_to_noise_ratio_minimum', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.long_name = 'Minimum Signal to Noise Ratio of the three beams'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('spectral_width_of_beam_1', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('spectral_width_of_beam_1', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Spectral Width of beam 1 (back panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('spectral_width_of_beam_2', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('spectral_width_of_beam_2', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Spectral Width of beam 2 (side panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('spectral_width_of_beam_3', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('spectral_width_of_beam_3', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Spectral Width of beam 3 (vertical beam from centre panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: standard_deviation'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('skew_of_beam_1', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('skew_of_beam_1', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Skew of beam 1 (back panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: skew'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('skew_of_beam_2', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('skew_of_beam_2', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Skew of beam 2 (side panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: skew'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('skew_of_beam_3', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('skew_of_beam_3', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Skew beam 3 (vertical beam from centre panel)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: skew'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
    
   if '1' in ver:
      v = nc.createVariable('qc_flag_wind', np.int8, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_wind', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Mean Winds'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_beam_1', np.int8, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_beam_1', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: SNR Beam 1 (back panel)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_beam_2', np.int8, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_beam_2', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: SNR Beam 2 (side panel)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_beam_3', np.int8, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_beam_3', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: SNR Beam 3 (vertical beam from centre panel)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
         
   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_2d, flag_2d         
         
def so2_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_sulfur_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_sulfur_dioxide_in_air'
   v.long_name = 'Mole Fraction of Sulphur Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_sulfur_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_sulfur_dioxide_in_air'
   v.long_name = 'Mass Fraction of Sulphur Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_sulfur_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_sulfur_dioxide_in_air'
   v.long_name = 'Mole Concentration of Sulphur Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_sulfur_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_sulfur_dioxide_in_air'
   v.long_name = 'Mass Concentration of Sulphur Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'SO2'
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
         
def soil(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 3; dg = 1;
   
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   # create 2d data
   data_2d = np.empty([len(ET), gates])
   flag_2d = np.empty([len(ET), gates])
         
   for x in range(0, len(ET)):
      for y in range(0, gates):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x] 

   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver
      
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   index = nc.createDimension('index', gates)
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('downward_heat_flux_in_soil', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'downward_heat_flux_in_soil'
   v.long_name = 'Downward Heat Flux in Soil'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('soil_temperature', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'soil_temperature'
   v.long_name = 'Soil Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('soil_water_potential', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kPa'
   v.long_name = 'Soil Water Potential'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('qc_flag_soil_heat_flux', np.int8, ('time', 'index',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Soil Water Potential'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   v = nc.createVariable('qc_flag_soil_temperature', np.int8, ('time', 'index',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Soil Temperature'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   v = nc.createVariable('qc_flag_soil_water_potential', np.int8, ('time', 'index',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Soil Water Potential'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   del dat, com, np, data_1d, flag_1d, data_2d, flag_2d
          
      
def solar_actinic_flux(meta, mode, nc, ver):
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
   v = nc.createVariable('solar_actinic_flux', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm-2 s-1 nm-1'
   v.long_name = 'Solar Actinic Flux (280–420 nm)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)   
   
   v = nc.createVariable('photolysis_frequencies_jno2', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(NO(2))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jo1d', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(O(1))(D))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jhcho', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(HCHO))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jhono', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(HONO))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
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

def sonde(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   [ET, DT, DoY] = dat.create_time(meta)
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   # write common global attrib 
   com.global_attributes_sonde(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver
      
   # write common dimensions
   com.dimensions_sonde(nc, ET)
   
   # write specific dimensions
   
   # write common variables
   com.variables_sonde(nc, ET, DT, DoY)
   
   # write specific variables
   v = nc.createVariable('altitude', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.standard_name = 'altitude'
   v.long_name = 'Geometric height above geoid (WGS 84).'
   v.axis = 'Z'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('latitude', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degrees_north'
   v.standard_name = 'latitude'
   v.long_name = 'Latitude'
   v.axis = 'Y'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('longitude', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degrees_east'
   v.standard_name = 'longitude'
   v.long_name = 'Longitude'
   v.axis = 'X'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('air_pressure', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hPa'
   v.standard_name = 'air_pressure'
   v.long_name = 'Air Pressure'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d) 
   
   v = nc.createVariable('air_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'air_temperature'
   v.long_name = 'Air Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('relative_humidity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.standard_name = 'relative_humidity'
   v.long_name = 'Relative Humidity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_speed', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Wind Speed'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_from_direction', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'wind_from_direction'
   v.long_name = 'Wind From Direction'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('upward_balloon_velocity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.long_name = 'Balloon Ascent Rate'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('elapsed_time', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's'
   v.long_name = 'Elapsed Time'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude altitude'
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

def stability_indices(meta, mode, nc, ver):
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
   v = nc.createVariable('atmosphere_stability_lifted_index', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Atmosphere Stability Lifted Index (LI)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 

   v = nc.createVariable('modified_atmosphere_stability_k_index', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Modified Atmosphere Stability K Index (KOI)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('atmosphere_stability_total_totals_index', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'atmosphere_stability_total_totals_index'
   v.long_name = 'Atmosphere Stability Total Totals Index (TTI) '
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('atmosphere_stability_k_index', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'atmosphere_stability_k_index'
   v.long_name = 'Atmosphere Stability K Index (KI)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('atmosphere_stability_showalter_index', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'atmosphere_stability_showalter_index'
   v.long_name = 'Atmosphere Stability Showalter Index (SI)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('atmosphere_convective_available_potential_energy', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'J kg-1'
   v.standard_name = 'atmosphere_convective_available_potential_energy'
   v.long_name = 'Atmosphere Convective Available Potential Energy (CAPE)'
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
       
def surface_met(meta, mode, nc, ver):
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
   
   v = nc.createVariable('relative_humidity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.standard_name = 'relative_humidity'
   v.long_name = 'Relative Humidity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('wind_speed', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'wind_speed'
   v.long_name = 'Wind Speed'
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
   
   v = nc.createVariable('thickness_of_rainfall_amount', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.standard_name = 'thickness_of_rainfall_amount'
   v.long_name = 'Rain Accumulated in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('rainfall_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.standard_name = 'rainfall_rate'
   v.long_name = 'Rainfall Rate'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('hail_intensity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hits cm-2'
   v.long_name = 'Hail Intensity'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)

   v = nc.createVariable('hail_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'hits cm-2 hr-1'
   v.long_name = 'Hail Rate'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('downwelling_longwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'downwelling_longwave_flux_in_air'
   v.long_name = 'Downwelling Longwave Radiation'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('downwelling_shortwave_flux_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.standard_name = 'shortwelling_longwave_flux_in_air'
   v.long_name = 'Downwelling Shortwave Radiation'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('downwelling_total_irradiance', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.long_name = 'Downwelling Total Radiative Flux'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('net_total_irradiance', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'W m-2'
   v.long_name = 'Net Downwelling Radiative Flux'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
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
   
   v = nc.createVariable('qc_flag_wind_from_direction', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Wind From Direction'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_radiation', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Radiation'
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
   
   del dat, com, np, data_1d, flag_1d