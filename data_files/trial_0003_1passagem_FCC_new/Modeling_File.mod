# Model : Trunk
# Coordinates : Fully Cartesian
# Constraints : Dot Product + Cross Product
# 
########################################################################## 
#
# Unit Vector Constraint: Thorax
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY,-, -, -, -, -, -, -, -
     1,    1,  31.212,    0.146239202,            0,            0,0, 0, 0, 0, 0, 0, 0, 0  
#
# Unit Vector Constraint: Head
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    2, 4.374,    0.019847025,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint: R_Upper_Arm
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    3, 1.512,    0.002903152,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint: L_Upper_Arm
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    4, 1.512,    0.002903152,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint: R_Forearm
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    5, 0.864,    0.001468944,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : L_Forearm
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    6, 0.864,    0.001468944,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : R_Thigh
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    7,   5.4,      0.0104329,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : L_Thigh
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    8,   5.4,      0.0104329,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : R_Leg
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,    9, 2.511,   0.0048512985,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : L_Leg
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,   10, 2.511,   0.0048512985,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
# Unit Vector Constraint : R_Foot
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,   11, 0.783,   0.0032715625,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Unit Vector Constraint : L_Foot
# Type, Body,  Mass, Moment_Inertia, CoMLocCoordX, CoMLocCoordY, -, -, -, -, -, -, -, -
     1,   12, 0.783,   0.0032715625,            0,            0, 0, 0, 0, 0, 0, 0, 0, 0 
#
#########################################################################
# 
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      2,      1, 0.0,   -0.143,        0,    0.337,  0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      3,        0,    0.337,      0.0,    0.132, 0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      4,        0, 0.337,      0.0,       0.127, 0, 0, 0, 0, 0, 0, 0
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y,   -, -, -, -, -, -, -
     9,      3,      5,        0,   -0.172,      0.0,    0.078, 0.0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      4,      6,        0,   -0.165,      0.0,    0.077, 0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      7,        0,   -0.174,      0.0,    0.162,  0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      8,        0,   -0.174,    0.0,      0.167, 0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      7,      9,    	   0,  -0.212,      0.0,     0.159, 0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      8,     10,        0, -0.218,      0.0,      0.153, 0, 0, 0, 0, 0, 0, 0
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      9,     11,        0, -0.209,      0.0,    0.058,   0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,     10,     12,        0,   -0.200,      0.0,    0.062, 0, 0, 0, 0, 0, 0, 0
#
#########################################################################
#
# Grounded Angular Driver Constraint : Dot Product
# Type, MovBd, GlCVtX,  GlCVtY, -, -, -, -, -, -, -, -, -, DoF
     3,     1,  1,   0,      0, 0, 0, 0, 0, 0, 0, 0, 0,   1
#
# Grounded Angular Driver Constraint : Cross Product
# Type, MovBd, GlCVtX,  GlCVtY, -, -, -, -, -, -, -, -, -, DoF
     5,     1,  1,   0,      0, 0, 0, 0, 0, 0, 0, 0, 0, 1
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv, -, -, -, -, -, -, -, -, DoF
     2,        1,       2,  1,   1, 0, 0, 0, 0, 0, 0, 0, 0, 4
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd,ChildBd,  Lu,  Lv, -, -, -, -, -, -, -, -, DoF
     4,        1,      2,   1,   1, 0, 0, 0, 0, 0, 0, 0, 0, 4
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        3,       1,1.0, 1.0,0,0,0,0,0,0,0,0,5
#
# Angular Driver Constraint : Cross Product
# Type,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,        3,      1, 1.0, 1.0,0,0,0,0,0,0,0,0,5
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        4,      1,1.0, 1.0,0,0,0,0,0,0,0,0,6
#
# Angular Driver Constraint : Cross Product
# Type,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,        4,      1, 1.0, 1.0,0,0,0,0,0,0,0,0,6
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        5,       3,1.0, 1.0,0,0,0,0,0,0,0,0,7
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,        5,      3, 1.0, 1.0,0,0,0,0,0,0,0,0,7
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        6,       4,1.0, 1.0,0,0,0,0,0,0,0,0,8
#
# Angular Driver Constraint : Cross Product
# Type,ParentBd,ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,      6,      4, 1.0, 1.0,0,0,0,0,0,0,0,0,8
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        7,       1,1.0, 1.0,0,0,0,0,0,0,0,0,9
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,       7,       1, 1.0, 1.0,0,0,0,0,0,0,0,0,9
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        8,       1, 1.0, 1.0,0,0,0,0,0,0,0,0,10
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,        8, 	     1, 1.0, 1,0,0,0,0,0,0,0,0,10
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        9,       7,1.0, 1.0,0,0,0,0,0,0,0,0,11
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,        9,       7, 1.0, 1.0,0,0,0,0,0,0,0,0,11
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,        10,       8,1.0, 1.0,0,0,0,0,0,0,0,0,12
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,       10,       8, 1.0, 1.0,0,0,0,0,0,0,0,0,12
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,      11,       9,1.0, 1.0,0,0,0,0,0,0,0,0,13
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,      11,       9, 1.0, 1.0,0,0,0,0,0,0,0,0,13
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd, Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     2,       12,       10,1.0, 1.0,0,0,0,0,0,0,0,0,14
#	 
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  Lu,  Lv,-,-,-,-,-,-,-,-,DoF
     4,       12,       10, 1.0, 1.0,0,0,0,0,0,0,0,0,14
#
########################################################################## 
#
# Trajectory Driver Constraint: Marker midhip
# Type,MovBd,DoFx,DoFy,LcCMvBx,LcCMvBy,GlCoordX,GlCoordY,GlCoordVelX,GlCoordVelY,GlCoordAccX,GlCoordAccY, -, DoFType
     6,    1,   2,   3,      0,  -0.174,       0,       0,         0,         0,          0,          0,  0,       1