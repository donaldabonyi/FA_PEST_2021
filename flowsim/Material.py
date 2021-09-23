#note: characteristic curves are not changeable at the moment

class Material:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.permeability = 1e-9 #default value
        self.porosity = 0.25 #default value
        self.tortuosity = 0.5 #default value
        self.rock_density = 2.8e3 #default value
        self.specific_heat = 1e3 #default value
        self.thermal_conductivity_dry = 0.5 #default value
        self.thermal_conductivity_wet = 0.5 #default value
        self.longitudinal_dispersivity = 5 #default value

    def to_pflotran(self):
        return f"""
        MATERIAL_PROPERTY {self.name}
            ID {self.id}
            POROSITY {self.porosity}
            TORTUOSITY {self.tortuosity}
            ROCK_DENSITY {self.rock_density}
            SPECIFIC_HEAT {self.specific_heat}
            THERMAL_CONDUCTIVITY_DRY {self.thermal_conductivity_dry}
            THERMAL_CONDUCTIVITY_WET {self.thermal_conductivity_wet}
            LONGITUDINAL_DISPERSIVITY {self.longitudinal_dispersivity}
            PERMEABILITY
                PERM_ISO {self.permeability}
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