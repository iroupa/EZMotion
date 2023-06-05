Examples
============

This section includes examples of the input files required to perform the forward and inverse dynamic analysis of distinct multibody systems. 

Forward Dynamic Analysis
~~~~~~~~~~~~~~~~~~~~~~~~ 

Single Pendulum
---------------

This model is composed by a body with unitary mass (m = 1 kg) connected to the ground through a link with unitary length (L1 = 1 m) that connects the ground via a double support joint [1]. For the forward dynamics simulation, the system moves only under the effect of gravity with zero initial velocity. The pendulum starts in a horizontal position with the body’s center of mass located at coordinates P2 = [-1, 0]

.. figure:: .\\images\\single_pendulum.png
	:scale: 15 %
	:align: center
	:alt: Representation of the single pendulum mechanism

	Fig 1.  Representation of the single pendulum mechanism. 

Modeling File
***********

.. csv-table:: Example of single pendulum modeling file (.mod)
   :file: .\\csv\\single_pendulum_model\\single_pendulum_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File (position)
***********

.. csv-table:: Example of single pendulum state file (.q)
   :file: .\\csv\\single_pendulum_model\\single_pendulum_q_file.csv
   :escape: '
   :align: center
   :widths: 25 25 25 25
   :header-rows: 1

State File (velocity)
***********

.. csv-table:: Example of single pendulum state file (.qp)
   :file: .\\csv\\single_pendulum_model\\single_pendulum_qp_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1


Slider-Crank
------------

The slider crank mechanism is composed by two identical rods (L1 and L2) with unitary length, a uniformly distributed mass of 1 kg and a square cross section of 0.01 m2, which are constrained in P2 by a revolute joint. The slider is considered to be massless and no friction with the ground is considered [1]. A single support joint is introduced, such that point P3 is constrained to move only along the *x* axis. The system moves under gravity effect from the initial position, represented in Fig. 2, to which corresponds θ=π⁄4. The initial velocity of point P3 is defined as 4 m.s-1 in the negative direction of the horizontal *x* axis.

.. figure:: .\\images\\slider_crank.png
	:scale: 15 %
	:align: center
	:alt: Representation of the slider-crank mechanism

	Fig 2.  Representation of the slider-crank mechanism. 

Modeling File
***********

.. csv-table:: Example of the slider-crank modeling file (.mod)
   :file: .\\csv\\slider_crank_model\\slider_crank_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File (position)
***********

.. csv-table:: Example of the slider-crank state file (.q)
   :file: .\\csv\\slider_crank_model\\slider_crank_q_file.csv
   :align: center
   :escape: '
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 1

State File (velocity)
***********

.. csv-table:: Example of the slider-crank state file (.qp)
   :file: .\\csv\\slider_crank_model\\slider_crank_qp_file.csv
   :align: center
   :escape: '
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 1

Kinematic Analysis
~~~~~~~~~~~~~~~~~~ 

Single Body
------------

This model is composed of a single segment that moves along the *x* axis of the global reference frame. 
The system starts in a diagonal position with respect to the global reference frame (θ=π⁄8 w) with its center of mass located at coordinates P1 = [-1, 0]. No external forces are applied to the system during the analysis.


.. figure:: .\\images\\single_body.png
	:scale: 15 %
	:align: center
	:alt: Representation of the single body

	Fig 4.  Representation of the single body. 

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

Modeling File
***********

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_model\\single_body_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of single body state file (.q)
   :file: .\\csv\\single_body_model\\single_body_q_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of single body data file (.data)
   :file: .\\csv\\single_body_model\\single_body_data_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of single body labels file (.lbl)
   :file: .\\csv\\single_body_model\\single_body_labels_file.csv
   :align: center
   :escape: '
   :widths: 50 50
   :header-rows: 1

Lower Body ``[Update model description and input files]``
------------

This model depicts the lower body of the human body and is composed of six segments (feet, legs and thighs) connected by revolute joints. 
The center of the hip, knee and ankle joint centers joint was defined as proposed by Wu et al. [3]. The inertial parameters were defined according to Dempster et al ``[2]``. 
The ground reaction forces measured during the gait cycle using several force plates were applied in the analysis using the *.f* files presented below.
 
.. figure:: .\\images\\lower_body.png
	:scale: 15 %
	:align: center
	:alt: Representation of the lower body

	Fig 5.  Representation of the lower body (right limb - green, left limb - red, external forceapplied in the model - purple). 

Modeling File
***********

.. csv-table:: Example of lower body modeling file (.mod)
   :file: .\\csv\\lower_body_model\\lower_body_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of lower body state file (.q)
   :file: .\\csv\\lower_body_model\\lower_body_q_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of lower body data file (.data)
   :file: .\\csv\\lower_body_model\\lower_body_data_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of lower body labels file (.lbl)
   :file: .\\csv\\lower_body_model\\lower_body_labels_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Force File
***********

.. csv-table:: Example of lower body labels file (.f)
   :file: .\\csv\\lower_body_model\\lower_body_force_file.csv
   :align: center
   :escape: '  
   :widths: 15 15 15 15 15 15 15
   :header-rows: 1

Inverse Dynamic Analysis
~~~~~~~~~~~~~~~~~~~~~~~~ 


Double Pendulum
---------------

``This model is composed of a single segment that moves along the *x* axis of the global reference frame. 
The system starts in a diagonal position with respect to the global reference frame (θ=π⁄8 w) with its center of mass located at coordinates P1 = [-1, 0]. No external forces are applied to the system during the analysis.


.. figure:: .\\images\\single_body.png
	:scale: 15 %
	:align: center
	:alt: Representation of the single body

	Fig 4.  Representation of the single body. 

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

Modeling File
***********

.. csv-table:: Example of single body modeling file (.mod)
   :file: .\\csv\\single_body_model\\single_body_modeling_file.csv
   :align: center
   :escape: '
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

State File
***********

.. csv-table:: Example of single body state file (.q)
   :file: .\\csv\\single_body_model\\single_body_q_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Data File
***********

.. csv-table:: Example of single body data file (.data)
   :file: .\\csv\\single_body_model\\single_body_data_file.csv
   :align: center
   :escape: '
   :widths: 25 25 25 25
   :header-rows: 1

Labels File
***********

.. csv-table:: Example of single body labels file (.lbl)
   :file: .\\csv\\single_body_model\\single_body_labels_file.csv
   :align: center
   :escape: '
   :widths: 50 50
   :header-rows: 1``[

   
References
*************************

[1] IFToMM technical committee for multibody dynamics, library of computational benchmark problems, (2022).

[2] Dempster, *The anthropometry of the manual work space for the seated subject*, Am. J. Phys. Anthropol. 17 (1959) 289, https://doi.org/10.1002/ ajpa.1330170405.

[3] G. Wu, S. Sieglerb, P. Alard, C. Kirtley, A. Leardini, D. Rosenbaum, M. Whittle, D.D. D’Lima, L. Cristofolinii, H. Wittej, O. Schmid, S. Siegler, P. Allard, C. Kirtley, A. Leardini, D. Rosenbaum, M. Whittle, D.D. D’Lima, L. Cristofolini, H. Witte, O. Schmid, I. Stokes, *ISB recommendation on definitions of joint coordinate system of various joints for the reporting of human joint motion—part I: ankle, hip, and spine*, J. Biomech. 35 (2002) 543–548. https://doi.org/10.1016/S0021-9290(01)00222-6.