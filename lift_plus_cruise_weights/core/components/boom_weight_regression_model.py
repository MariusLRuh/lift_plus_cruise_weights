import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class BoomWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_weight = self.declare_variable('battery_weight', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
      

        boom_weight =  6.64226897e-01 * wing_area + 1.18429889e+01 * wing_AR -3.00395573e-01 * fuselage_length -1.22160336e-03 * battery_weight -1.18242922e-02 * cruise_speed - 15.090980695937446
        self.register_output('boom_weight',boom_weight)

