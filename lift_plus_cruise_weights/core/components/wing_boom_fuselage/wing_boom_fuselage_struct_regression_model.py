import numpy as np 
import csdl 
from csdl import Model 
import pandas as pd 

class WingBoomFuselageStructRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
    
        # df = pd.read_csv('core/components/wing_boom_fuselage/wing_boom_fuselage_struct_regression_model.csv')
        df = pd.read_csv('core/components/wing_boom_fuselage/wing_boom_fuselage_regression_model_metric_2.csv')
       

        wing_boom_fuselage_list = [
            'wing_boom_fuselage_mass',
            'wing_boom_fuselage_cg_x',
            'wing_boom_fuselage_I_xx_global',
            'wing_boom_fuselage_I_yy_global',
            'wing_boom_fuselage_I_zz_global',
        ]    

        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_weight = self.declare_variable('battery_weight', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
        
        for i in range(len(wing_boom_fuselage_list)):
            str = wing_boom_fuselage_list[i]
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_weight + reg_coeff[4] * cruise_speed + reg_coeff[5]
            self.register_output(str,pred)
