import numpy as np
from csdl import Model
import csdl


class WeightsInputsModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
        self.parameters.declare('wing_area', types=np.ndarray)
        self.parameters.declare('wing_AR', types=np.ndarray)
        self.parameters.declare('fuselage_length', types=np.ndarray)
        self.parameters.declare('battery_weight', types=np.ndarray)
        self.parameters.declare('cruise_speed', types=np.ndarray)
        self.parameters.declare('tail_area', types=np.ndarray)
        self.parameters.declare('fin_area', types=np.ndarray)

    def define(self):
        shape = self.parameters['shape']
        wing_area = self.parameters['wing_area']
        wing_AR = self.parameters['wing_AR']
        fuselage_length = self.parameters['fuselage_length']
        battery_weight = self.parameters['battery_weight']
        cruise_speed = self.parameters['cruise_speed']
        tail_area = self.parameters['tail_area']
        fin_area = self.parameters['fin_area']
        

        self.create_input('wing_area', shape=shape, val=wing_area)
        self.create_input('wing_AR', shape=shape, val=wing_AR)
        self.create_input('fuselage_length', shape=shape, val=fuselage_length)
        self.create_input('battery_weight', shape=shape, val=battery_weight)
        self.create_input('cruise_speed', shape=shape, val=cruise_speed)
        self.create_input('tail_area', shape=shape, val=tail_area)
        self.create_input('fin_area',shape=shape, val=fin_area)

        self.add_design_variable('wing_area')
        self.add_design_variable('wing_AR')
        self.add_design_variable('fuselage_length')
        self.add_design_variable('battery_weight')
        self.add_design_variable('cruise_speed')
        self.add_design_variable('tail_area')
        self.add_design_variable('fin_area')

    


       
