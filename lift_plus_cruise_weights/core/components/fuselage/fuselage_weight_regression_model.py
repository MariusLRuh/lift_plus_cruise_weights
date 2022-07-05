import numpy as np 
import pandas as pd
import csdl 
from csdl import Model 


from lift_plus_cruise_weights.regression_parameters import RegressionPararmeters


class FuselageWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        df = pd.read_csv('core/components/fuselage/fuselage_linear_regression_model.csv')
        num_items = df.shape[1]
       
        mass_str = 'mass'
        cg_str ='cg'

        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_mass = self.declare_variable('battery_mass', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)

        # Unit conversions 
        slug_ft_2_to_kg_m_2 = 1.35581795
        slug_to_kg = 14.5939
        ft_to_m = 0.3048

        mass_str = 'mass'
        cg_str ='cg'

        for i in range(10):
            str = df.columns[i]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5]
            if mass_str in str:
                out = pred * slug_to_kg
                # self.print_var(out)
                self.register_output(str, out)
            elif cg_str in str:
                out = pred * ft_to_m
                self.register_output(str, out)
            else:
                out = pred * slug_ft_2_to_kg_m_2
                self.register_output(str, out)

      