# D
def depolarisation_ratio(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 100; dg = 30
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   #data_1d, flag_1d: length ET
   range_1d = dat.create_data_range(gates, dg) # length gates
   angles = 1
   AZ_2d = np.empty([len(ET), angles])
   EL_2d = np.empty([len(ET), angles])
   min_AZ = 23; max_AZ = 23
   min_EL = 88; max_EL = 88
   for x in range(0, len(ET)):
      AZ_2d[x, :] = np.ones([angles]) * 23
      EL_2d[x, :] = np.ones([angles]) * 88
 
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
   
   v = nc.createVariable('attenuated_aerosol_backscatter_coefficient_co', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Attenuated Aerosol Backscatter Coefficient (Planar Polarised)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('signal_to_noise_ratio_plus_1_co', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Signal to Noise Ratio: SNR+1 (Planar Polarised)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('attenuated_aerosol_backscatter_coefficient_cr', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm-1 sr-1'
   v.long_name = 'Attenuated Aerosol Backscatter Coefficient (Cross Polarised)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('signal_to_noise_ratio_plus_1_cr', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Signal to Noise Ratio: SNR+1 (Cross Polarised)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('depolarisation_ratio', np.float32, ('time', 'index_of_range', 'index_of_angle',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Volume Linear Depolarization Ratio'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.coordinates = 'latitude longitude'
   v.cell_methods = 'time: mean'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('qc_flag_attenuated_aerosol_backscatter_coefficient_co', np.float32, ('time', 'index_of_range', 'index_of_angle',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Attenuated backscatter coefficient (Planar Polarised)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:,:] = np.int8(flag_3d)
   
   v = nc.createVariable('qc_flag_attenuated_aerosol_backscatter_coefficient_cr', np.float32, ('time', 'index_of_range', 'index_of_angle',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Attenuated backscatter coefficient (Cross Polarised)'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:,:,:] = np.int8(flag_3d)
      
   del dat, com, np, range_1d, data_1d, AZ_2d, EL_2d, range_3d, data_3d, flag_3d   
         
def dew_point(meta, mode, nc, ver):
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

   v = nc.createVariable('dew_point_temperature', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'K'
   v.standard_name = 'dew_point_temperature'
   v.long_name = 'Dew \Frost point Temperature'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
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
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_fraction_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_water_vapor_in_air'
   v.long_name = 'Mole Fraction of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.long_name = 'Mass Fraction of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_water_vapor_in_air'
   v.long_name = 'Mole Concentration of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_water_vapor_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_water_vapor_in_air'
   v.long_name = 'Mass Concentration of Water Vapour in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2O'
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