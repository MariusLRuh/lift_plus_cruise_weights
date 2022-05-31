import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from core.weights_regression_model import WeightsRegressionModel

num_evaluations = 1


# TO DO: get areas/AR/fuselage legnth + from points sets 

shape = (num_evaluations,)
weights_model = WeightsRegressionModel(
    shape=shape,
    wing_area=np.array([210.28]),        # ft^2
    wing_AR=np.array([12.1423]),         #
    fuselage_length=np.array([30]),      # ft
    battery_weight=np.array([2675.27]),  # lbs
    cruise_speed=np.array([112]),        # ktas
    tail_area=np.array([39.51]),         # ft^2
    fin_area=np.array([27.34]),          # ft^2
)

sim = Simulator(weights_model)
sim.run()

# sim.prob.check_partials(compact_print=True)
# sim.prob.check_totals(compact_print=True)

print(sim['gross_weight'])