import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from core.weights_inputs_model import WeightsInputsModel

class GrossWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_mass = self.declare_variable('battery_mass', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
        tail_area = self.declare_variable('tail_area', shape=shape)
        fin_area = self.declare_variable('fin_area', shape=shape)
    
        gross_weight_minus_empennage = -49.118771850502334 * wing_area  -233.00816566857483 * wing_AR +  327.67564472201457 * fuselage_length +  2.2478553238442878 * battery_mass + 63.277198378545386  * cruise_speed + \
                       0.10364578242260847 * wing_area**2 + 0.7260390015132265 * wing_area * wing_AR + 0.30030382982080767 * wing_area * fuselage_length  -0.003683686051535743 * wing_area * battery_mass +  0.05797638247542994 * wing_area * cruise_speed + \
                       9.159983648870826 * wing_AR**2 + 6.457748691778041 * wing_AR * fuselage_length -0.007374590741813262 * wing_AR * battery_mass -1.3141664220591458 * wing_AR * cruise_speed + \
                       -10.929752756064005 * fuselage_length**2 + 0.05567259108973069 * fuselage_length * battery_mass + 0.539730523695426 * fuselage_length * cruise_speed + \
                        0.00010742156558762872 * battery_mass**2 -0.022510378907086626 * battery_mass * cruise_speed + \
                        -0.04763256483978545 * cruise_speed**2 + 71.77120785036095

         
        empennage_weight = 7.57715283e-02 * tail_area  - 5.07300739e-02 * fin_area  + 8.42532575e-05 * tail_area**2 + 6.72483630e-02 * tail_area * fin_area  - 2.05722127e-03 * fin_area**2 + 70.80119198401702
        
        gross_weight_2 = 8.99868129 * wing_area + 161.90075337 * wing_AR + 40.98060689 * fuselage_length + 1.04094761 * battery_mass + 5.01979066  * cruise_speed + 746.7280307830879

        gross_weight = gross_weight_minus_empennage + empennage_weight

        self.register_output('gross_weight',gross_weight)
        self.register_output('gross_weight_2', gross_weight_2)


