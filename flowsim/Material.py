#note: characteristic curves are not changeable at the moment

import util.NumberToPflotran as ntp
import os

class Material():
    def __init__(self, id=1, name="gravel"):
        self.id = id
        self.name = name
        self.permeability = 1e-10 #default value
        self.porosity = 0.25 #default value
        self.tortuosity = 0.5 #default value
        self.rock_density = 2.8e3 #default value
        self.specific_heat = 1e3 #default value
        self.thermal_conductivity_dry = 0.5 #default value
        self.thermal_conductivity_wet = 0.5 #default value
        self.longitudinal_dispersivity = 3.1536 #default value
        if(os.path.isfile("permeability_data.h5")): #TODO adapt file name
            self.permeability_from_file = True
        else:
            self.permeability_from_file = False

    def to_pflotran(self):
        return f"""
        MATERIAL_PROPERTY {self.name}
            ID {self.id}
            POROSITY {ntp.ntop(self.porosity)}
            TORTUOSITY {ntp.ntop(self.tortuosity)}
            ROCK_DENSITY {ntp.ntop(self.rock_density)}
            SPECIFIC_HEAT {ntp.ntop(self.specific_heat)}
            THERMAL_CONDUCTIVITY_DRY {ntp.ntop(self.thermal_conductivity_dry)}
            THERMAL_CONDUCTIVITY_WET {ntp.ntop(self.thermal_conductivity_wet)}
            LONGITUDINAL_DISPERSIVITY {ntp.ntop(self.longitudinal_dispersivity)}
            PERMEABILITY
                {"PERM_ISO "+ntp.ntop(self.permeability) if not self.permeability_from_file else ""}
            /
            CHARACTERISTIC_CURVES {self.name}_cc
        /

        CHARACTERISTIC_CURVES {self.name}_cc
            SATURATION_FUNCTION VAN_GENUCHTEN
                ALPHA 1.d-4
                M 0.5d0
                LIQUID_RESIDUAL_SATURATION 0.1d0
            /
            PERMEABILITY_FUNCTION MUALEM_VG_LIQ
                M 0.5d0
                LIQUID_RESIDUAL_SATURATION 0.1d0
            /
        END
        """


class FluidProperties():

    def __init__(self, diffusion=1e-9):
        self.diffusion = diffusion

    def to_pflotran(self):
        return f"""
FLUID_PROPERTY
  DIFFUSION_COEFFICIENT {ntp.ntop(self.diffusion)}
/
"""

