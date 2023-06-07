# Model : Trunk
# Coordinates : Fully Cartesian
# Constraints : Dot Product + Cross Product
# 
########################################################################## 
#
# Unit Vector Constraint: Thorax
# Type,Row,Body,-,  Lu,  Mass,Moment_Inertia,-,-,-,-,-,-,-
     1,  0,   1,0, 1.0,31.212,0.146239202,0,0,0,0,0,0,0 
#
# Grounded Angular Driver Constraint : Dot Product
# Type,Row,MovBd, -,  Lu,  Lv,   -,   -,  GlCVtX, GlCVtY, -, -,  -, DoF
     3,  0,   1, 0, 1.0, 1.0, 0.0, 0.0,      1.0,    0.0, 0,  0, 0,   1
#
# Grounded Angular Driver Constraint : Cross Product
# Type, Row, MovBd, -,  Lu,  Lv,   -,   -, GlCVtX, GlCVtY, -, -, -, DoF
     5,   0,     1, 0, 1.0, 1.0, 0.0, 0.0,    1.0,    0.0, 0, 0, 0,   1
#
########################################################################## 
#
# Trajectory Driver Constraint: Marker midhip
# Type,Row,MovBd,DoFx,DoFy,LcCMvBx,LcCMvBy,GlCoordX,GlCoordY,GlCoordVelX,GlCoordVelY,GlCoordAccX,GlCoordAccY,DoFType
     6,  0,    1,   2,   3,      0,  -0.174,       0,       0,          0,          0,          0,          0,      1
#
########################################################################## 
#
# Unit Vector Constraint: Head
# Type,Row,Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,   2,0, 1.0,4.374,0.019847025,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type,Row,ParentBd,ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,       1,      2,1.0, 1.0,0,0,0,0,0,0,0,4
#
# Angular Driver Constraint : Cross Product
# Type,Row,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,       1,      2, 1.0, 1.0,0,0,0,0,0,0,0,4
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,   0,      2,      1, 0, 0,      0.0,   -0.143,        0,    0.337,  0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint: R_Upper_Arm
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,   0,    3,0, 1.0,1.512,0.002903152,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,   0,       3,       1,1.0, 1.0,0,0,0,0,0,0,0,5
#
# Angular Driver Constraint : Cross Product
# Type,Row,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        3,      1, 1.0, 1.0,0,0,0,0,0,0,0,5
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      1,      3, 0, 0,        0,    0.337,      0.0,    0.132,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint: L_Upper_Arm
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    4,0, 1.0,1.512,0.002903152,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        4,      1,1.0, 1.0,0,0,0,0,0,0,0,6
#
# Angular Driver Constraint : Cross Product
# Type,Row,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        4,      1, 1.0, 1.0,0,0,0,0,0,0,0,6
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      1,      4, 0, 0,    0, 0.337,      0.0,        0.127,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint: R_Forearm
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    5,0, 1.0,0.864,0.001468944,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        5,       3,1.0, 1.0,0,0,0,0,0,0,0,7
#
# Angular Driver Constraint : Cross Product
# Type,Row,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,       5,      3, 1.0, 1.0,0,0,0,0,0,0,0,7
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -
     9,  0,      3,      5, 0, 0,        0,   -0.172,      0.0,    0.078, 0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : L_Forearm
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    6,0, 1.0,0.864,0.001468944,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        6,       4,1.0, 1.0,0,0,0,0,0,0,0,8
#
# Angular Driver Constraint : Cross Product
# Type,Row,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,      6,      4, 1.0, 1.0,0,0,0,0,0,0,0,8
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      4,      6, 0, 0,        0,   -0.165,      0.0,    0.077,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : R_Thigh
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,   7,0, 1.0,5.40,0.0104329,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        7,       1,1.0, 1.0,0,0,0,0,0,0,0,9
#
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        7,       1, 1.0, 1.0,0,0,0,0,0,0,0,9
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      1,      7, 0, 0,        0,   -0.174,      0.0,    0.162,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : L_Thigh
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    8,0, 1.0,5.40,0.0104329,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        8,       1, 1.0, 1.0,0,0,0,0,0,0,0,10
#
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        8, 	     1, 1.0, 1.0,0,0,0,0,0,0,0,10
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      1,      8, 0, 0,        0,   -0.174,    0.0,      0.167,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : R_Leg
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    9,0, 1.0,2.5110,0.0048512985,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        9,       7,1.0, 1.0,0,0,0,0,0,0,0,11
#
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        9,       7, 1.0, 1.0,0,0,0,0,0,0,0,11
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -
     9,  0,      7,      9, 0, 0,    	  0,  -0.212,      0.0,     0.159, 0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : L_Leg
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    10,0, 1.0,2.5110,0.0048512985,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,        10,       8,1.0, 1.0,0,0,0,0,0,0,0,12
#
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,        10,       8, 1.0, 1.0,0,0,0,0,0,0,0,12
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -
     9,  0,      8,     10, 0, 0,        0, -0.218,      0.0,      0.153, 0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : R_Foot
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    11,0, 1.0,0.783,0.0032715625,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,      11,       9,1.0, 1.0,0,0,0,0,0,0,0,13
#
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,      11,       9, 1.0, 1.0,0,0,0,0,0,0,0,13
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -,    LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,      9,      11, 0, 0,          0, -0.209,      0.0,    0.058,      0.0, 0, 0, 0
#
########################################################################## 
#
# Unit Vector Constraint : L_Foot
# Type, Row, Body,-,  Lu,-,-,-,-,-,-,-,-,-
     1,  0,    12,0, 1.0,0.783,0.0032715625,0,0,0,0,0,0,0 
#
# Angular Driver Constraint : Dot Product
# Type, Row, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,DoF
     2,  0,       12,       10,1.0, 1.0,0,0,0,0,0,0,0,14
#	 
# Angular Driver Constraint : Cross Product
# Type, Row, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,DoF
     4,  0,       12,       10, 1.0, 1.0,0,0,0,0,0,0,0,14
#
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,  0,     10,     12, 0, 0,        0,   -0.200,      0.0,      0.062,      0.0, 0, 0, 0