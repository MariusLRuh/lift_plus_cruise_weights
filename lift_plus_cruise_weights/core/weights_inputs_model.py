import numpy as np
from csdl import Model
import csdl


class WeightsInputsModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)

    def define(self):
        shape = self.parameters['shape']
    
        self.create_input('wing_area', shape=shape, val=210.28)
        self.create_input('wing_AR', shape=shape, val=12.1423)
        self.create_input('fuselage_length', shape=shape, val=30)
        self.create_input('battery_weight', shape=shape, val=2675.27)
        self.create_input('cruise_speed', shape=shape, val=112)
        self.create_input('tail_area', shape=shape, val=39.51)
        self.create_input('fin_area',shape=shape, val=27.34)

        self.add_design_variable('wing_area')
        self.add_design_variable('wing_AR')
        self.add_design_variable('fuselage_length')
        self.add_design_variable('battery_weight')
        self.add_design_variable('cruise_speed')
        self.add_design_variable('tail_area')
        self.add_design_variable('fin_area')

    


       
