# A
def acoustic_backscatter_winds(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
    
   # create time dat and flag variables
   gates = 100; dg = 30
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
      v = nc.createVariable('sound_intensity_level_in_air', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('sound_intensity_level_in_air', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dB'
   v.standard_name = 'sound_intensity_level_in_air'
   v.long_name = 'Sound Intensity Level in Air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
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
   
   if '1' in ver:
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
   
   if '1' in ver:
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
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_mean_winds', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_mean_winds', np.int8, ('time', 'altitude',))
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
      v = nc.createVariable('qc_flag_wind_component_eastward', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_wind_component_eastward', np.int8, ('time', 'altitude',))
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
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_wind_component_northward', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_wind_component_northward', np.int8, ('time', 'altitude',))
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
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_wind_component_upward_air_velocity', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_wind_component_upward_air_velocity', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Upward Air Velocity (W)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_backscatter', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_backscatter', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Backscatter'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_background_noise', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_background_noise', np.int8, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Background Noise'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
         
   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_2d, flag_2d
   
def aerosol_backscatter_radial_winds(meta, mode, opt, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 100; dg = 30;
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
         
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   range_1d = dat.create_data_range(gates, dg) # length gates
   
   if 'fixed' in opt:
      angles = 1
      AZ_2d = np.empty([len(ET), angles])
      EL_2d = np.empty([len(ET), angles])
      min_AZ = 23; max_AZ = 23
      min_EL = 88; max_EL = 88
      for x in range(0, len(ET)):
         AZ_2d[x, :] = np.ones([angles]) * 23
         EL_2d[x, :] = np.ones([angles]) * 88
         
   if 'rhi' in opt:   
      angles = 5
      AZ_2d = np.empty([len(ET), angles])
      EL_2d = np.empty([len(ET), angles])
      min_AZ = 20; max_AZ = 20
      min_EL = 0; max_EL = 180
      for x in range(0, len(ET)):
         AZ_2d[x, :] = np.ones([angles]) * 20
         EL_2d[x, :] = [0, 45, 90, 135, 180]
   
   if 'ppi' in opt:   
      angles = 8  
      AZ_2d = np.empty([len(ET), angles])
      EL_2d = np.empty([len(ET), angles])
      min_AZ = 0; max_AZ = 315
      min_EL = 45; max_EL = 45
      for x in range(0, len(ET)):
         AZ_2d[x, :] = [0, 45, 90, 135, 180, 225, 270, 315]
         EL_2d[x, :] = np.ones([angles]) * 45
   
   if 'winds-ppi' in opt:   
      angles = 4   
      AZ_2d = np.empty([len(ET), angles])
      EL_2d = np.empty([len(ET), angles])
      min_AZ = 0; max_AZ = 270
      min_EL = 70; max_EL = 70
      for x in range(0, len(ET)):
         AZ_2d[x, :] = [0, 90, 180, 270]
         EL_2d[x, :] = np.ones([angles]) * 70
         
   if 'user' in opt:   
      angles = 4   
      AZ_2d = np.empty([len(ET), angles])
      EL_2d = np.empty([len(ET), angles])
      min_AZ = 0; max_AZ = 270
      min_EL = 0; max_EL = 180
      for x in range(0, len(ET)):
         AZ_2d[x, :] = [0, 90, 180, 270]
         EL_2d[x, :] = [0, 60, 120, 180]    
 
   # create 3d data
   data_3d = np.empty([len(ET), gates, angles])
   range_3d = np.empty([len(ET), gates, angles])
   flag_3d = np.empty([len(ET), gates, angles])
   for x in range(0, len(ET)):
      for y in range(0, gates):
         for z in range(0, angles):
            data_3d[x, y, z] = data_1d[x]
            flag_3d[x, y, z] = flag_1d[x]
            range_3d[x, y, z] = range_1d[y]
   
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.featureType = 'timeSeriesProfile'
   nc.product_version = ver
   nc.setncattr('laser_wavelength', '910 nm')
   nc.setncattr('nominal_laser_pulse_energy', '3.0e-06 J')
   nc.setncattr('pulse_repetition_frequency', '6500 s-1')
   nc.setncattr('lens_diameter', '0.148 m')
   nc.setncattr('beam_divergence', '0.14 degrees')
   nc.setncattr('pulse_length', '1.1e-07 s')
   nc.setncattr('sampling_frequency', '1.5e+07 s-1')
   nc.setncattr('focus', 'Inf')
   nc.setncattr('velocity_resolution', '0.0382 m s-1')
   nc.setncattr('number_of_gates', '64')
   nc.setncattr('gate_length', '30 m')
   nc.setncattr('fft_length', '1024')
   nc.setncattr('maximum_range', '10 000m')
      
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   index_of_range = nc.createDimension('index_of_range', gates)
   index_of_angle = nc.createDimension('index_of_angle', angles) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)   

   # write specific variables
   v = nc.createVariable('range', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.long_name = 'Distance of Measurement Volume Centre Point from Instrument'
   v.axis = 'Z'
   v.valid_min = np.float32(min(range_1d))
   v.valid_max = np.float32(max(range_1d))
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:,:] = np.float32(range_3d)
   
   v = nc.createVariable('sensor_azimuth_angle_instrument_frame', np.float32, ('time', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Scanning head azimuth angle in the instrument frame of reference'
   v.valid_min = np.float32(min_AZ)
   v.valid_max = np.float32(max_AZ)
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(AZ_2d)
   
   v = nc.createVariable('sensor_view_angle_instrument_frame', np.float32, ('time', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Scanning head elevation angle in the instrument frame of reference'
   v.valid_min = np.float32(min_EL)
   v.valid_max = np.float32(max_EL)
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(EL_2d)
   
   v = nc.createVariable('sensor_azimuth_angle_earth_frame', np.float32, ('time', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Scanning head azimuth angle in the Earth frame of reference'
   v.valid_min = np.float32(min_AZ)
   v.valid_max = np.float32(max_AZ)
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(AZ_2d)
   
   v = nc.createVariable('sensor_view_angle_earth_frame', np.float32, ('time', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.long_name = 'Scanning head elevation angle in the Earth frame of reference'
   v.valid_min = np.float32(min_EL)
   v.valid_max = np.float32(max_EL)
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(EL_2d)
   
   v = nc.createVariable('radial_velocity_of_scatterers_away_from_instrument', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm s-1'
   v.standard_name = 'radial_velocity_of_scatterers_away_from_instrument'
   v.long_name = 'Radial Velocity of Scatterers Away From Instrument'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('attenuated_aerosol_backscatter_coefficient', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Attenuated Aerosol Backscatter Coefficient'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('signal_to_noise_ratio_plus_1', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Signal to Noise Ratio: SNR+1'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('qc_flag_radial_velocity_of_scatterers_away_from_instrument', np.float32, ('time', 'index_of_range', 'index_of_angle',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Radial Velocity of Scatterers Away From Instrument'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:,:] = np.int8(flag_3d)
   
   v = nc.createVariable('qc_flag_backscatter', np.float32, ('time', 'index_of_range', 'index_of_angle',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Backscatter'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:,:] = np.int8(flag_3d)
      
   del dat, com, np, range_1d, data_1d, flag_1d, AZ_2d, EL_2d, range_3d, data_3d, flag_3d   
    
def aerosol_backscatter(meta, mode, nc, ver):
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
   nc.setncattr('laser_wavelength', '910 nm')
   nc.setncattr('nominal_laser_pulse_energy', '3.0e-06 J')
   nc.setncattr('pulse_repetition_frequency', '6500 s-1')
   nc.setncattr('lens_diameter', '0.148 m')
   nc.setncattr('beam_divergence', '0.14 degrees')
   nc.setncattr('pulse_length', '1.1e-07 s')
   nc.setncattr('sampling_frequency', '1.5e+07 s-1')
      
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
      v = nc.createVariable('attenuated_aerosol_backscatter_coefficient', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('attenuated_aerosol_backscatter_coefficient', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Attenuated Aerosol Backscatter Coefficient'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)   
   
   if '1' in ver:
      v = nc.createVariable('range_squared_corrected_backscatter_power', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('range_squared_corrected_backscatter_power', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Range Squared Corrected Backscatter Power (ln(arbitrary raw data unit))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d) 
   
   v = nc.createVariable('laser_pulse_energy', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.long_name = 'Laser Pulse Energy (% of maximum)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('laser_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Laser Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sensor_zenith_angle', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'sensor_zenith_angle'
   v.long_name = 'Sensor Zenith Angle (from vertical)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sensor_azimuth_angle', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'degree'
   v.standard_name = 'sensor_azimuth_angle'
   v.long_name = 'Sensor Azimuth Angle (clockwise from true North)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('profile_pulses', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Number of pulses in each profile'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('profile_scaling', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.long_name = 'Scaling of range profile (default = 100%)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('window_contamination', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mV'
   v.long_name = 'Window Contamination (mV as measured by ADC: 0 - 2500)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('window_transmttance', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '%'
   v.long_name = 'Window Transmittance, % of nominal value'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('background_light', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mV'
   v.long_name = 'Background Light (mV as measured by ADC: 0 - 2500)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('backscatter_sum', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mV'
   v.long_name = 'Sum of detected and normalized backscatter'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag', np.float32, ('time', 'altitude',))
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
      
   del dat, com, np, range_1d, alt_1d, alt_2d, data_1d, flag_1d, data_2d, flag_2d 
         
def aerosol_concentration(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables 
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
   v = nc.createVariable('number_concentration_of_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm-3'
   v.standard_name = 'number_concentration_of_ambient_aerosol_particles_in_air'
   v.long_name = 'Number Concentration of Ambient Aerosol Particles in air'
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
         
def aerosol_extinction(meta, mode, nc, ver):
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
      v = nc.createVariable('volume_extinction_coefficient_in_air_due_to_ambient_aerosol_particles_355', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('volume_extinction_coefficient_in_air_due_to_ambient_aerosol_particles_355', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Volume Extinction Coefficient in air due to Ambient Aerosol Particles (Wavelength = 355 nm)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)   
   
   if '1' in ver:
      v = nc.createVariable('volume_extinction_coefficient_in_air_due_to_ambient_aerosol_particles_316', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   else:
      v = nc.createVariable('volume_extinction_coefficient_in_air_due_to_ambient_aerosol_particles_316', np.float32, ('time', 'altitude',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Volume Extinction Coefficient in air due to Ambient Aerosol Particles (Wavelength = 316 nm)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_355', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_355', np.float32, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: 316nm'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)
   
   if '1' in ver:
      v = nc.createVariable('qc_flag_316', np.float32, ('time', 'index',))
   else:
      v = nc.createVariable('qc_flag_316', np.float32, ('time', 'altitude',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: 316nm'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:] = np.int8(flag_2d)

   del dat, com, np, range_1d, alt_1d, data_1d, flag_1d, alt_2d, data_2d, flag_2d
         
def aerosol_no3_so4_nh3_org_concentration(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables 
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
   v = nc.createVariable('mass_concentration_of_nitrate_in_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug cm-3'
   v.long_name = 'Mass concentration of the NO3 component of ambient aerosol particles in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   chemical_species = 'NO3'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_sulfate_in_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug cm-3'
   v.long_name = 'Mass concentration of the SO4 component of ambient aerosol particles in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   chemical_species = 'SO4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_ammonia_in_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug cm-3'
   v.long_name = 'Mass concentration of the NH3 component of ambient aerosol particles in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   chemical_species = 'NH3'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_organics_in_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug cm-3'
   v.long_name = 'Mass concentration of the organic component of ambient aerosol particles in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   chemical_species = 'organic'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_no3', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NO3'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_so4', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: SO4'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_nh3', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NH3'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_org', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Organics'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d         
         
def aerosol_optical_depth(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables 
   [ET, DT, DoY] = dat.create_time(meta)   
   freq = 10;
   ff = np.empty([freq])
   for x in range(0,freq):
      ff[x] = (x * 10) + x
      
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
   index = nc.createDimension('index', freq) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('instrument_channel_wavelength', np.float32, ('index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'nm'
   v.long_name = 'Instrument Channel Wavelength'
   v.valid_min = np.float32(np.min(ff))
   v.valid_max = np.float32(np.max(ff))
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(ff)
   
   v = nc.createVariable('angstrom_exponent_of_ambient_aerosol_in_air', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.standard_name = 'angstrom_exponent_of_ambient_aerosol_in_air'
   v.long_name = 'Angstrom Exponent of Ambient Aerosol in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('atmosphere_optical_thickness_due_to_ambient_aerosol_particles', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.standard_name = 'atmosphere_optical_thickness_due_to_ambient_aerosol_particles'
   v.long_name = 'Atmosphere Optical Thickness Due to Ambient Aerosol Particles'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('qc_flag', np.int8, ('time','index',))
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
   
   del dat, com, np, ff, data_1d, flag_1d, data_2d, flag_2d   
         
def aerosol_size_distribution(nm, meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables 
   diam = 32; dg = 20;
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   dd_1d = np.empty([diam])
   for x in range(0, diam):
      dd_1d[x] = x * dg + x
      
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   data_2d = np.empty([len(ET), diam])
   flag_2d = np.empty([len(ET), diam])
   dd_2d = np.empty([len(ET), diam])
         
   for x in range(0, len(ET)):
      for y in range(0, diam):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x]
         dd_2d [x,y] = dd_1d[y]
      
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver
   nc.setncattr('measurement_technique', 'holder')
   nc.setncattr('dma_inner_radius', 'not applicable')
   nc.setncattr('dma_outer_radius', 'not applicable')
   nc.setncattr('dma_length', 'not applicable')
   nc.setncattr('impactor_orifice_diameter', 'not applicable')
   nc.setncattr('lower_channel_cut_off', 'not applicable')
   nc.setncattr('upper_channel_cut_off', 'not applicable')
   
   if 'ncas-aps' in nm:
      nc.setncattr('measurement_technique', 'aerodynamic')
      nc.setncattr('lower_channel_cut_off', '3 um')
      nc.setncattr('upper_channel_cut_off', '195 um')
   if 'ncas-smps' in nm:
      nc.setncattr('measurement_technique', 'electrostatic_mobility')
      nc.setncattr('dma_inner_radius', '0.937 cm')
      nc.setncattr('dma_outer_radius', '1.961 cm')
      nc.setncattr('dma_length', '44.369 cm')
      nc.setncattr('impactor_orifice_diameter', '0.0508 cm')
      nc.setncattr('lower_channel_cut_off', '3 nm')
      nc.setncattr('upper_channel_cut_off', '195 nm')
   else: 
      nc.setncattr('measurement_technique', 'optical')
      nc.setncattr('lower_channel_cut_off', '3 um')
      nc.setncattr('upper_channel_cut_off', '195 um')
   
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   index = nc.createDimension('index', diam) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('ambient_aerosol_particle_diameter', np.float32, ('time','index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'um'
   v.standard_name = 'ambient_aerosol_particle_diameter'
   v.long_name = 'Ambient Aerosol Particle Diameter'
   v.valid_min = np.float32(np.min(dd_1d))
   v.valid_max = np.float32(np.max(dd_1d))
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(dd_2d)
   
   v = nc.createVariable('measurement_channel_lower_limit', np.float32, ('time','index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'um'
   v.long_name = 'Lower Limit of Spectrometer Measurement Channel'
   v.valid_min = np.float32(np.min(dd_1d))
   v.valid_max = np.float32(np.max(dd_1d))
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(dd_2d)  

   v = nc.createVariable('measurement_channel_upper_limit', np.float32, ('time','index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'um'
   v.long_name = 'Upper Limit of Spectrometer Measurement Channel'
   v.valid_min = np.float32(np.min(dd_1d))
   v.valid_max = np.float32(np.max(dd_1d))
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(dd_2d)      
      
   v = nc.createVariable('ambient_aerosol_number_per_channel', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm3-1'
   v.long_name = 'Ambient Aerosol Number per Channel (dN)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('ambient_aerosol_size_distribution', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm3-1 um-1'
   v.long_name = 'Ambient Aerosol Size Distribution (dN\dD)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('ambient_aerosol_size_log_distribution', np.float32, ('time', 'index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm3-1'
   v.long_name = 'Ambient Aerosol Size Distribution (dN\dlogD)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('total_number_concentration_of_ambient_aerosol_particles_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'cm3-1'
   v.long_name = 'Number Concentration of Ambient Aerosol Particles in air (N)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sample_pressure', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kPa'
   v.long_name = 'Pressure of Sample Stream'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sample_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.long_name = 'Temperature of Sample Stream'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sample_mean_free_path', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.long_name = 'Mean Free Path of Sample Stream'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('sample_gas_viscosity', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'Pa s'
   v.long_name = 'Gas Viscosity of Sample Stream'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag', np.int8, ('time','index',))
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
   
   del dat, com, np, dd_1d, data_1d, flag_1d, dd_2d, data_2d, flag_2d        