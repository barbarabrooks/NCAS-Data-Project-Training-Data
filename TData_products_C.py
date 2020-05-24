# C
def ch4_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_methane_in_air'
   v.long_name = 'Mole Fraction of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_methane_in_air'
   v.long_name = 'Mass Fraction of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_methane_in_air'
   v.long_name = 'Mole Concentration of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_methane_in_air'
   v.long_name = 'Mass Concentration of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
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
         
def ch4_n2o_co2_co_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_methane_in_air'
   v.long_name = 'Mole Fraction of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_methane_in_air'
   v.long_name = 'Mass Fraction of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_methane_in_air'
   v.long_name = 'Mole Concentration of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_methane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_methane_in_air'
   v.long_name = 'Mass Concentration of Methane in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CH4'
   #write data
   v[:] = np.float32(data_1d)
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_nitrous_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_nitrous_oxide_in_air'
   v.long_name = 'Mole Fraction of Nitrous Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_nitrous_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_nitrous_oxide_in_air'
   v.long_name = 'Mass Fraction of Nitrous Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'N2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_nitrous_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_nitrous_oxide_in_air'
   v.long_name = 'Mole Concentration of Nitrous Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'N2O'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_nitrous_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_nitrous_oxide_in_air'
   v.long_name = 'Mass Concentration of Nitrous Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'N2O'
   #write data
   v[:] = np.float32(data_1d)
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Fraction of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_carbon_dioxide_in_air'
   v.long_name = 'Mass Fraction of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mass Concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mole Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_ch4', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: CH4'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)

   v = nc.createVariable('qc_flag_n2o', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: N2O'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d) 

   v = nc.createVariable('qc_flag_co2', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: CO2'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d) 

   v = nc.createVariable('qc_flag_co', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: CO'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d) 

   del dat, com, np, data_1d, flag_1d   

def cloud_base(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 4; dg = 1;
  
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   data_2d = np.empty([len(ET), gates])
   flag_2d = np.empty([len(ET), gates])
         
   for x in range(0, len(ET)):
      for y in range(0,gates):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x]
    
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
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
   layer_index = nc.createDimension('layer_index', gates) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('cloud_base_altitude', np.float32, ('time','layer_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.standard_name = 'cloud_base_altitude'
   v.long_name = 'Cloud Base Altitude (Geometric height above geoid WGS84)'
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
   
   del dat, com, np, data_1d, flag_1d, data_2d, flag_2d 
            
         
def cloud_coverage(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   gates = 4; dg = 1;
  
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   data_2d = np.empty([len(ET), gates])
   flag_2d = np.empty([len(ET), gates])
         
   for x in range(0, len(ET)):
      for y in range(0,gates):
         data_2d[x,y] = data_1d[x]
         flag_2d[x,y] = flag_1d[x]
    
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
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
   layer_index = nc.createDimension('layer_index', gates) 
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables
   v = nc.createVariable('cloud_base_altitude', np.float32, ('time','layer_index',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.standard_name = 'cloud_base_altitude'
   v.long_name = 'Cloud Base Altitude (Geometric height above geoid WGS84)'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.float32(data_2d)
   
   v = nc.createVariable('cloud_coverage', np.int8, ('time','layer_index',), fill_value=-127)
   #variable attributes
   v.units = 'okta'
   v.long_name = 'Cloud Coverage in oktas (0 = clear, 8 = full coverage, 9 = vertical visibility)'
   v.valid_min = np.int8(min_dat * 10)
   v.valid_max = np.int8(max_dat * 10)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:] = np.int8(data_2d * 10)
   
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
   
   del dat, com, np, data_1d, flag_1d, data_2d, flag_2d          
         
def co_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mole Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
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

def co_h2_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mole Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Fraction of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_carbon_monoxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_carbon_monoxide_in_air'
   v.long_name = 'Mass Concentration of Carbon Monoxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO'
   #write data
   v[:] = np.float32(data_1d)
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_molecular_hydrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_molecular_hydrogen_in_air'
   v.long_name = 'Mole Fraction of Molecular Hydrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_molecular_hydrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_molecular_hydrogen_in_air'
   v.long_name = 'Mass Fraction of Molecular Hydrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_molecular_hydrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_molecular_hydrogen_in_air'
   v.long_name = 'Mole Concentration of Molecular Hydrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_molecular_hydrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_molecular_hydrogen_in_air'
   v.long_name = 'Mass Concentration of Molecular Hydrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'H2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_co', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: CO'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_h2', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: H2'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d        
         
def co2_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Fraction of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_carbon_dioxide_in_air'
   v.long_name = 'Mass Fraction of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mole Concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_carbon_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_carbon_dioxide_in_air'
   v.long_name = 'Mass Concentration of Carbon Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'CO2'
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