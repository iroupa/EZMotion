# Model: Moving Body
# Unit Vector Constraint: Body 1
# Type, Body,  Lu, -, -, -, -, -, -, -, -, -, -, - 
     1, 1, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# Grounded Angular Driver Constraint : Dot Product
# Type, MovBd,  Lu,  Lv, GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
     3,     1, 1.0, 1.0,    1.0,      0, 0, 0, 0, 0, 0, 0, 0, 1
# Grounded Angular Driver Constraint : Cross Product
# Type, MovBd, Lu,  Lv, GlCVtX, GlCVtY, -, -, -, -, -, -, -, DoF 
     5,     1,  1,   1,      1,      0, 0, 0, 0, 0, 0, 0, 0, 1
# Trajectory Driver Constraint : 
# Type, MovBd, DoFx,  DoFy,  LcCMvBx, LcCMvBy, GlCoordX*, GlCoordY*, GlCoordVelX*, GlCoordVelY*, GlCoordAccX*, GlCoordAccY*, -,  DoFType 
     6,     1,    2,    3,         0,      0,         0,    	   0,            0,            0,            0,           0, 0,      1