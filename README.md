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

### ***Analysis*** panel <br>

![This is an image](/images/EZ_Motion_Analysis_Panel.png) <br> <br> 

The ***Analysis*** panel has distinct sections that allows to: <br>
 * Select the type of analysis: ***Analysis Type***
 * Select the input files folder: ***Input Files Folder***
 * Select the input files: ***Input Files***
 * Define the parameters of the analysis: ***Analysis Parameters***, 
 * Select the output files folder: ***Export Files*** 
 * Obtain analysis feedback: ***Messages*** 



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


