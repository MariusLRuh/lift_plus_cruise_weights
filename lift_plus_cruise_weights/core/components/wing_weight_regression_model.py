import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class WingWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_weight = self.declare_variable('battery_weight', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
    
        wing_weight =   3.16517210e+00 * wing_area + 4.98717495e+01 * wing_AR + 2.56574260e+00 * fuselage_length + 2.31695801e-02 * battery_weight -1.37015474e-01 * cruise_speed  -878.4384764733035
        self.register_output('wing_weight',wing_weight)

