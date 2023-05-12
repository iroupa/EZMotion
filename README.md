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

EZMotion_2D has a graphical user interface with two panels, ***Analysis*** and ***Visualization***, that allow the user to select the input files required to perform a kinematic or dynamic analysis or to visualize the outputs of such analysis. 

The ***Analysis*** panel allows to perform the following analysis: <br> 
* #### Kinematic Analysis: Input Files:   <br>
  #### Modeling file (.mod): Topology of the model
  #### Initial state file (.q) Initial generalized coordinates of the system
  #### Input data file (.data) Labels associated to each driver of the system
  #### Drives_Labels (.lbl) Data used to drive the model during the analysis
    
  
* Inverse Dynamic Analysis <br> 
* Forward Dynamic Analysis <br> 

To perform a *** Kinematic Analysis *** the following input files are required <br> 

