Input Files
========

For each type of analysis, the list of inputs files, its extension and description are presented below. A detailed description of each file and is availbale at <link>

Kinematic Analysis
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
***********
.. list-table:: Input Files
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
   * - Force Files Folder
     - 
     - Path of the folder containing the force files to apply during the analysis

Forward Dynamic Analysis
***********
.. list-table:: Input Files
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
   * - Force Files Folder
     - 
     - Path of the folder containing the force files to apply during the analysis

Musculoskeletal Analysis
***********
.. list-table:: Input Files
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
   * - Force Files Folder
     - 
     - Path of the folder containing the force files to apply during the analysis
  * - Muscle Files
     - .msk
     - File containing the muscle parameters
	 
Vizualization
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
     - External forces applied drng the analysis     
   * - Muscles
     - .msk
     - File containing the muscle parameters