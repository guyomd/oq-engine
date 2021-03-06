Classical Hazard QA Test, Case 2
================================

============== ===================
checksum32     2,848,891,951      
date           2019-07-30T15:04:31
engine_version 3.7.0-git3b3dff46da
============== ===================

num_sites = 1, num_levels = 4, num_rlzs = 1

Parameters
----------
=============================== ==================
calculation_mode                'preclassical'    
number_of_logic_tree_samples    0                 
maximum_distance                {'default': 200.0}
investigation_time              1.0               
ses_per_logic_tree_path         1                 
truncation_level                0.0               
rupture_mesh_spacing            1.0               
complex_fault_mesh_spacing      1.0               
width_of_mfd_bin                0.001             
area_source_discretization      None              
ground_motion_correlation_model None              
minimum_intensity               {}                
random_seed                     1066              
master_seed                     0                 
ses_seed                        42                
=============================== ==================

Input files
-----------
========================= ============================================================
Name                      File                                                        
========================= ============================================================
gsim_logic_tree           `gsim_logic_tree.xml <gsim_logic_tree.xml>`_                
job_ini                   `job.ini <job.ini>`_                                        
reqv:active shallow crust `lookup_asc.hdf5 <lookup_asc.hdf5>`_                        
reqv:stable shallow crust `lookup_sta.hdf5 <lookup_sta.hdf5>`_                        
source_model_logic_tree   `source_model_logic_tree.xml <source_model_logic_tree.xml>`_
========================= ============================================================

Composite source model
----------------------
========= ======= =============== ================
smlt_path weight  gsim_logic_tree num_realizations
========= ======= =============== ================
b1        1.00000 trivial(1,1)    1               
========= ======= =============== ================

Required parameters per tectonic region type
--------------------------------------------
====== ================== ========= ========== ==========
grp_id gsims              distances siteparams ruptparams
====== ================== ========= ========== ==========
0      '[SadighEtAl1997]' rrup      vs30       mag rake  
1      '[SadighEtAl1997]' rrup      vs30       mag rake  
====== ================== ========= ========== ==========

Realizations per (GRP, GSIM)
----------------------------

::

  <RlzsAssoc(size=2, rlzs=1)>

Number of ruptures per tectonic region type
-------------------------------------------
================ ====== ==================== ============ ============
source_model     grp_id trt                  eff_ruptures tot_ruptures
================ ====== ==================== ============ ============
source_model.xml 0      Active Shallow Crust 3,000        3,000       
source_model.xml 1      Stable Shallow Crust 3,000        3,000       
================ ====== ==================== ============ ============

============= =====
#TRT models   2    
#eff_ruptures 6,000
#tot_ruptures 6,000
============= =====

Slowest sources
---------------
========= ====== ==== ============ ========= ========= ====== =======
source_id grp_id code num_ruptures calc_time num_sites weight speed  
========= ====== ==== ============ ========= ========= ====== =======
2         1      P    3,000        0.00537   1.00000   3,000  558,645
1         0      P    3,000        0.00518   1.00000   3,000  579,164
========= ====== ==== ============ ========= ========= ====== =======

Computation times by source typology
------------------------------------
==== ========= ======
code calc_time counts
==== ========= ======
P    0.01055   2     
==== ========= ======

Information about the tasks
---------------------------
================== ======= ========= ======= ======= =======
operation-duration mean    stddev    min     max     outputs
preclassical       0.00561 1.229E-04 0.00552 0.00569 2      
read_source_models 0.00607 NaN       0.00607 0.00607 1      
================== ======= ========= ======= ======= =======

Data transfer
-------------
================== ========================================================= ========
task               sent                                                      received
preclassical       params=441.09 KB srcs=2.34 KB srcfilter=440 B gsims=294 B 684 B   
read_source_models converter=306 B fnames=99 B                               2.06 KB 
================== ========================================================= ========

Slowest operations
------------------
======================== ========= ========= ======
calc_15545               time_sec  memory_mb counts
======================== ========= ========= ======
total preclassical       0.01121   0.0       2     
total read_source_models 0.00607   0.0       1     
managing sources         0.00559   0.0       1     
store source_info        0.00204   0.0       1     
aggregate curves         2.851E-04 0.0       2     
======================== ========= ========= ======