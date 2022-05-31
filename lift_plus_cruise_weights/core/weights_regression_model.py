import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from core.weights_inputs_model import WeightsInputsModel

class WeightsRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
        self.parameters.declare('wing_area')
        self.parameters.declare('wing_AR')
        self.parameters.declare('fuselage_length')
        self.parameters.declare('battery_weight')
        self.parameters.declare('cruise_speed')
        self.parameters.declare('tail_area')
        self.parameters.declare('fin_area')
    def define(self):
        shape = self.parameters['shape']
        wing_area = self.parameters['wing_area']
        wing_AR = self.parameters['wing_AR']
        fuselage_length = self.parameters['fuselage_length']
        battery_weight = self.parameters['battery_weight']
        cruise_speed = self.parameters['cruise_speed']
        tail_area = self.parameters['tail_area']
        fin_area = self.parameters['fin_area']

        self.add(WeightsInputsModel(
            shape=shape,
            wing_area=wing_area,
            wing_AR=wing_AR,
            fuselage_length=fuselage_length,
            battery_weight=battery_weight,
            cruise_speed=cruise_speed,
            tail_area=tail_area,
            fin_area=fin_area,
        ))

        wing_area = self.declare_variable('wing_area', shape=shape)#, val=210.28)
        wing_AR = self.declare_variable('wing_AR', shape=shape)#, val=12.1423)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)#, val=30)
        battery_weight = self.declare_variable('battery_weight', shape=shape)#, val=2675.27)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)#, val=112)
        tail_area = self.declare_variable('tail_area', shape=shape)#, val=39.51)
        fin_area = self.declare_variable('fin_area', shape=shape)#, val=27.34)

        gross_weight_minus_empennage = -49.118771850502334 * wing_area  -233.00816566857483 * wing_AR +  327.67564472201457 * fuselage_length +  2.2478553238442878 * battery_weight + 63.277198378545386  * cruise_speed + \
                       0.10364578242260847 * wing_area**2 + 0.7260390015132265 * wing_area * wing_AR + 0.30030382982080767 * wing_area * fuselage_length  -0.003683686051535743 * wing_area * battery_weight +  0.05797638247542994 * wing_area * cruise_speed + \
                       9.159983648870826 * wing_AR**2 + 6.457748691778041 * wing_AR * fuselage_length -0.007374590741813262 * wing_AR * battery_weight -1.3141664220591458 * wing_AR * cruise_speed + \
                       -10.929752756064005 * fuselage_length**2 + 0.05567259108973069 * fuselage_length * battery_weight + 0.539730523695426 * fuselage_length * cruise_speed + \
                        0.00010742156558762872 * battery_weight**2 -0.022510378907086626 * battery_weight * cruise_speed + \
                        -0.04763256483978545 * cruise_speed**2 + 71.77120785036095

         
        empennage_weight = 7.57715283e-02 * tail_area  - 5.07300739e-02 * fin_area  + 8.42532575e-05 * tail_area**2 + 6.72483630e-02 * tail_area * fin_area  - 2.05722127e-03 * fin_area**2 + 70.80119198401702
        
        gross_weight = gross_weight_minus_empennage + empennage_weight
        
        self.register_output('gross_weight',gross_weight)
        # self.add_objective('gross_weight')
