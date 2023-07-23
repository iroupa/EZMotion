Input Files
========

For each type of analysis, the list of inputs files needed, their extension and their description are presented below. 

Kinematic Analysis
******************
.. list-table:: Table 1. Kinematic Analysis - Input Files
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Extension
     - Description
   * - Modeling File
     - .mod
     - Topology of the model
   * - Modeling State
     - .q
     - Generalized coordinates of the system for the initial time
   * - Drivers Labels
     - .lbl
     - Labels associated to each driver of the system
   * - Model Data
     - .data
     - Data used to drive the model during the analysis  

Inverse Dynamic Analysis
************************
.. list-table:: Table 2. Inverse Dynamic Analysis - Input Files
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Extension
     - Description
   * - Modeling File
     - .mod
     - Topology of the model
   * - Modeling State
     - .q
     - Generalized coordinates of the system for the initial time
   * - Drivers Labels
     - .lbl
     - Labels associated to each driver of the system
   * - Model Data
     - .data
     - Data used to drive the model during the analysis      
   * - Force Files 
     - .f
     - External force files to apply during the analysis

Forward Dynamic Analysis
************************
.. list-table:: Table 1. Forward Dynamic Analysis - Input Files
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Extension
     - Description
   * - Modeling File
     - .mod
     - Topology of the model
   * - Modeling State
     - .q
     - Generalized coordinates of the system for the initial time
   * - Modeling State
     - .qp
     - Generalized velocities of the system for the initial time
   * - Force Files
     - .f
     - External force files to apply during the analysis

Musculoskeletal Analysis
************************
.. list-table:: Table 4. Musculoskeletal Analysis - Input Files
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Extension
     - Description
   * - Modeling File
     - .mod
     - Topology of the model
   * - Modeling State
     - .q
     - Generalized coordinates of the system for the initial time
   * - Drivers Labels
     - .lbl
     - Labels associated to each driver of the system
   * - Model Dat
     - .data
     - Data used to drive the model during the analysis     
   * - Model Dat
     - .data
     - Data used to drive the model during the analysis     
   * - Force Files
     - .f
     - External force files to apply during the analysis
  * - Muscle Files
     - .msk
     - File containing the muscle parameters
	 
Visualization
**********
.. list-table:: Input Files
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Extension
     - Description
   * - Modeling File
     - .mod
     - Topology of the model
   * - Outputs File
     - .out
     - Kinematic and dynamic analysis variables 
   * - Experimental Markers
     - .mkr
     - Cartesian coordinates of the markers used during the experimental acquisition
   * - Segments Local Coordinates
     - .jt
     - Local coordinates of the extremities of each segment of the model     
   * - External forces
     - .f
     - External forces applied during the analysis     
   * - Muscles
     - .msk
     - File containing the muscle parameters