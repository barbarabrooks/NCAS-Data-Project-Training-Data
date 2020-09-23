# N
def n2o_concentration(meta, mode, nc, ver):
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
         
def n2o_sf6_concentration(meta, mode, nc, ver):
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
   
   v = nc.createVariable('qc_flag_sf6', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: SF6'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d           
         
def no2_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mole Fraction of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mass Fraction of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mole Concentration of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mass Concentration of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
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
         
def nox_noxy_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_nitric_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.long_name = 'Mole Fraction of Nitric Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_nitric_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.long_name = 'Mass Fraction of Nitric Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_nitric_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.long_name = 'Mole Concentration of Nitric Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_nitric_oxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.long_name = 'Mass Concentration of Nitric Oxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO'
   #write data
   v[:] = np.float32(data_1d)  
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mole Fraction of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mass Fraction of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mole Concentration of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_nitrogen_dioxide_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_nitrogen_dioxide_in_air'
   v.long_name = 'Mass Concentration of Nitrogen Dioxide in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NO2'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_fraction_of_nox_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_nox_expressed_as_nitrogen_in_air'
   v.long_name = 'Mole Fraction of NOx expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOx'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_nox_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_nox_expressed_as_nitrogen_in_air' 
   v.long_name = 'Mass Fraction of NOx expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOx'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_nox_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_nox_expressed_as_nitrogen_in_air'
   v.long_name = 'Mole Concentration of NOx expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOx'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_nox_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_nox_expressed_as_nitrogen_in_air'
   v.long_name = 'Mass Concentration of NOx expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOx'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_fraction_of_noy_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.long_name = 'Mole Fraction of NOy expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOy'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_noy_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.long_name = 'Mass Fraction of NOy expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOy'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_noy_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.long_name = 'Mole Concentration of NOx expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOy'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_noy_expressed_as_nitrogen_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.long_name = 'Mass Concentration of NOy expressed as nitrogen in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'NOy'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('qc_flag_no', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NO'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_no2', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NO2'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_nox', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NOx'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_noy', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: NOy'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d   