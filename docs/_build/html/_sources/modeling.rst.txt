Modeling
============

``Multibody systems`` (MBS) are composed of a collection of bodies interconnected to each other by different types of joints, which constrain their motion, and acted upon by forces of different origins [1].

To model the components of these systems, such as ``segments`` and ``joints``, different mathematical formulations can be used. These formulations require the use of a set of parameters, referred to as generalized coordinates, which uniquely defines the position and orientation of each system’s segment during the motion analysis. 

In the ``EZMotion`` tool, the fully cartesian coordinates (FCC) with a generic rigid body [2] are used to model and analyze the kinematics and dynamics of mechanical and biomechanical multibody systems. 

The details of the modeling procedure of each component of a multibody system is presented below. This information regarding the modeling of each model component must be included in a new line in the :doc:`modeling file </modeling>` of the multibody system.  

|
Segments
--------

Each segment of the model must be modeled as a rigid body. Thus, for each segment of the model it is necessary to include a rigid body kinematic constraint as presented in Figure 1.   

Rigid Body
**************

Ensure that the segment maintains constant length during the analysis.

.. figure:: .\\images\\generic_rigid_body.png
	:scale: 10 %
	:align: center
	:alt: Representation of a generic rigid body

	Fig 1. Representation of a generic rigid body

.. list-table:: Table 1. Rigid Body: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 1)
   * - Body
     - Number of the segment 
   * - Mass
     - Mass of the segment
   * - Moment of Inertia
     - Moment of inertia of the segment
   * - CoMLocCoordsX
     - Local coordinate of the *x* coordinate of the CoM with respect to the local reference frame of the segment 
   * - CoMLocCoordsY
     - Local coordinate of the *y* coordinate of the CoM with respect to the local reference frame of the segment 

.. list-table:: Table 2. Rigid Body: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - Body,
     - Mass,
     - Moment of Inertia,
     - CoMLocCoordsX,
     - CoMLocCoordsY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
   * - 1,
     - 1,
     - 1,
     - 0.0833,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0


|
Angular Drivers:
---------------

There are essentially two types of kinematic drivers: ``the angular driver``, used to prescribe the angle between two segments or a segment and a global axis, throughout the analysis period, and the ``trajectory driver``, used to prescribe the trajectory of a given point with respect to a given reference. 

The angular driver defined using the dot product fails to guide the angle for values in the vicinity of 0° and 180°, since the two vectors become aligned. To overcome this situation, it is necessary to use an angular driver defined usig the cross product between such vectors. In certain cases, the position or orientation of the rigid bodies need to be constrained with respect to the global reference frame (grounded). In such cases, it is possible to define specific kinematic constraint equations that relate a given rigid body with the Cartesian coordinates of fixed (grounded) points and unit vectors, defined in the global reference frame. 

Angular Driver: Dot Product
*************************

Allows driving the angle between two segments using the dot product (see Figure 2).

.. figure:: .\\images\\angular_driver.png
	:scale: 10 %
	:align: center
	:alt: Representation of the angular driver using the dot product between two segments.

	Fig 2. Representation of the angular driver using the dot product between two segments. 

.. list-table:: Table 3. Angular driver using the dot product: Fields Description
   :widths: 25 75  
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 2)
   * - ParentBd
     - Number of the moving body 1 
   * - ChildBd
     - Number of the moving body 2
   * - DoF
     - Number of the guided degree of freedom


.. list-table:: Table 4. Angular driver using the dot product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

 
   * - Type,
     - MovBd1,
     - MovBd2,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 1,
     - 1,
     - 2,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1
	 
Angular Driver Grounded: Dot Product
************************************

Allows driving the angle between one segment and one axis of the global reference frame using the dot product (see Figure 3).


.. figure:: .\\images\\angular_driver_grounded.png
	:scale: 10 %
	:align: center
	:alt: Representation of the angular driver grounded using the dot product between one segment and one axis of the global reference frame

	Fig 3. Representation of the angular driver grounded using the dot product.

.. list-table:: Table 5. Representation of the angular driver grounded using the dot product: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 3)
   * - MovBd
     - Number of the moving segment 
   * - GlCVtX
     - 'x' component of the global horizontal axis
   * - GlCVtY
     - 'y' component of the global horizontal axis
   * - DoF
     - Number of the guided degree of freedom

.. list-table:: Table 6. Representation of the angular driver grounded using the dot product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd1,
     - GlCVtX,
     - GlCVtY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 3,
     - 1,
     - 1,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1

Angular Driver: Cross Product
*****************************

Allows driving the angle between two segments using the cross product (see Figure 4).


.. figure:: .\\images\\angular_driver.png
	:scale: 10 %
	:align: center
	:alt: Representation of the angular driver using the cross product between two segments.

	Fig 4. Representation of the angular driver using the cross product between two segments. 

.. list-table:: Table 7. Angular driver using the cross product: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 4)
   * - ParentBd
     - Number of the moving segment 1 
   * - ChildBd
     - Number of the moving segment 1
   * - DoF
     - Number of the guided degree of freedom

.. list-table:: Table 8. Angular driver using the cross product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - ParentBd,
     - ChildBd,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 4,
     - 1,
     - 2,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1
	 

Angular Driver Grounded: Cross Product
**************************************

Allows driving the angle between one segment and one axis of the global reference frame using the cross product (see Figure 5).


.. figure:: .\\images\\angular_driver_grounded.png
	:scale: 10 %
	:align: center
	:alt: Representation of the angular driver grounded using the cross product between one segment and one axis of the global reference frame

	Fig 5. Representation of the angular driver grounded using the cross product.

.. list-table:: Table 9. Representation of the angular driver grounded using the cross product: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 5)
   * - MovBb
     - Number of the moving segment 
   * - GlCVtX
     - 'x' component fo the orientation ovector of the unitary vector of global axis
   * - GlCVtY
     - 'y' component fo the orientation ovector of the unitary vector of global axis
   * - DoF
     - Number of the guided degree of freedom

.. list-table:: Table 10. Representation of the angular driver grounded using the dot product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd1,
     - MovBd2,
     - GlCVtX,
     - GlCVtY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - 
   * - 5,
     - 1,
     - 1,
     - 1,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1

|
Trajectory Driver:
---------------

Allows to prescribe the trajectory of a given point with respect to a given reference (see Figure 6). 


.. figure:: .\\images\\trajectory_driver.png
	:scale: 10 %
	:align: center
	:alt: Representation of a revolute joint

	Fig 6. Representation of the trajectory driver. 

.. list-table:: Table 11. Trajectory driver: Fields Description
   :widths: 25 75 
   :header-rows: 1
    
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 6)
   * - MovBd
     - Number of the moving segment 
   * - DoFx
     - Number of the guided degree of freedom (*x* component)
   * - DoFy
     - Number of the guided degree of freedom (*y* component)
   * - LcCMvBx
     - Local coordinate of the *x* coordinate of the trajectory driver with respect to the global reference frame 
   * - LcCMvBy
     - Local coordinate of the *y* coordinate of the trajectory driver with respect to the global reference frame 
   * - GlCoordX*
     - Prescribed coordinate of the *x* coordinate of the trajectory driver with respect to the global reference frame
   * - GlCoordY*
     - prescribed coordinate of the *y* coordinate of the trajectory driver with respect to the global reference frame
   * - GlCoordVelX*
     - Prescribed velocity of the *x* coordinate of the trajectory driver with respect to the global reference frame
   * - GlCoordVelY*
     - Prescribed velocity of the *y* coordinate of the trajectory driver with respect to the global reference frame
   * - GlCoordAcclX*
     - Prescribed acceleration of the *x* coordinate of the trajectory driver with respect to the global reference frame
   * - GlCoordAcclY*
     - Prescribed acceleration of the *y* coordinate of the trajectory driver with respect to the global reference frame
   * - DoFType
     - Type of degree of freedom (linear or angular)

.. list-table:: Table 12. Trajectory driver: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1
 

   * - Type,
     - MovBd,
     - DoFx,
     - DoFy,
     - LcCMvBx,
     - LcCMvBy,
     - GlCoordX*,
     - GlCoordY*,
     - GlCoordVelX*,
     - GlCoordVelY*,
     - GlCoordAccX*,
     - GlCoordAccY*,
     - ,
     - DoFType
   * - 6,
     - 9,
     - 31,
     - 32,
     - 0,
     - -0.208,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1
 

|
Joints
--------

Joints allow for the relative emotion between adjacent bodies. Below is presented how to include a revolute, a double support or a single support joint in a multibody system.  

Single Support Joint
********************

It allows 1 rotation and 1 translation in one direction (see Figure 7).


.. figure:: .\\images\\single_support_joint.png
	:scale: 10 %
	:align: center
	:alt: Representation of a single support joint

	Fig 7. Representation of a single support joint. 

.. list-table:: Table 13. Single Support Joint: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 7)
   * - MovBd
     - Number of the moving segment 
   * - BlkDir
     - Blocked direction (0 - Horizontal, 1 - Vertical)
   * - LcCMvBx
     - Local coordinate of the *x* coordinate of the CoM of the segment with respect to the single support joint
   * - LcCMvBy
     - Local coordinate of the *y* coordinate of the CoM of the segment with respect to the single support joint
   * - GlCBlkDirX
     - *x* component of the axis of the global reference frame used to define the orientation of the moving direction
   * - GlCBlkDirY
     - *y* component of the axis of the global reference frame used to define the orientation of the moving direction

.. list-table:: Table 14. Single Support Joint: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd,
     - BlkDir,
     - LcCMvBx,
     - LcCMvBy,
     - GlCBlkDirX,
     - GlCBlkDirY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - 
   * - 7,
     - 2,
     - 1,
     - 0.5,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0


Double Support Joint
********************

It allows the rotational motion of one body with respect to a ``fixed`` point (See Figure 8).

.. figure:: .\\images\\double_support_joint.png
	:scale: 10 %
	:align: center
	:alt: Representation of a double support joint

	Fig 8. Representation of a double support joint. 

.. list-table:: Table 15. Double Support Joint: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 8)
   * - MovBd
     - Number of the moving segment 1 
   * - LcCMvBx
     - Local coordinate of the *x* coordinate of the double support joint with respect to the local reference frame of segment 1
   * - LcCMvBy
     - Local coordinate of the *y* coordinate of the double support  joint with respect to the local reference frame of segment 1
   * - GlCSpX
     - Global coordinate of the *x* coordinate of the double support joint
   * - GlCSpY
     - Global coordinate of the *y* coordinate of the double support joint


.. list-table:: Table 16. Double Support: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd,
     - LcCMvBx,
     - LcCMvBy,
     - LcCMvB1y,
     - GlCSpX,
     - GlCSpY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - 
   * - 8,
     - 1,
     - -1,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0

Revolute Joint
**************

It allows the rotational motion between two adjacent bodies (See Figure 9).


.. figure:: .\\images\\revolute_joint.png
	:scale: 10 %
	:align: center
	:alt: Representation of a revolute joint

	Fig 9. Representation of a revolute joint. 

.. list-table:: Table 17. Revolute Joint: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 9)
   * - MovBd1
     - Number of the moving segment 1 
   * - MovBd2
     - Number of the moving segment 2
   * - LcCMvB1x
     - Local coordinate of the *x* coordinate of the revolute joint with respect to the local reference frame of segment 1
   * - LcCMvB1y
     - Local coordinate of the *y* coordinate of the revolute joint with respect to the local reference frame of segment 1
   * - LcCMvB2x
     - Local coordinate of the *x* coordinate of the revolute joint with respect to the local reference frame of segment 2
   * - LcCMvB2y
     - Local coordinate of the *y* coordinate of the revolute joint with respect to the local reference frame of segment 2

.. list-table:: Table 18. Revolute Joint: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd1,
     - MovBd2,
     - LcCMvB1x,
     - LcCMvB1y,
     - LcCMvB2x,
     - LcCMvB2y,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - 
   * - 9,
     - 1,
     - 2,
     - 0.5,
     - 0,
     - -0.5,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0


Mixed Angular Drivers
---------------------

Mixed Angular Driver Grounded: Dot Product
******************************************

Allows computing the angle between one segment and the axis of the global reference frame using the dot product (see Figure 10).

.. figure:: .\\images\\mixed_angular_driver_grounded.png
	:scale: 10 %
	:align: center
	:alt: Representation of the mixed angular driver grounded using the dot product 

	Fig 10. Representation of mixed angular driver grounded using the dot product. 

.. list-table:: Table 19. Mixed angular driver grounded using the dot product: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 12)
   * - MovBd
     - Number of the moving
   * - Lu
     - Length of the unitary vector defining the orientation vector of moving body
   * - Lv
     - Length of the unitary vector defining the orientation vector of the global reference frame 
   * - GlCVtX
     - *x* component of the orientation vector of the global reference frame
   * - GlCVtY
     - *y* component of the orientation vector of the global reference frame
   * - DoF
     - Number of the degree of freedom

.. list-table:: Table 20. Mixed angular driver grounded using the dot product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd,
     - GlCVtX,
     - GlCVtY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 12,
     - 1,
     - 1,
     - 1,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1	 


Mixed Angular Driver: Dot Product
*********************************

Allows computing the angle between two segments using the dot product (see Figure 11).

.. figure:: .\\images\\mixed_angular_driver.png
	:scale: 10 %
	:align: center
	:alt: Representation of the mixed angular driver using the dot product between two segments

	Fig 11. Representation of the mixed angular driver using the dot product between two segments. 

.. list-table:: Table 21. Mixed angular driver using the dot product: Fields Description
   :widths: 25 75 
   :header-rows: 1
     
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 13)
   * - ParentBd
     - Number of the parent moving segment 1 
   * - ChildBd
     - Number of the child moving segment 1
   * - DoF
     - Number of the degree of freedom

.. list-table::  Table 22. Mixed angular driver using the dot product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - ParentBd,
     - ChildBd,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 13,
     - 1,
     - 2,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 2

Mixed angular Driver Grounded: Cross Product
********************************************

Allows computing the angle between one segment and the axis of the global reference frame using the cross product (see Figure 12).

.. figure:: .\\images\\mixed_angular_driver_grounded.png
	:scale: 10 %
	:align: center
	:alt: Representation of mixed angular driver grounded using the cross product

	Fig 12. Representation of the mixed angular driver grounded using the cross product. 

.. list-table:: Table 23. Mixed angular driver grounded using the cross product: Fields Description
   :widths: 25 75 
   :header-rows: 1
     
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 14)
   * - MovBd
     - Number of the moving
   * - GlCVtX
     - *x* component of the orientation vector of the global reference frame
   * - GlCVtY
     - *y* component of the orientation vector of the global reference frame
   * - DoF
     - Number of the degree of freedom

.. list-table:: Table 24. Mixed angular driver grounded using the cross product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - MovBd,
     - GlCVtX,
     - GlCVtY,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 14,
     - 1,
     - 1,
     - 1,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 1

Mixed Angular Driver: Cross Product
***********************************

Allows computing the angle between two segments using the cross product (see Figure 13).

.. figure:: .\\images\\mixed_angular_driver.png
	:scale: 10 %
	:align: center
	:alt: Representation of the mixed angular driver using the cross product between two segments

	Fig 13. Representation of the mixed angular driver using the cross product between two segments. 

.. list-table:: Table 25. Mixed angular driver using the cross product: Fields Description
   :widths: 25 75 
   :header-rows: 1
   
   * - Label
     - Description
   * - Type
     - Type of kinematic constraint ( == 15)
   * - ParentBd
     - Number of the parent moving segment 1 
   * - ChildBd
     - Number of the child moving segment 1
   * - DoF
     - Number of the degree of freedom

.. list-table::  Table 26. Mixed angular driver using the cross product: Modeling Example
   :widths: 7 7 7 7 7 7 7 7 7 7 7 7 7 7
   :header-rows: 1

   * - Type,
     - ParentBd,
     - ChildBd,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - ,
     - DoF
   * - 15,
     - 1,
     - 2,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 0,
     - 2

References
*************************

[1] Flores, P. *Concepts and Formulations for Spatial Multibody Dynamics*, Springer, New York Dordrecht London, 2015.

[2] I. Roupa, S.B. Gonçalves, M.T. da Silva, *Kinematics and dynamics of planar multibody systems with fully Cartesian coordinates and a generic rigid body*, Mech. Mach. Theory. 180 (2023) 105134. https://doi.org/https://doi.org/10.1016/j.mechmachtheory.2022.105134.
