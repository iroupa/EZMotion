# Model  		: Full body + Pelvis
# Coordinates	: Mixed Coordinates
# RoM			: Static
#
###################################################################################
#
# Unit Vector Constraint: Body 1 : Thorax
# Type, Body, Lu,   Mass, Moment_Inertia, CoMLocCoordsX, CoMLocCoordsY, -, -, -, -, - , -, - 
     1,    1,  1, 31.212,    0.146239202,             0,             0, 0, 0, 0, 0, 0 , 0, 0 
#
# Mixed Grounded Angular Driver Constraint : Dot Product
# Type, MovBd, Lu,  Lv,   GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
    12,     1, 1.0, 1.0,     1.0,      0, 0, 0, 0, 0, 0, 0, 0, 1
#
# Mixed Grounded Angular Driver Constraint : Cross Product
# Type, MovBd,  Lu,  Lv, GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
    14,     1, 1.0, 1.0,    1.0,      0, 0, 0, 0, 0, 0, 0, 0, 1
#
##################################################################################
#
# Unit Vector Constraint: Body 2 : Head
# Type, Body, Lu, -, -, -, -, -, -, -, -, - , -, - 
      1,   2, 1.0,4.374,0.019847025,0,0,0,0,0,0,0 ,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,  -, -, -, -, -, -, -
     9,      1,      2,        0, 	0.192,         0,   -0.143,  0, 0, 0, 0, 0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,   0,        1,       2, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 2
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,   0,        1,       2, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0, 2	
#
###################################################################################
#
# Unit Vector Constraint: Body 3 : R_Upper_Arm
# Type, Body,  Lu,    -,          -, -, -, -, -, -, -, -, -, - 
     1,    3, 1.0,1.512,0.002903152, 0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -, -, -, -
     9,     1,      3,         0, 0.192,       0.0,    0.138,        0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  11,       1,       3, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0,    3
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  12,       1,       3, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,    3	
#
###################################################################################
# 
# Unit Vector Constraint: Body 4 : L_Upper_Arm
# Type, Body,  Lu,     -,           -, -, -, -, -, -, -, -, -, - 
     1,    4, 1.0, 1.512, 0.002903152, 0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -, -, -, -
     9,      1,      4,        0,    0.192,      0.0,    0.127,   0, 0, 0, 0, 0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  16,        1,       4, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 4
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  17,        1,       4, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  4	
#
###################################################################################
#
# Unit Vector Constraint: Body 5 : R_ForeArm
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,    5, 1.0,0.864,0.001468944,0,0,0,0,0,0,0 ,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,  -, -, -, -, -, -, -
     9,      3,      5,       0,    -0.171,      0.0,    0.078,  0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  21,       3,       5, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 5
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  22,       3,       5, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  5
#
###################################################################################
#
# Unit Vector Constraint: Body 6 : L_ForeArm
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
      1,    6, 1.0,0.864,0.001468944,0,0,0,0,0,0,0 ,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,    -, -, -, -, -, -, -
     9,      4,      6, 	  0,       -0.165,      0.0,    0.076,    0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
   13,  26,        4,       6, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 6
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  27,        4,       6, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  6	
#
###################################################################################
#
# Unit Vector Constraint: Body 7 : R_Thigh
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,   7, 1.0,5.40,0.0104329,0,0,0,0,0,0,0,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      7,   	  0,   -0.326,      0.0,    0.162,        0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  31,       1,       7, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 7
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
   15,  32,        1,       7, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  7	
#
###################################################################################
#
# Unit Vector Constraint: Body 8 : L_Thigh
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,    8, 1.0,5.40,0.0104329,0,0,0,0,0,0,0,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      8,       0,    -0.326,      0.0,    0.167, 0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  36,        1,       8, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 8
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  37,        1,       8, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  8	
#
###################################################################################
#
# Unit Vector Constraint: Body 9 : R_Shank
# Type, Body, Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,    9, 1.0,2.5110,0.0048512985,0,0,0,0,0,0,0 ,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      7,      9,        0,   -0.212,      0.0,    0.159, 0, 0, 0, 0, 0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
   13,  41,        7,       9, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 9
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  42,       7,       9, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,   9	
#
###################################################################################
#
# Unit Vector Constraint: Body 10 : L_Shank
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,    10, 1.0,2.5110,0.0048512985,0,0,0,0,0,0,0,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      8,     10,  0, -0.218,      0.0,    0.153,        0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  46,        8,       10, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 10
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  47,        8,       10, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  10	
#
###################################################################################
#
# Unit Vector Constraint: Body 11 : R_Foot
# Type, Body,  Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,   11, 1.0,0.783,0.0032715625,0,0,0,0,0,0,0 ,0,0  
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,     9,     11,       0, -0.208,      0.0,    0.058,   0,  0, 0, 0,  0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  51,        9,       11, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 11
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  52,        9,       11, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  11	
#
###################################################################################
#
# Unit Vector Constraint: Body 12 : L_Foot
# Type, Body, Lu, -, -, -, -, -, -, -, -, - , -, - 
     1,   12, 1.0,0.783,0.0032715625,0,0,0,0,0,0,0,0,0 
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,     10,     12,        0,   -0.200,      0.0,    0.062, 0, 0, 0, 0, 0, 0, 0
#
# Mixed Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,   Lu,  Lv, -, -,  -, -, Theta*, Thetadot*, Thetaddot*, DoF
    13,  56,      10,       12, 1.0, 1.0, 0, 0,  0, 0,      0,         0,          0, 12
#
# Mixed Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv, -, -, -, -, Theta*, Thetadot*, Thetaddot*, DoF
    15,  57,        10,       12, 1.0, 1.0, 0, 0, 0, 0,      0,         0,          0,  12	
#
# Trajectory Driver Constraint : MidShoulder marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     1,   13,    14,        0,   0.192,        0,          0,        	0,            0,            0,            0,  0,       1
#
# Trajectory Driver Constraint : MidHip marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     1,   15,    16,        0,  -0.326,         0,         0,    	    0,            0,            0,            0, 0,       1
# 
# Trajectory Driver Constraint : TopHead marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     2,   17,    18,  	   0,   0.143,         0,         0,    	    0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : R Elbow marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     3,   19,    20,        0,  -0.171,         0,         0,    	    0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : l Elbow marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     4,   21,    22,   	   0,  -0.165,         0,         0,            0,    	      0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : r wrist marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     5,   23,    24,        0,  -0.171,         0,         0,    	    0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : l wrist marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     6,   25,    26,        0,  -0.165,         0,    	  0,            0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : R knee marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     7,   27,    28,        0,  -0.212,         0,    	  0,            0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : L knee marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,     8,   29,    30,        0,  -0.218,         0,         0,    	    0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : R Ankle marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,    9,    31,    32,        0,  -0.208,         0,    	  0,            0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : L Ankle marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,    10,   33,    34,        0,  -0.200,         0,    	  0,            0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : R Meta marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,    11,   35,    36,        0,  -0.058,         0,         0,    	    0,            0,            0,            0, 0,       1
#
# Trajectory Driver Constraint : L Meta marker
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -, DoFType 
     6,    12,   37,    38,        0,  -0.062,         0,    	  0,            0,            0,            0,            0, 0,       1