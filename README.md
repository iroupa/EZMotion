# EZMotion

EZMotion is a Python tool that provides an easy and intuitive way to model and perform kinematic and dynamic analyses of planar multibody systems without requiring coding skills and visualize its outputs. The current implementation has been developed in Python 3, and its outputs have been validated against those available in the IFToMM library of computational benchmark problems [1].
<br>
<br>


## Dependencies

EZMotion requires the following libraries:

numpy (https://numpy.org/) <br>
scipy (https://scipy.org/) <br>
wxpython (https://www.wxpython.org/) <br>
pandas (https://pandas.pydata.org/)
<br>
## How to use

EZMotion has a graphical user interface with two panels, ***Analysis*** and ***Visualization*** that allows to run or visualize the outputs of a kinematic or dynamic analysis. A detailed description of how to use EZ_Motion, the required files and how to implement customized models is available in folder provided in the folder ***Docs***.
### ***Analysis*** panel <br>

![This is an image](/images/EZ_Motion_Analysis_Panel.png) <br> <br> 

The ***Analysis*** panel has distinct sections that allows to: <br>
 * Select the type of analysis: ***Analysis Type***
 * Select the input files folder: ***Input Files Folder***
 * Select the input files: ***Input Files***
 * Define the parameters of the analysis: ***Analysis Parameters***, 
 * Select the output files folder: ***Export Files*** 
 * Obtain analysis feedback: ***Messages***  <br> 



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


