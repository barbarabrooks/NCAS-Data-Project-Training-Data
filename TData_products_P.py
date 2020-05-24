# P
def peroxyacetyl_nitrate_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mole_fraction_of_peroxyacetyl_nitrate_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'nmol mol-1'
   v.standard_name = 'mole_fraction_of_peroxyacetyl_nitrate_in_air'
   v.long_name = 'Mole Fraction of Peroxyacetyl Nitrate in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H3NO5'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_fraction_of_peroxyacetyl_nitrate_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1e-9'
   v.practical_units = 'ppt'
   v.standard_name = 'mass_fraction_of_peroxyacetyl_nitrate_in_air'
   v.long_name = 'Mass Fraction of Peroxyacetyl Nitrate in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H3NO5'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mole_concentration_of_peroxyacetyl_nitrate_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mol m-3'
   v.standard_name = 'mole_concentration_of_peroxyacetyl_nitrate_in_air'
   v.long_name = 'Mole Concentration of Peroxyacetyl Nitrate in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H3NO5'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_peroxyacetyl_nitrate_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'kg m-3'
   v.standard_name = 'mass_concentration_of_peroxyacetyl_nitrate_in_air'
   v.long_name = 'Mass Concentration of Peroxyacetyl Nitrate in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H3NO5'
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
         
def photolysis_frequencies(meta, mode, nc, ver):
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
   v = nc.createVariable('photolysis_frequencies_jno2', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(NO(2))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jo1d', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(O(1))(D))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jhcho', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(HCHO))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('photolysis_frequencies_jhono', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 's-1'
   v.long_name = 'Photolysis Frequencies (j(HONO))'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: point'
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
         
def pm_concentration(meta, mode, nc, ver):
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
   v = nc.createVariable('mass_concentration_of_pm1_ambient_aerosol_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug m-3'
   v.standard_name = 'mass_concentration_of_pm1_ambient_aerosol_in_air'
   v.long_name = 'Mass Concentration of PM1 Ambient Aerosol in Air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)  
   
   v = nc.createVariable('mass_concentration_of_pm2p5_ambient_aerosol_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug m-3'
   v.standard_name = 'mass_concentration_of_pm2p5_ambient_aerosol_in_air'
   v.long_name = 'Mass Concentration of PM2.5 Ambient Aerosol in Air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 
   
   v = nc.createVariable('mass_concentration_of_pm4_ambient_aerosol_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug m-3'
   v.long_name = 'Mass Concentration of PM4 Ambient Aerosol in Air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('mass_concentration_of_pm10_ambient_aerosol_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug m-3'
   v.standard_name = 'mass_concentration_of_pm10_ambient_aerosol_in_air'
   v.long_name = 'Mass Concentration of PM10 Ambient Aerosol in Air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d) 
   
   v = nc.createVariable('mass_concentration_of_total_pm_ambient_aerosol_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'ug m-3'
   v.long_name = 'Mass Concentration of Total PM Ambient Aerosol Particles in air'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
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

   v = nc.createVariable('qc_flag_pm1', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: PM1'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_pm2p5', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: PM2.5'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_pm4', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: PM4'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_pm10', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: PM10'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_total_pm', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Total PM'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   v = nc.createVariable('qc_flag_total_number', np.int8, ('time',))
   #variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: Total Number'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = 'not_used' + '\n'
   v.flag_meanings = v.flag_meanings + 'good_data' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data<0.075' + '\n'
   v.flag_meanings = v.flag_meanings + 'suspect_data_data_not_quality_controlled:_data>0.925' + '\n'
   v.flag_meanings = v.flag_meanings + 'bad_data_do_not_use:_data=0' 
   #write data
   v[:] = np.int8(flag_1d)
   
   del dat, com, np, data_1d, flag_1d    
         
def precipitation(meta, mode, nc, ver):
   import TData_data as dat
   import TData_common as com
   import numpy as np
   
   # create time dat and flag variables  
   diam = 20; fall = 22;
   [ET, DT, DoY] = dat.create_time(meta)
   [lat, lon] = dat.create_pos(ET, mode)
   
   dd = np.empty([diam])
   fs = np.empty([fall])
   
   for x in range(0, diam):
      dd[x] = x * 2
      
   for x in range(0, fall):
      fs[x] = x * 4
      
   [data_1d, flag_1d, min_dat, max_dat] = dat.create_data_flag(ET)
   
   data_3d = np.empty([len(ET), fall, diam])
   flag_3d = np.empty([len(ET), fall, diam])
         
   for x in range(0, len(ET)):
      for y in range(0, fall):
         for z in range(0, diam):
            data_3d[x, y, z] = data_1d[x]
    
   # write common global attrib 
   com.global_attributes(nc, meta, ET, mode)
   
   # write specific global attrib
   nc.product_version = ver
   nc.setncattr('measurement_technique', 'drop counting')
   nc.setncattr('drop size in mm', '0.01 mm')
   nc.setncattr('amount', '0.1 mm')
   nc.setncattr('width of rain gauge throat', '20 cm')
   nc.setncattr('laser wavelength', '785 nm')
   nc.setncattr('sample area', '45 cm2')
   
   # write common dimensions
   com.dimensions(nc, ET, lat, lon)
   
   # write specific dimensions
   diameter = nc.createDimension('diameter', diam) 
   fallspeed = nc.createDimension('fallspeed', fall)
   
   # write common variables
   com.variables(nc, ET, DT, DoY, lat, lon, mode)
   
   # write specific variables 
   v = nc.createVariable('diameter', np.float32, ('diameter',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.long_name = 'Hydrometeor Diameter'
   v.valid_min = np.float32(np.min(dd))
   v.valid_max = np.float32(np.max(dd))
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(dd) 
   
   v = nc.createVariable('fallspeed', np.float32, ('fallspeed',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.long_name = 'Hydrometeor Diameter'
   v.valid_min = np.float32(np.min(fs))
   v.valid_max = np.float32(np.max(fs))
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(fs) 
   
   v = nc.createVariable('number_of_hydrometeors', np.float32, ('time', 'fallspeed', 'diameter'), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Number of Hydrometeors Detected'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:,:,:] = np.float32(data_3d)
   
   v = nc.createVariable('thickness_of_rainfall_amount', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.standard_name = 'thickness_of_rainfall_amount'
   v.long_name = 'Rain Accumulated in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: sum'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('rainfall_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.standard_name = 'rainfall_rate'
   v.long_name = 'Rain Accumulated in Averaging Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('total_precipitation_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.long_name = 'Total Precipitation Rate'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('solid_precipitation_rate', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm hr-1'
   v.long_name = 'Solid Precipitation Rate'
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
   
   v = nc.createVariable('maximum_diameter_of_hail', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'mm'
   v.long_name = 'Maximum Diameter of Hail'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('number_of_drops', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = '1'
   v.long_name = 'Number of Pulses\Drops Counted in Integration Period'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('equivalent_reflectivity_factor', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'dBZ'
   v.standard_name = 'equivalent_reflectivity_factor'
   v.long_name = 'Equivalent Radar Reflectivity Factor'
   v.valid_min = np.float32(min_dat)
   v.valid_max = np.float32(max_dat)
   v.cell_methods = 'time: mean'
   v.coordinates = 'latitude longitude'
   #write data
   v[:] = np.float32(data_1d)
   
   v = nc.createVariable('precipitation_visibility', np.float32, ('time',), fill_value=-1.00e+20)
   #variable attributes
   v.units = 'm'
   v.long_name = 'Visibility Reduction Caused by Precipitation.'
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
   
   del dat, com, np, data_1d, flag_1d, data_3d