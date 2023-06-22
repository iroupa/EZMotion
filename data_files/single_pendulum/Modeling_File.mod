# Unit Vector Constraint: Body 1
# Type, Body, Mass, Moment_Inertia, CoMLocCoordsX, CoMLocCoordsY, -, -, -, -, -, -, -, - 
     1,    1,    1,         0.0833, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Double Support Constraint
# Type, MovBd, LcCMvBx, LcCMvBy, GlCSpX, GlCSpY, -, -, -, -, -, -, -, -
     8,     1,    -0.5,     0.0,      0,      0, 0, 0, 0, 0, 0, 0, 0, 0
#
# Grounded Angular Driver Constraint : Dot Product
# Type, MovBd, GlCVtX, GlCVtY, -, -, -, -, -, -, -, -, -, DoF 
     3,     1,      1,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1
#
# Grounded Angular Driver Constraint : Cross Product
# Type, MovBd, GlCVtX, GlCVtY, -, -, -, -, -, -, -, -, -, DoF 
     5,     1,      1,      0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1