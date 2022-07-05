import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator


class NonStructuralWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']

        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_mass = self.declare_variable('battery_mass', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
    
        non_structural_weight =   5.49683441 * wing_area + 91.34214517 * wing_AR +  1.9698989 * fuselage_length + 1.00166832 * battery_mass + 3.72346506 * cruise_speed + 2032.858763286621
        self.register_output('non_structural_weight',non_structural_weight)

