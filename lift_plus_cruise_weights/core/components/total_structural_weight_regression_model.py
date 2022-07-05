import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class TotalStructuralWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_mass = self.declare_variable('battery_mass', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
    
        total_structural_weight =   3.44445789e+00 * wing_area + 6.98584506e+01 * wing_AR + 3.98349615e+01 * fuselage_length + 6.80710943e-02 * battery_mass + 1.42482522e+00 * cruise_speed  -1384.6035424747126
        self.register_output('total_structural_weight',total_structural_weight)

