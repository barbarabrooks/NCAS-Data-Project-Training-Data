def read_meta(logfile, vocab_ver):
   import pandas as pd
   from datetime import datetime
   
   # read in meta
   if vocab_ver == "1.1":
      fn = "meta_1.1.xlsx"
      
   if vocab_ver == "2.0":
      fn = "meta_2.0.xlsx"
   
   try:
      df = pd.read_excel(fn)
   except:
      # exit if problem encountered
      print("Unable to open meta.xlsx. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open meta.xlsx. Program will terminate.\n')
      g.close()
      exit()     
   
   del pd, datetime    
   
   return df
   
def read_lookup(logfile):
   import pandas as pd
   from datetime import datetime
   
   # read in lookup1 table
   try:
      df = pd.read_excel("lookup.xlsx")
   except:
      # exit if problem encountered
      print("Unable to open lookup.xlsx. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open lookup.xlsx. Program will terminate.\n')
      g.close()
      exit()
  
   name = df.loc[:, 'name':'name':1].values
   name_product = df.loc[:, 'product':'product':1].values
   
   #delete the lookup table as not needed now
   del df, pd, datetime
   
   return name, name_product

def read_config(logfile):
   from datetime import datetime
   
   # read in Config file
   try:
      f = open("Config.txt", "r")
      if f.mode == 'r':
         lines = f.readlines()
         f.close()
   except:
      # exit if problem encountered
      print("Unable to open Config.txt file. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open Config.txt. Program will terminate.\n')
      g.close()
      exit()
   
   # process information in config file
   # 1. deployment mode
   # Create a list called mode
   
   # find the start of deployment mode info block
   x_st = 0; x_ed = 0;
   ss1 = "Mode Start"; ss2 = "Mode End"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         x_st = x          
      if (ss2 in lines[x]):
         x_ed = x
         break         
   
   mode = []
   for x in range (x_st+1, x_ed):
      if (('<' in lines[x]) or ('>' in lines[x])):
         # do nothing - line below is just a dummy
         cc = 0
      else:
         if ('all' in lines[x]):
            mode.append(lines[x].strip('\n'))
            break
         else:         
            mode.append(lines[x].strip('\n'))
            
   if len(mode) == 0:
      print("A deployment mode must be provided. This program will termnate.")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' A deployment mode must be provided. Program will terminate.\n')
      g.close()
      exit()
      
   # 2. Instruments
   # Create a list called instruments
   # If no instrument name is given set value to 'all' 
   
   # find the start of instrument info block
   x_st = 0; x_ed = 0;
   ss1 = "Instrument Start"; ss2 = "Instrument End"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         x_st = x          
      if (ss2 in lines[x]):
         x_ed = x
         break         
   
   instrument = []
   for x in range (x_st+1, x_ed):
      if (('<' in lines[x]) or ('>' in lines[x])):
         # do nothing - line below is just a dummy
         cc = 0
      else:
         if ('all' in lines[x]):
            instrument.append(lines[x].strip('\n'))
            break
         else:        
            instrument.append(lines[x].strip('\n'))   
            
   if len(instrument) == 0:
      # if no instrument name give then drive by the list of data products
      instrument.append('empty')
      
   # 3. data products
   # Create a list called data_product
   # If no data product name is given set value to 'all' 
   
   # find the start of instrument info block
   x_st = 0; x_ed = 0;
   ss1 = "Data Product Start"; ss2 = "Data Product End"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         x_st = x          
      if (ss2 in lines[x]):
         x_ed = x
         break         
   
   data_product = []
   for x in range (x_st+1, x_ed):
      if (('<' in lines[x]) or ('>' in lines[x])):
         # do nothing - line below is just a dummy
         cc = 0
      else:
         if ('all' in lines[x]):
            data_product.append(lines[x].strip('\n'))
            break
         else:        
            data_product.append(lines[x].strip('\n'))   
            
   if len(data_product) == 0:
   # if no data products given then drive by the list of instruments
      data_product.append('empty')
      
   if (('empty' in instrument[0]) and ('empty' in data_product[0])):
      print("Either an instrument name or a data product name must be given. This program will terminate.")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Either an instrument name or data product must be provided. Program will terminate.\n')
      g.close()
      exit()
      
   # 3. Data set version
   # Create a list called ver
   
   # find the start of deployment mode info block
   x_st = 0; x_ed = 0;
   ss1 = "Version Start"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         ver = lines[x+1].strip('\n')        
         break  

   # 4. Vocabulary version
   # Create a list called ver
   
   # find the start of deployment mode info block
   x_st = 0; x_ed = 0;
   ss1 = "Vocabulary Start"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         vocab_ver = lines[x+1].strip('\n')        
         break 
         
   
   #delete the config file as not needed now
   del lines, datetime
      
   return mode, instrument, data_product, ver, vocab_ver
   
def create_runs(name, name_product, mode, instrument, data_product):
   # create temporary run list
   # column 1 name
   # column 2 data product
   
   import numpy as np
   
   col1 = [] # instrument name
   col2 = [] # data product
   for x in range (0, len(name)):
      # get the data product(s). If there are multiple data products they separated by ","
      nm = str(name[x]);
      dp = str(name_product[x])
      dp = dp.strip('[]\'\n') 
 
      # look for the positions of the seperators
      index = dp.find(",")
      # return -1 if none found
      if index < 0: #only one data product
         col1.append(nm)
         col2.append(dp)
      else:
         # at least one comma found need to find all occuances
         pos = [0]
         for y in range (0, len(dp)):
            if (',' in dp[y]):
               pos.append(y)
 
         for y in range (0, len(pos)):
            col1.append(nm)
            if y < len(pos)-1:
               col2.append(dp[pos[y] : pos[y+1]])
            else:
               col2.append(dp[pos[y] : len(dp)])
               
   #strip out all unwanted characters
   for x in range(0, len(col1)):
      col1[x] = col1[x].strip(',[]\'\n')
      col1[x] = col1[x].strip()
    
   for x in range(0, len(col2)):
      col2[x] = col2[x].strip(',[]\'\n')
      col2[x] = col2[x].strip()
      
   for x in range(0, len(data_product)):
      data_product[x] = data_product[x].strip('[]\'\n') 
      data_product[x] = data_product[x].strip()

   for x in range(0, len(instrument)):
      instrument[x] = instrument[x].strip('[]\'\n')
      instrument[x] = instrument[x].strip()      
   
   # if all instruments or all data products requested
   if (('all' in instrument[0]) or ('all' in data_product[0])):
      run_list = np.empty([len(col1), 2], dtype=object)
      for x in range (0, len(col1)):
         run_list[x,0] = col1[x]
         run_list[x,1] = col2[x]
   else:    
      cc = 0
      # run through instrument list
      # get the number of files that will be wanted
      for x in range (0, len(instrument)):
         for y in range (0, len(col1)):
            if (instrument[x] in col1[y]):
               cc = cc + 1
               
      # run through data_product lists
      # get the number of files that will be wanted         
      for x in range (0, len(data_product)):
         for y in range (0, len(col2)):
            if (data_product[x] in col2[y]):
               cc = cc + 1
               
      run_list = np.empty([cc, 2], dtype=object)
      
      # make the list
      cc = -1
      for x in range (0, len(instrument)):
         for y in range (0, len(col1)):
            if (instrument[x] in col1[y]):
               cc = cc + 1
               run_list[cc,0] = col1[y]
               run_list[cc,1] = col2[y]
               
      for x in range (0, len(data_product)):
         for y in range (0, len(col2)):
            if ((data_product[x] in col2[y]) and (len(data_product[x]) == len(col2[y]))):
               cc = cc + 1
               run_list[cc,0] = col1[y]
               run_list[cc,1] = col2[y]               
   
   # clean up and delete temp variables
   del col1, col2, np
   
   return run_list
      
def do_run(df, mode, run_list, ver, logfile,  vocab_ver):
   import pandas as pd
   import numpy as np
   import TData_products as prod
   
   for x in range (0, len(run_list)):
      # clean up name and product strings
      nm = run_list[x,0]
      dp = run_list[x,1]
      
      print('Run number: ',x,' of ', len(run_list),'. ', run_list[x,0], run_list[x,1])
     
      # pull out appropriate line from meta file
      inst = df.loc[:, 'instrument\n':'instrument\n':1].values
      tp = df.columns
      header = np.array(tp[1:len(tp)])      
      for x in range (0, len(inst)):
         if (nm in inst[x]):
            tp = df.loc[x,:].values  
            data = np.array(tp[1:len(tp)])
            break
            
      meta = np.empty([len(header), 2], dtype=object)       
      
      for x in range (0, len(header)):
         meta[x, 0] = header[x]
         meta[x, 1] = data[x]
      
      # set default file naming options
      opt1 = ''; opt2 = ''; opt3 = ''
      
      # create, write and close the files
      # A
      if (dp == 'acoustic-backscatter-winds'):
         import TData_products_A as prodA
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.acoustic_backscatter_winds(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         del prodA
         
      if ((dp == 'aerosol-backscatter-radial-winds') and (len(dp) > 20)):
         # set up all naming options
         opt11 = 'fixed'; opt21 = 'co'; opt31 = 'standard'
         opt12 = 'fixed'; opt22 = 'co'; opt32 = 'advanced'
         opt13 = 'fixed'; opt23 = 'cr'; opt33 = 'standard'
         opt14 = 'fixed'; opt24 = 'cr'; opt34 = 'advanced'
         opt15 = 'ppi';   opt25 = 'standard'; opt35 = ''
         opt16 = 'ppi';   opt26 = 'advanced'; opt36 = ''
         opt17 = 'rhi';   opt27 = 'standard'; opt37 = ''
         opt18 = 'rhi';   opt28 = 'advanced'; opt38 = ''
         opt19 = 'user-1';   opt29 = 'standard'; opt39 = ''
         opt110 = 'user-1';   opt210 = 'advanced'; opt310 = ''
         opt111 = 'user-2';   opt211 = 'standard'; opt311 = ''
         opt112 = 'user-2';   opt212 = 'advanced'; opt312 = ''
         opt113 = 'user-3';   opt213 = 'standard'; opt313 = ''
         opt114 = 'user-3';   opt214 = 'advanced'; opt314 = ''
         opt115 = 'user-4';   opt215 = 'standard'; opt315 = ''
         opt116 = 'user-4';   opt216 = 'advanced'; opt316 = ''
         opt117 = 'user-5';   opt217 = 'standard'; opt317 = ''
         opt118 = 'user-5';   opt218 = 'advanced'; opt318 = ''
         opt119 = 'winds-ppi';   opt219 = 'standard'; opt319 = ''
         opt120 = 'winds-ppi';   opt220 = 'advanced'; opt320 = ''
         
         import TData_products_A as prodA
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt11, nc, ver)
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt12, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt13, opt23, opt33, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt13, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt14, opt24, opt34, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt14, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt15, opt25, opt35, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt15, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt16, opt26, opt36, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt16, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt17, opt27, opt37, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt17, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt18, opt28, opt38, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt18, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt19, opt29, opt39, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt19, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt110, opt210, opt310, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt110, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt111, opt211, opt311, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt111, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt112, opt212, opt312, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt112, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt113, opt213, opt313, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt113, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt114, opt214, opt314, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt114, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt115, opt215, opt315, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt115, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt116, opt216, opt316, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt116, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt117, opt217, opt317, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt117, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt118, opt218, opt318, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt118, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt119, opt219, opt319, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt119, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt120, opt220, opt320, logfile, mode)
         prodA.aerosol_backscatter_radial_winds(meta, mode, opt120, nc, ver)
         nc.close()
         
         del prodA
         
      if ((dp == 'aerosol-backscatter') and (len(dp) <= 20)):
         # set up all naming options
         opt11 = 'standard'; opt21 = ''; opt31 = ''
         opt12 = 'advanced'; opt22 = ''; opt32 = ''
         
         import TData_products_A as prodA
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
         prodA.aerosol_backscatter(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
         prodA.aerosol_backscatter(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         del prodA
         
      if (dp == 'aerosol-concentration'):
         import TData_products_A as prodA 
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.aerosol_concentration(meta, mode, nc, ver)
         nc.close()
         
         del prodA
         
      if (dp == 'aerosol-extinction'):
         import TData_products_A as prodA
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.aerosol_extinction(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         del prodA
         
      if (dp == 'aerosol-no3-so4-nh3-org-concentration'):
         import TData_products_A as prodA
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.aerosol_no3_so4_nh3_org_concentration(meta, mode, nc, ver)
         nc.close()
         
         del prodA
         
      if (dp == 'aerosol-optical-depth'):
         import TData_products_A as prodA
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.aerosol_optical_depth(meta, mode, nc, ver)
         nc.close()
         
         del prodA
         
      if (dp == 'aerosol-size-distribution'):
         import TData_products_A as prodA
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodA.aerosol_size_distribution(nm, meta, mode, nc, ver)
         nc.close()
            
         del prodA
      
      # B
      if (dp == 'boundary-layer-temperature-profiles'):
         import TData_products_B as prodB
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodB.boundary_layer_temperature_profiles(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         del prodB
         
      if (dp == 'boundary-layer-thickness'):
         import TData_products_B as prodB
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodB.boundary_layer_thickness(meta, mode, nc, ver)
         nc.close()  
         
         del prodB

      if (dp == 'brightness-temperature'):
         import TData_products_B as prodB
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodB.brightness_temperature(meta, mode, nc, ver)
         nc.close()
         
         del prodB
         
      # C
      if (dp == 'ch4-concentration'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.ch4_concentration(meta, mode, nc, ver)
         nc.close()
         
         del prodC
         
      if (dp == 'ch4-n2o-co2-co-concentration'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.ch4_n2o_co2_co_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodC

      if (dp == 'cloud-base'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.cloud_base(meta, mode, nc, ver)
         nc.close()
         
         del prodC
         
      if (dp == 'cloud-coverage'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.cloud_coverage(meta, mode, nc, ver)
         nc.close()
         
         del prodC
         
      if (dp == 'co-concentration'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.co_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodC

      if (dp == 'co-h2-concentration'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.co_h2_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodC
         
      if (dp == 'co2-concentration'):
         import TData_products_C as prodC
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodC.co2_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodC
         
      # D
      if (dp == 'depolarisation-ratio'):
         import TData_products_D as prodD
         # set up all naming options
         opt11 = 'standard'; opt21 = ''; opt31 = ''
         opt12 = 'advanced'; opt22 = ''; opt32 = ''
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
         prodD.depolarisation_ratio(meta, mode, nc, ver)
         nc.close()  
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
         prodD.depolarisation_ratio(meta, mode, nc, ver)
         nc.close() 
         
         del prodD
         
      if (dp == 'dew-point'):
         import TData_products_D as prodD
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodD.dew_point(meta, mode, nc, ver)
         nc.close()  
         
         del prodD
      
      # E 
      # F
      if (dp == 'flux-components'):
         import TData_products_F as prodF
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodF.flux_components(meta, mode, nc, ver)
         nc.close() 

         del prodF         
         
      if (dp == 'flux-estimates'):
         import TData_products_F as prodF
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodF.flux_estimates(meta, mode, nc, ver)
         nc.close() 
         
         del prodF
         
      if (dp == 'full-troposphere-temperature-profiles'):
         import TData_products_F as prodF
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodF.full_troposphere_temperature_profiles(meta, mode, nc, ver, vocab_ver)
         nc.close() 
         
         del prodF
         
      # G
      # H
      if (dp == 'h2-concentration'):
         import TData_products_H as prodH
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodH.h2_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodH
         
      if (dp == 'halocarbon-concentration'):
         import TData_products_H as prodH
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodH.halocarbon_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodH
      
      # I 
      if (dp == 'iwv-lwp'):
         import TData_products_I as prodI
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodI.iwv_lwp(meta, mode, nc, ver)
         nc.close()  
         
         del prodI
         
      # J
      # K
      # L
      if (dp == 'liquid-water-content'):
         import TData_products_L as prodL
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodL.liquid_water_content(meta, mode, nc, ver)
         nc.close()
         
         del prodL
      
      # M
      if (dp == 'mean-co2-h2o'):
         import TData_products_M as prodM
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodM.mean_co2_h2o(meta, mode, nc, ver)
         nc.close()

         del prodM         
         
      if (dp == 'mean-winds'):
         import TData_products_M as prodM
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodM.mean_winds(meta, mode, nc, ver)
         nc.close() 
         
         del prodM
         
      if (dp == 'mean-winds-profile'):
         import TData_products_M as prodM
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodM.mean_winds_profile(meta, mode, nc, ver, vocab_ver)
         nc.close() 
         
         del prodM
         
      if (dp == 'moisture-profiles'):
         import TData_products_M as prodM
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodM.moisture_profiles(meta, mode, nc, ver, vocab_ver)
         nc.close() 
         
         del prodM
         
      # N
      if (dp == 'n2o-concentration'):
         import TData_products_N as prodN
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodN.n2o_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodN
         
      if (dp == 'n2o-sf6-concentration'):
         import TData_products_N as prodN
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodN.n2o_sf6_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodN
         
      if (dp == 'no2-concentration'):
         import TData_products_N as prodN
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodN.no2_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodN
         
      if (dp == 'nox-noxy-concentration'):
         import TData_products_N as prodN
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodN.nox_noxy_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodN
      
      # O
      if (dp == 'o2-concentration'):
         import TData_products_O as prodO
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodO.o2_concentration(meta, mode, nc, ver)
         nc.close() 

         del prodO         
         
      if (dp == 'o2n2-concentration-ratio'):
         import TData_products_O as prodO
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodO.o2n2_concentration_ratio(meta, mode, nc, ver)
         nc.close() 
         
         del prodO
         
      if (dp == 'o3-concentration'):
         import TData_products_O as prodO
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodO.o3_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodO
         
      if (dp == 'o3-concentration-profile'):
         import TData_products_O as prodO
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodO.o3_concentration_profile(meta, mode, nc, ver, vocab_ver)
         nc.close() 
         
         del prodO
         
      if (dp == 'oh-concentration'):
         import TData_products_O as prodO
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodO.oh_concentration(meta, mode, nc, ver)
         nc.close()    

         del prodO         
      
      # P   
      if (dp == 'particle-size-distribution'):
         import TData_products_P as prodP
         if 'ncas-caps-1' in nm:
            # set up all naming options
            opt11 = 'cas'; opt21 = ''; opt31 = ''
            opt12 = 'cip'; opt22 = ''; opt32 = ''         
            
            # create nc file
            nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
            prodP.particle_size_distribution(nm, meta, mode, nc, ver)
            nc.close()
         
            # create nc file
            nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
            prodP.particle_size_distribution(nm, meta, mode, nc, ver)
            nc.close()
         else:
            # create nc file
            nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
            prodP.particle_size_distribution(nm, meta, mode, nc, ver)
            nc.close()
            
         del prodP
   
      if (dp == 'peroxyacetyl-nitrate-concentration'):
         import TData_products_P as prodP
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodP.peroxyacetyl_nitrate_concentration(meta, mode, nc, ver)
         nc.close()  
         
         del prodP
         
      if (dp == 'photolysis-frequencies'):
         import TData_products_P as prodP
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodP.photolysis_frequencies(meta, mode, nc, ver)
         nc.close() 
         
         del prodP
         
      if (dp == 'pm-concentration'):
         import TData_products_P as prodP
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodP.pm_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodP
         
      if (dp == 'precipitation'):
         import TData_products_P as prodP
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodP.precipitation(meta, mode, nc, ver)
         nc.close()
         
         del prodP
         
      # Q
      # R
      if (dp == 'radiation'):
         import TData_products_R as prodR
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodR.radiation(meta, mode, nc, ver)
         nc.close()  
         
         del prodR
         
      if (dp == 'radon-concentration'):
         import TData_products_R as prodR
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodR.radon_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodR
         
      if (dp == 'rain-lwc-velocity-reflectivity'):
         import TData_products_R as prodR
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodR.rain_lwc_velocity_reflectivity(meta, mode, nc, ver, vocab_ver)
         nc.close() 
         
         del prodR
         
      # S
      if (dp == 'sf6-concentration'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.sf6_concentration(meta, mode, nc, ver)
         nc.close() 

         del prodS         
         
      if (dp == 'size-concentration-spectra'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.size_concentration_spectra(meta, mode, nc, ver, vocab_ver)
         nc.close()

         del prodS         
         
      if (dp == 'snr-winds'):
         import TData_products_S as prodS
         # set up all naming options
         opt11 = 'high-range-mode'; opt21 = '15m'; opt31 = ''
         opt12 = 'low-range-mode'; opt22 = '15m'; opt32 = ''
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
         prodS.snr_winds(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
         prodS.snr_winds(meta, mode, nc, ver, vocab_ver)
         nc.close()
         
         del prodS
         
      if (dp == 'so2-concentration'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.so2_concentration(meta, mode, nc, ver)
         nc.close()

         del prodS         
         
      if (dp == 'soil'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.soil(meta, mode, nc, ver)
         nc.close()   
         
         del prodS
      
      if (dp == 'solar-actinic-flux'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.solar_actinic_flux(meta, mode, nc, ver)
         nc.close()  
         
         del prodS

      if (dp == 'sonde'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.sonde(meta, mode, nc, ver)
         nc.close()   
         
         del prodS

      if (dp == 'stability-indices'):
         import TData_products_S as prodS
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodS.stability_indices(meta, mode, nc, ver)
         nc.close() 

         del prodS         
       
      if (dp == 'surface-met'):
         import TData_products_S as prodS
         # set up all naming options
         opt11 = '10m'; opt21 = ''; opt31 = ''
         opt12 = '30m'; opt22 = ''; opt32 = ''
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt11, opt21, opt31, logfile, mode)
         prodS.surface_met(meta, mode, nc, ver)
         nc.close()
         
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt12, opt22, opt32, logfile, mode)
         prodS.surface_met(meta, mode, nc, ver)
         nc.close() 
         
         del prodS
           
      # T
      if (dp == 'tgm-concentration'):
         import TData_products_T as prodT
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodT.tgm_concentration(meta, mode, nc, ver)
         nc.close() 
         
         del prodT
      
      # U
      # V
      if (dp == 'voc-concentration'):
         import TData_products_V as prodV
         # create nc file
         nc = prod.create_NC_file(nm, dp, ver, opt1, opt2, opt3, logfile, mode)
         prodV.voc_concentration(meta, mode, nc, ver)
         nc.close()
         
         del prodV
         
      # W
      # X
      # Y
      # Z

def t_control(logfile):      
   # read in instrument\data product lookup table
   [name, name_product] = read_lookup(logfile)
 
   # read in and process config file   
   [mode, instrument, data_product, ver, vocab_ver] = read_config(logfile)
   print("Deployment mode: ", mode)
   print("Data Set Version: ", ver)
   print("Vocabulary Version: ", vocab_ver)
   
   # read in meta file
   df = read_meta(logfile, vocab_ver)
   
   # creat list of files
   run_list = create_runs(name, name_product, mode, instrument, data_product)
   
   # run through run list for each deployment mode
   for x in range (0, len(mode)):
      if ('all' in mode[x]):
         md = 'land'
         do_run(df, md, run_list, ver, logfile, vocab_ver)
         
         md = 'sea'
         do_run(df, md, run_list, ver, logfile, vocab_ver)
         
         md = 'air'
         do_run(df, md, run_list, ver, logfile, vocab_ver)
         
      if ('land' in mode[x]):
         md = 'land'
         do_run(df, md, run_list, ver, logfile, vocab_ver)
         
      if ('air' in mode[x]):
         md = 'air'
         do_run(df, md, run_list, ver, logfile, vocab_ver)
         
      if ('sea' in mode[x]):
         md = 'sea'
         do_run(df, md, run_list, ver, logfile, vocab_ver)