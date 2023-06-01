# Unit Vector Constraint: Body 1
# Type, Row, Body, -,  Lu, -, -, -, -, -, -, -, -, - 
     1,   0,    1, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# Unit Vector Constraint: Body 2
# Type, Row, Body, -,  Lu, -, -, -, -, -, -, -, -, -
     1,   1,    2, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# Double Support Constraint
# Type, Row, MovBd, -, -, -, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -
     8,   2,     1, 0, 0, 0,    -0.5,     0.0,    0.0,    0.0, 0, 0, 0, 0
# Revolute Joint Constraint
# Type, Row, MovBd1, MovBd2, -, -, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -
     9,   4,      1,      2, 0, 0,      0.5,      0.0,     -0.5,      0.0, 0, 0, 0, 0
# Single Support Constraint (BlkDir=[0:X,1:Y])
# Type, Row, MovBd, BlkDir, -, -, LcCMvBx, LcCMvBy, GlCBlkDirX, GlCBlkDirY, -, -, -, -
     7,   6,     2,      1, 0, 0,     0.5,     0.0,        0.0,        0.0, 0, 0, 0, 0
