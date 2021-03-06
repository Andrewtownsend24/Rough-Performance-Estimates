# Use this file to create the plane objects to find their performances and compare them to each other
# Place the XFLR5 polars into the "AirFoils" folder
# All units being used in this program are the SI units (m, s, m/s, kg, N, watts, joules)
# Down below is an example of an aircraft

import PistonEngine
import TurboJet
import ElectricMotor
import Plane

a = PistonEngine.PistonEngine("NACA_2412_Re5.256.txt", "Cessna 172", 11, 1.378, 0, 1.11, 2, 62, 84, 767, 173, 171,
                              0.0175, 0.7, 0.000000777, .9, 120000, 6)

b = PistonEngine.PistonEngine("NACA_2412_Re5.256.txt", "Cessna 172-1", 11, 1.378, 0, 1.11, 2, 62, 84, 747, 173, 190,
                              0.0175, 0.7, 0.000000777, .9, 120000, 6)

lst = Plane.PlaneList()
lst.add_plane(a)
lst.add_plane(b)

c = lst.greatest_range()

print(c.get_name())

