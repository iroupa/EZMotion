# Unit Vector Constraint: Body 1
# Type, Body, Mass, Moment_Inertia, CoMLocCoordsX, CoMLocCoordsY, -, -, -, -, -, -, - , - 
     1,    1,    1,         0.0833, 			0, 			   0, 0, 0, 0, 0, 0, 0, 0, 0
# Unit Vector Constraint: Body 2
# Type, Body, Mass, Moment_Inertia, CoMLocCoordsX, CoMLocCoordsY, -, -, -, -, -, -, -, -
     1,    2,    1,         0.0833, 			0, 			   0, 0, 0, 0, 0, 0, 0, 0, 0
# Double Support Constraint
# Type, MovBd, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -, -, -, -, -
     8,     1,    -0.5,     0.0,    0.0,    0.0, 0, 0, 0, 0, 0, 0, 0, 0
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      2,      0.5,      0.0,     -0.5,      0.0, 0, 0, 0, 0, 0, 0, 0
# Single Support Constraint (BlkDir=[0:X,1:Y])
# Type, MovBd, BlkDir, LcCMvBx, LcCMvBy, GlCBlkDirX, GlCBlkDirY, -, -, -, -, -, -, -
     7,     2,      1,     0.5,     0.0,        0.0,        0.0, 0, 0, 0, 0, 0, 0, 0
