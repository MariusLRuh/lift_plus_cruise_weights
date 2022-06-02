import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from lift_plus_cruise_weights.core.core_weights_model import CoreWeightsModel

# TO DO: get areas/AR/fuselage legnth + from points sets 

num_evaluations = 1
shape = (num_evaluations,)

weights_model = CoreWeightsModel(
    shape=shape,
)

sim = Simulator(weights_model)
sim.run()

# sim.prob.check_partials(compact_print=True)
# sim.prob.check_totals(compact_print=True)

print(sim['gross_weight'])
print(sim['empennage_weight'])
print(sim['fuselage_weight'])