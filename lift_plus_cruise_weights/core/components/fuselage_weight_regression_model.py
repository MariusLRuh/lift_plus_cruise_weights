import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class FuselageWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)

        fuselage_weight = 38.55199147 * fuselage_length - 344.4498597087978

        self.register_output('fuselage_weight',fuselage_weight)

