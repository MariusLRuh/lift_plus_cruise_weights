import numpy as np 
import csdl 
from csdl import Model 
import pandas as pd 

class EmpennageWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
    
        # htail_df = pd.read_csv('core/components/empennage/htail_linear_regression_model.csv')
        # vtail_df = pd.read_csv('core/components/empennage/vtail_linear_regression_model.csv')

        df = pd.read_csv('core/components/empennage/empennage_linear_regression_model.csv')
        
        # num_items = htail_df.shape[1]
        tail_area = self.declare_variable('tail_area', shape=shape)
        fin_area = self.declare_variable('fin_area', shape=shape)
        
        empennage_name_list = [
            'empennage_struct_mass',
            'empennage_struct_cg_x',
            'empennage_struct_cg_z',
            'empennage_struct_I_xx_global',
            'empennage_struct_I_yy_global',
            'empennage_struct_I_zz_global',
            'empennage_struct_I_xz_global',
        ]


        for i in range(len(empennage_name_list)):
            str = empennage_name_list[i]
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * tail_area + reg_coeff[1] * fin_area + reg_coeff[2] 
            # self.print_var(pred)
            self.register_output(str,pred)

  
