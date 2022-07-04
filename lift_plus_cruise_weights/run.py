import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from lift_plus_cruise_weights.core.lift_plus_cruise_weights_model import LiftPlusCruiseWeightsModel

# TO DO: get areas/AR/fuselage legnth + from points sets 

num_nodes = 1


weights_model = LiftPlusCruiseWeightsModel(
    num_nodes=num_nodes,
)

sim = Simulator(weights_model)

sim.run()


print('\n')
print('Mass properties:')
print('mass: ',sim['mass'])
print('cgx: ', sim['cgx'])
print('cgy: ', sim['cgy'])
print('cgz: ', sim['cgz'])
print('ixx: ', sim['ixx'])
print('iyy: ', sim['iyy'])
print('izz: ', sim['izz'])
print('ixy: ', sim['ixy'])
print('ixz: ', sim['ixz'])
print('iyz: ', sim['iyz'])



# sim.prob.check_partials(compact_print=True)
# sim.prob.check_totals(compact_print=True)
