import scipy.interpolate as interpolate

rbf_function = interpolate.Rbf([25, 65], [35, 75], [5,5] , function='thin_plate')
interpolated_permeability = rbf_function([25, 65], [35, 75])

print('interpolated permeability: \n', interpolated_permeability)