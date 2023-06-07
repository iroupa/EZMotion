# Unit Vector Constraint: Body 1
# Type, Body, -, -, -, -, -, -, -, -, -, -, -, - 
     1,    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Unit Vector Constraint: Body 2
# Type, Body, -, -, -, -, -, -, -, -, -, -, -, - 
     1,    2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Double Support Constraint
# Type, MovBd, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -, -, -, -, -
     8,     1,    -0.5,     0.0,      0,      0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Revolute Joint Constraint
# Type, MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,      1,      2,      0.5,      0.0,     -0.5,      0.0, 0, 0, 0, 0, 0, 0, 0
#	  
# Grounded Angular Driver Constraint : Dot Product
# Type, MovBd, GlCVtX, GlCVtY, -, -, -, -, -, -, -, -, -, DoF 
     3,     1,      1,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1
#
# Grounded Angular Driver Constraint : Cross Product
# Type, MovBd, GlCVtX, GlCVtY, -, -, -, -, -, -, -, -, -, DoF 
     5,     1,      1,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1
#
# Angular Driver Constraint : Dot Product
# Type, ParentBd, ChildBd,  -, -, -, -, -, -, -, -, -, -, DoF 
     2,        1,       2,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2
#
# Angular Driver Constraint : Cross Product
# Type, ParentBd, ChildBd,  -, -, -, -, -, -, -, -, -, -, DoF 
     4,        1,       2,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2