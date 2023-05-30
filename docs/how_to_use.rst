How to use
============

``EZMotion`` has a graphical user interface with two panels, ``Analysis`` (see Figure 1) and ``Visualization`` (see Figure 2), that allows to perform the kinematic or dynamic analysis or to visualize and export the analysis outputs. A description of how to use both is presented below. 

Run Analysis
************

To run an analysis, is it necessary to select the required input files and then press the ``Run Analysis`` button. The output file (``.out`` extension) will be exported to the folder selected on the ``Export Files`` section.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel
   
   Fig 1. EZMotion: Analysis Panel.

The ``Analysis Type`` section allows to select one of the following type of analysis to perform: ``Kinematic``, ``Inverse Dynamic``, ``Forward Dynamic`` or ``Musculoskeletal``. According to the selection the number of fields in the ``Input Files`` section will be updated.  

The ``Input Files Folder`` section allows to select the folder in which the input files for the seleted analysis are located. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select the input files in the ``Input Files`` section.

The ``Analysis Parameters`` section allows to select the initial and final timeof th eanalyis as well as its sampling frequency. The subject mass will be used to normalize the dynamic outputs of the analysis, such as the joint moments or joint power of the model. 

The ``Export Files`` section allows to select the folder to which the outputs of the analysis will be exported. This field is automatically updated when the ``Input Files Folder`` section is updated.

The ``Messages`` section provides a feedback about the evolution of the analysis.
	
Visualize Outputs
************
		
The ``Visualization Panel``	comprises two resizable panels. In the left  the input files and the variable to plot ``(Plot Data > Variable)`` are selected, while in the right one the model and the selected variable are plotted. To start the animation, it is necessary to press the ``Show Model`` button. 		
		
The ``Input Files Folder`` section allows to select the folder in which the input files for the seleted analysis are located. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select the input files in the ``Input Files`` section.
			
The ``Plot Data`` section allows to select the variable of the model that will be presented in the lower right plot. Moreover, it also allows to present the raw or filtered data of the variable. For that purpose, it is necessary to select the ``Yes`` option on the ``Plot Data > Filter Data`` and select the pretended cuttoff frequency in Hz.

The ``Outputs`` section allows to select the folder to which the variable presented on the lower right plot may be exported.

The ``Messages`` section alerts the user in case an error occurred during the visualization of the outputs.

.. figure:: .\\images\\EZ_Motion_Viz_Panel.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel

	Fig 2. EZMotion: Visualization Panel.

To export the variable presented on the lower right plot side to a new file ``(.csv extension)``, it is necessary to select the 'Yes' option on the ``Outputs > Export Outputs`` section (see Figure 3). Next, the initial and the final frame of the analysis must be defined as well as if the variable will be normalized (n = 101 samples).
		
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Export_Outputs.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel

	Fig 3. EZMotion: Visualization Panel.