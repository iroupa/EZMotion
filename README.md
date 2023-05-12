# EZMotion
 
EZMotion_2D is a pure-Python tool to perform kinematic and dynamic analysis of mechanical and biomechanical multibody systems. <br>
<br>
## Dependencies

EZMotion requires the following libraries:

numpy (https://numpy.org/) <br>
scipy (https://scipy.org/) <br>
wxpython (https://www.wxpython.org/) <br>
pandas (https://pandas.pydata.org/)
<br>
## How to use

EZMotion_2D has a graphical user interface with two panels, ***Analysis*** and ***Visualization***.  

The ***Analysis*** panel has five sections (***Analysis Type***, ***Input Files Folder***, ***Analysis Parameters***, ***Export Files Messages***, ***Messages***) that allows the user to:


select the input files required to perform the selected analysis. 

![This is an image](/images/EZ_Motion_Analysis_Panel.png) <br> <br> 

   * ***Kinematic Analysis - Input Files:***  <br> 
     * Modeling file (.mod): Topology of the model<br> 
     * Initial state file (.q): Initial generalized coordinates of the multibody system<br> 
     * Input data file (.data): Labels associated to each driver of the multibody system<br> 
     * Drivers_Labels (.lbl): Data used to drive the model during the analysis<br><br>  
      
   * ***Forward Dynamic Analysis - Input Files:*** <br>
     * Modeling_File (.mod): Topology of the model<br> 
     * Initial state file (.q): Initial generalized coordinates of the multibody system<br> 
     * Initial state file (.qp): Initial generalized velocities of the multibody system<br> 
     * Force Files Folder: Path of the folder containing the force files to apply during the analysis<br> <br> 

   * ***Inverse Dynamic Analysis - Input Files:*** <br>
     * Modeling_File (.mod): Topology of the model<br> 
     * Initial state file (.q): Initial generalized coordinates of the multibody system<br> 
     * Initial state file (.qp): Initial generalized velocities of the multibody system<br> 
     * Force Files Folder: Path of the folder containing the force files to apply during the analysis<br> 
     * Input data file (.data): Labels associated to each driver of the multibody system<br> 
     * Drivers_Labels (.lbl): Data used to drive the model during the analysis<br> 
     * Muscles database (.msk): File containing the muscle parameters <br> <br> 


