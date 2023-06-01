How to use
==========

``EZMotion`` has a graphical user interface with two panels, ``Analysis`` (see Figure 1) and ``Visualization`` (see Figure 2), which  allow performing kinematic or dynamic analyses and visualizing and exporting the analysis outputs, respectively. A description on how to use both panels is presented below. 

Run Analysis
************

To run an analysis, the user needs to select the required input files and then press the ``Run Analysis`` button. The output file (``.out`` extension) will be exported to the folder selected on the ``Export Files > Outputs Folder`` option.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel
   
   Fig 1. EZMotion: Analysis Panel.

The ``Analysis Type > Analysis`` option allows to select one of the following type of analysis: ``Kinematic``, ``Inverse Dynamic``, ``Forward Dynamic`` or ``Musculoskeletal``. According to the selection the number of fields in the ``Input Files`` section will be updated.  

The ``Input Files Folder > Input Files Folder`` option allows to select the folder in which the ``input files`` for the selected analysis are located. The list of input files required for each type of analysis and their detailed description is provided in :doc:`Input Files </input_files>` and :doc:`Modeling </modeling>` sections, respectively. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select such input files.

The ``Analysis Parameters`` section allows to select the initial (``Analysis Parameters > Initial Time (s)``) and final time (``Analysis Parameters > Final Time (s)``) of the analysis as well as its sampling frequency (``Analysis Parameters > Sampling Frequency (Hz)``). The subject mass will be used to normalize the dynamic outputs of the analysis, such as the ``joint moments`` or ``joint power`` of the model. 

The ``Export Files > Outputs Folder`` option allows to select the folder to which the outputs of the analysis will be exported. This field is automatically updated when the ``Input Files Folder`` section is updated.

The ``Messages`` section provides a feedback about the evolution of the analysis.
	
Visualize Outputs
************
		
The ``Visualization Panel``	comprises two resizable panels. In the left panel, the input files and the variable to plot ``(Plot Data > Variable)`` are selected, while in the right panel the model and the selected variable are plotted. To start the animation, it is necessary to press the ``Show Model`` button. 		
				
.. figure:: .\\images\\EZ_Motion_Viz_Panel.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel

	Fig 2. EZMotion: Visualization Panel.
				
The ``Input Files Folder > Input Files Folder`` option allows to select the folder in which the input files for the selected analysis are located. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select such input files.
			
The ``Plot Data > Variable`` option allows to select the variable of the model, available in the (``.out`` file), that will be presented in the lower right plot. 
Moreover, by selecting the ``Plot Data > Filter Data > Yes`` option it is possible to plot the filtered data of the variable (see Figure 3). For that purpose, it is necessary to set the  cuttoff frequency in Hz in the ``Plot Data > Filter Frequency (Hz)`` option and press the ``Show Model`` button.
				
				
				
				
				
.. figure:: .\\images\\EZ_Motion_Viz_Panel_plot_data_filtered.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel - Plot data

	Fig 3. EZMotion: Visualization Panel - Plot data

The ``Outputs`` section allows to select the folder to which the variable presented on the lower right plot will be exported. For that purpose it is necessary to select the ``Outputs > Export Outputs > Yes`` option (see Figure 4). Next, the user must define the initial ``Outputs > Initial Frame`` and final frame ``Outputs > End Frame`` of the analysis. If requested, the time variable may be normalized between 0 and 100 ``Outputs > Normalized``.
		
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Export_Outputs.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel

	Fig 4. EZMotion: Visualization Panel.
	
The ``Messages`` section alerts the user in case an error occurs during the visualization of the outputs.

	
	
	
	
	