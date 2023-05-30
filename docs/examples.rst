Examples
============

This section includes examples of the input files required to perform the forward and inverse dynamic analysis of distinct multibody systems. 

Forward Dynamic Analysis
~~~~~~~~~~~~~~~~~~~~~~~~ 

Single Pendulum
---------------

This model is composed by a body with unitary mass (m = 1 kg) connected to the ground through a link with unitary length (L_1 = 1 m) that connects the ground via a double support joint. For the forward dynamics simulation, the system moves only under the effect of gravity with zero initial velocity. The pendulum starts in a horizontal position with the body’s center of mass located at coordinates P_2=[-1, 0]

.. figure:: .\\images\\single_pendulum.png
	:scale: 15 %
	:align: center
	:alt: Representation of the single pendulum mechanism

	Fig 1.  Representation of the single pendulum mechanism. 

Modeling File
***********

.. csv-table:: Example of single pendulum modeling file (.mod)
   :file: .\\csv\\single_pendulum_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File (position)
***********

.. csv-table:: Example of single pendulum state file (.q)
   :file: .\\csv\\single_pendulum_q_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

State File (velocity)
***********

.. csv-table:: Example of single pendulum state file (.qp)
   :file: .\\csv\\single_pendulum_qp_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1


Slider-Crank
------------

The slider crank mechanism is composed by two identical rods (L_1 and L_2) with unitary length, a uniformly distributed mass of 1kg and a square cross section of 0.01m2, which are constrained in P_2 by a revolute joint. The slider is considered to be massless and no friction with the ground is considered. A ``translation-revolute`` joint is introduced between body L_2 and the ground, such that point P_3 is constrained to move only along the x axis. The system moves under gravity effect from the initial position, represented in Fig. 2, to which corresponds θ=π⁄4. The initial velocity of point P_3 is defined as 4 m.s-1 in the negative direction of the horizontal x axis.

.. figure:: .\\images\\slider_crank.png
	:scale: 15 %
	:align: center
	:alt: Representation of the slider-crank mechanism

	Fig 2.  Representation of the slider-crank mechanism. 

Modeling File
***********

.. csv-table:: Example of single pendulum modeling file (.mod)
   :file: .\\csv\\slider_crank_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File (position)
***********

.. csv-table:: Example of single pendulum state file (.q)
   :file: .\\csv\\slider_crank_q_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

State File (velocity)
***********

.. csv-table:: Example of single pendulum state file (.qp)
   :file: .\\csv\\slider_crank_qp_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1


Inverse Dynamic Analysis
~~~~~~~~~~~~~~~~~~~~~~~~ 

Double Pendulum 
------------

This model is composed of ``[...]``

.. figure:: .\\images\\double_pendulum.png
	:scale: 15 %
	:align: center
	:alt: Representation of the double pendulum mechanism

	Fig 3.  Representation of the double pendulum mechanism. 


Modeling File
***********

.. csv-table:: Example of double pendulum modeling file (.mod)
   :file: .\\csv\\double_pendulum_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of double pendulum state file (.q)
   :file: .\\csv\\double_pendulum_q_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of double pendulum data file (.qp)
   :file: .\\csv\\double_pendulum_data_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of double pendulum labels file (.qp)
   :file: .\\csv\\double_pendulum_labels_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Single Body 
------------

This model is composed of ``[...]``

.. figure:: .\\images\\single_body.png
	:scale: 15 %
	:align: center
	:alt: Representation of the single body

	Fig 4.  Representation of the single body. 

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

Modeling File
***********

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of single body state file (.q)
   :file: .\\csv\\single_body_q_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of single body data file (.qp)
   :file: .\\csv\\single_body_data_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of single body labels file (.qp)
   :file: .\\csv\\single_body_labels_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Lower Body
------------

This model is composed of ``[...]``

.. figure:: .\\images\\lower_body.png
	:scale: 15 %
	:align: center
	:alt: Representation of the lower body

	Fig 5.  Representation of the lower body. 

Modeling File
***********

.. csv-table:: Example of lower body modeling file (.mod)
   :file: .\\csv\\lower_body_modeling_file.csv
   :align: center
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of lower body state file (.q)
   :file: .\\csv\\lower_body_q_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of lower body data file (.qp)
   :file: .\\csv\\lower_body_data_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of lower body labels file (.qp)
   :file: .\\csv\\lower_body_labels_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

Force File
***********

.. csv-table:: Example of lower body labels file (.qp)
   :file: .\\csv\\lower_body_force_file.csv
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1