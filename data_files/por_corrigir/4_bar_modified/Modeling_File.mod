# Unit Vector Constraint: Body 1
# Type,  Body, Lu, -, -, -, -, -, -, -, -, -, - , - 
     1,     1, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Unit Vector Constraint: Body 2
# Type,  Body, Lu, -, -, -, -, -, -, -, -, - , - , - 
     1,     2, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Unit Vector Constraint: Body 3
# Type,  Body, Lu, -, -, -, -, -, -, -, -, -, - , - 
     1,     3, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Double Support Constraint: Ground -> Body 1
# Type,  MovBd, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -, -, -, -, -
     8,      1,    -0.5,     0.0,      0,      0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Double Support Constraint : Ground -> Body 3
# Type,  MovBd, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -, -, -, -, -
     8,      3,      0.5,     0.0,     10,     0, 0, 0, 0, 0, 0, 0, 0, 0
# 
# Revolution Joint Constraint : Body 1 - > 2
# Type,  MovBd1, MovBd2, LcCMvB1x, LcCMvB1y, LcCMvB2x, LcCMvB2y, -, -, -, -, -, -, -
     9,       1, 	  2,      0.5,      0.0,       -5,        0, 0, 0, 0, 0, 0, 0, 0
#
# Translation Revolution Joint Constraint : Body 2 - > 3 
# Point 'p1' belong to parent body
# Point 'p2' and 'p3' belong to child body
# Type,  MovBd1, MovBd2, Lu, Lv, LcCoordP1x, LcCoordP1y, LcCoordP2x, LcCoordP2y, LcCoordP3x, LcCoordP3y, -, -, -
   10,        2, 	  3,  1,  1,        5.0,        0.0,        0.5,        0.0,       -5.0,          0, 0, 0 , 0 
#
# Angular Driver Constraint : Dot Product 
# Type,  ParentBd, ChildBd,  Lu,  Lv,   -,   -,   -,   -, -, -, -, -, DoF 
     2,         1,       2, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0,   1
#
# Grounded Angular Driver Constraint : Dot Product
# Type,  MovBd, Lu,  Lv,   GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
     3,      1, 1.0, 1.0,     1.0,     0,  0, 0, 0, 0, 0, 0, 0,   2
#
# Grounded Angular Driver Constraint : Dot Product
# Type,  MovBd, Lu,  Lv,   GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
     5,      1,  1,   1,       -1,    0.0, 0, 0, 0, 0, 0, 0, 0,   2