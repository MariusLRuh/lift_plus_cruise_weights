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

print('empennage_weight: ',sim['empennage_weight'])
print('fuselage_weight: ',sim['fuselage_weight'])
print('wing_weight: ',sim['wing_weight'])
print('boom_weight: ',sim['boom_weight'])
print('-----------------------------')
print('total_structural_weight: ', sim['total_structural_weight'])

print('total_non_structural_weight: ', sim['non_structural_weight'])
print('-----------------------------')
print('gross_weight: ', sim['gross_weight'])
