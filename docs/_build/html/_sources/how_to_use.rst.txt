How to use
==========

``EZMotion`` has a graphical user interface with two panels, ``Analysis`` (see Figure 1) and ``Visualization`` (see Figure 9), which  allow performing kinematic or dynamic analyses and visualizing and exporting the analysis outputs, respectively. A description on how to use both panels is presented below. 

Run Analysis
~~~~~~~~~~~~ 

The ``Analysis`` panel (see Figure 1) is composed of several sections with distinct functions (see Table 1)

.. figure:: .\\images\\EZ_Motion_Analysis_Panel.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel
   
   Fig 1. EZMotion: Analysis Panel.

.. list-table:: Table 1. Analysis Panel Sections
   :widths: 20 80
   :header-rows: 1

   * - Name
     - Description
   * - Analysis Type
     - Select type of analysis (kinematic, forward dynamic, inverse dynamic or musculoskeletal) 
   * - Input Files Folder
     - Select the input files required to perform the selected anaysis .
   * - Analysis Parameters
     - Set the initial and final time for the selected analysis, as well as its sampling frequency and the subjet bodymass. 
   * - Export Files
     - Select the path of the folder to which the outputs file will be exported. 
   * - Run Analysis
     - Start the selected analysis.  
   * - Messages
     - Provide feedback about the analysis.  
 
To run an analysis, the user needs to follow the following steps: 

**1. Step: Select the type of analysis to perform.**
----------------------------------------------------
  
The ``Analysis Type > Analysis`` option allows to select one of the following type of analysis: ``Kinematic``, ``Inverse Dynamic``, ``Forward Dynamic`` or ``Musculoskeletal``. According to the selection the number of fields in the ``Input Files`` section will be updated.  

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Analysis_Type.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Analysis Type Section
   
   Fig 2. EZMotion: Analysis Panel - Analysis Type Section.


**2. Step: Select the folder containing the input files for the analysis defined in step #1. (optional)**  
----------------------------------------------------

The ``Input Files Folder > Input Files Folder`` option allows to select the folder in which the ``input files`` for the selected analysis are located. The list of input files required for each type of analysis and their detailed description is provided in :doc:`Input Files </input_files>` and :doc:`Modeling </modeling>` sections, respectively. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select such input files.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Input_Files_Folder.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Input Files Folder Section
   
   Fig 3. EZMotion: Analysis Panel - Input Files Folder Section.

**3. Step: Choose the input files for the type of analysis in step defined #1.** 
----------------------------------------------------
 
This step is performed automatically during step #2. However, the user can select each file manually, by using the selection tool available on the right side of the section. 

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Input_Files.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Input Files Section
   
   Fig 4. EZMotion: Analysis Panel - Input Files Section.

**4. Step: Set the initial and final time, sampling frequency and subject bodymass for the analysis defined in step #1.**  
----------------------------------------------------

The ``Analysis Parameters`` section allows to select the initial (``Analysis Parameters > Initial Time (s)``) and final time (``Analysis Parameters > Final Time (s)``) of the analysis as well as its sampling frequency (``Analysis Parameters > Sampling Frequency (Hz)``). The subject bodymass (``Analysis Parameters > Subject Bodymass (kg)``) will be used to normalize the dynamic outputs of the analysis, such as the ``joint moments`` or ``joint power`` of the model. By default, this value is set to 1 kg.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Analysis_Parameters.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Analysis Parameters Section
   
   Fig 5. EZMotion: Analysis Panel - Analysis Parameters Section.

**5. Step: Select the path of the folder to which the outputs file** ``(.out)`` **of the analysis defined in step #1 will be exported.**  
-----------------------------------------------

The ``Export Files > Outputs Folder`` option is automatically updated when the input files folder is selected. However, it can be manually defined by the user.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Export_Files.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Export Files Section
   
   Fig 6. EZMotion: Analysis Panel - Export Files Section.

**6. Step: Run Analysis**
-------------------------

To start the analysis the user must press the ``Run Analysis`` button.

.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Run_Analysis_Button.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Run Analysis Section
   
   Fig 7. EZMotion: Analysis Panel - Run Analysis Section.

**7. Step: View analysis feedback**
-----------------------------------

The ``Messages`` section provides a feedback about the evolution of the analysis.
	
.. figure:: .\\images\\EZ_Motion_Analysis_Panel_Messages.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Messages Section
   
   Fig 8. EZMotion: Analysis Panel - Messages Section.
	
	
Visualize Outputs
~~~~~~~~~~~~~~~~~ 
		
The ``Visualization Panel``	comprises two resizable panels (see Figure 9). In the left panel, composed of several sections (see Table 2) with distinct functions  the input files and the variable to plot are selected, while in the right panel the model and the selected variable are plotted. 
				
.. figure:: .\\images\\EZ_Motion_Viz_Panel.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel

	Fig 9. EZMotion: Visualization Panel. ``[Insert model and plot on right panel]``

.. list-table:: Table 2. Visualize Panel Sections
   :widths: 20 80
   :header-rows: 1

   * - Name
     - Description
   * - Input Files Folder
     - Select the input files folder.
   * - Input Files 
     - Select the input files required to visualize the analysis outputs.
   * - Plot Data
     - Select the variable to plot. 
   * - Show Model
     - Start the animation.  
   * - Outputs
     - Export the selected variable (raw or normalized) into a new file ``(.csv)``. 
   * - Messages
     - Provide feedback about the analysis.  

To visualize the analysis, the user needs to follow the following steps: 

To start the animation, it is necessary to press the ``Show Model`` button. 		

**1. Step: Select the folder containing the input files for the animation. (optional)**
----------------------------------------------------
				
The ``Input Files Folder > Input Files Folder`` option allows to select the folder in which the input files for the animation are located. By selecting a specific folder, the input fields in the ``Input Files`` section (see Figure 4) will be automatically updated. However, it is also possible to manually select such input files.
			
		
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Input_Files_Folder.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Visualization Panel - Input Files Folder.
   
   Fig 10. EZMotion: Visualization Panel - Input Files Folder.	
			
**2. Step: Select the input files for the analysis defined in step #1. (mandatory)**  
----------------------------------------------------

The ``Input Files Folder > Input Files Folder`` option allows to select the folder in which the ``input files`` for the selected analysis are located. The list of input files required for each type of analysis and their detailed description is provided in :doc:`Input Files </input_files>` and :doc:`Modeling </modeling>` sections, respectively. By selecting a specific folder, the input fields in the ``Input Files`` section will be automatically updated. However, it is also possible to manually select such input files.
		
.. figure:: .\\images\\EZ_Motion_Viz_Panel.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Analysis Panel - Input Files Section
   
   Fig 11. EZMotion: Visualizatiom Panel - Input Files Section.
	
**3. Step: Select the variable to plot. mandatory)**  
----------------------------------------------------		
			
The ``Plot Data > Variable`` option allows to select the variable of the model, available in the outputs file (``.out``), that will be presented in the lower right plot. 
By selecting the ``Plot Data > Filter Data > Yes`` option it is possible to plot the filtered data of the variable (see Figure 3). For that purpose, it is necessary to set the  cuttoff frequency in Hz in the ``Plot Data > Filter Frequency (Hz)`` option and press the ``Show Model`` button.
				
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Plot_Data.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel - Plot data

	Fig 12. EZMotion: Visualization Panel - Plot data


**4. Step: Export plotted variable. (optional)**  
----------------------------------------------------	

The ``Outputs`` section allows to select the folder to which the variable presented on the lower right plot will be exported. For that purpose it is necessary to select the ``Outputs > Export Outputs > Yes`` option (see Figure 13). Next, the user must define the initial ``Outputs > Initial Frame`` and final frame ``Outputs > End Frame`` of the analysis. If requested, the time variable may be normalized between 0 and 100 % ``Outputs > Normalized``.
		
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Export_Outputs.png
	:scale: 75 %
	:align: center
	:alt: EZMotion: Visualization Panel - Export Outputs Section

	Fig 13. EZMotion: Visualization Panel - Export Outputs Section.
	
	
**5. Step: View feedback (optional)**
-----------------------------------

The ``Messages`` section alerts the user in case an error occurs during the visualization of the outputs.
	
.. figure:: .\\images\\EZ_Motion_Viz_Panel_Messages.png
   :scale: 75 %
   :align: center
   :alt: EZMotion: Visualization Panel - Messages Section
   
   Fig 14. EZMotion: Visualization Panel - Messages Section.