import numpy as np 
import pandas as pd 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class WingWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']

        df = pd.read_csv('core/components/wing/wing_linear_regression_model.csv')
        num_items = df.shape[1]
        
        # each component (e.g. gear_nose) has mass, 3 cg coordinates, 6 local inertia tensor entries and 6 global inertia tensor entries 
        num_components = int(num_items/16)
        items_str = df.columns
        # print(items_str[0])
        # print(df[items_str[0]].to_numpy())

        mass_str = 'mass'
        cg_str ='cg'
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_mass = self.declare_variable('battery_mass', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
    
        # Unit conversions 
        slug_to_lbs = 32.1740
        slug_ft_2_to_kg_m_2 = 1.35581795
        slug_to_kg = 14.5939
        ft_to_m = 0.3048


        cg_counter = 0
        I_counter = 0
        # I_counter = 0
        for i in range(10):
            str = df.columns[i]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5]
            if mass_str in str:
                # print(str)
                out = pred * slug_to_kg
                # self.print_var(out)
                self.register_output(str, out)
            elif cg_str in str:
                # print(str)
                out = pred * ft_to_m
                # self.print_var(out)
                self.register_output(str, out)
            else:
                # print(str)
                out = pred * slug_ft_2_to_kg_m_2
                # self.print_var(out)
                self.register_output(str, out)
            
            
            # if mass_str in str:
            #     out_str = str.replace(str,'wing_struct_weight')
            #     reg_coeff = df[str].to_numpy()
            #     self.register_output(out_str, (reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5]) * slug_to_lbs)
            # elif cg_str in str:
            #     reg_coeff = df[str].to_numpy()
            #     if cg_counter == 0:
            #         cg_list = []
            #     cg_list.append(reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5])
            #     cg_counter += 1
            #     if cg_counter == 3:
            #         out_str = str[0:12] + 'cg'
            #         output = self.create_output(out_str,shape=(shape[0],3))
            #         output[:,0] = csdl.reshape(cg_list[0],new_shape=(shape[0],1))
            #         output[:,1] = csdl.reshape(cg_list[1],new_shape=(shape[0],1))
            #         output[:,2] = csdl.reshape(cg_list[2],new_shape=(shape[0],1))
            #         cg_counter = 0 
            # elif I_str_local in str:
            #     reg_coeff = df[str].to_numpy()
            #     if I_counter == 0:
            #         I_list = []
            #     I_list.append(reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5])
            #     I_counter += 1
            #     if I_counter == 6:
            #         out_str = str[0:12] + 'I_local'
            #         output = self.create_output(out_str,shape=(shape[0],3,3))
            #         output[:,0,0] = csdl.reshape(I_list[0],new_shape=(shape[0],1,1))
            #         output[:,1,1] = csdl.reshape(I_list[1],new_shape=(shape[0],1,1))
            #         output[:,2,2] = csdl.reshape(I_list[2],new_shape=(shape[0],1,1))
            #         output[:,0,1] = csdl.reshape(I_list[3],new_shape=(shape[0],1,1))
            #         output[:,0,2] = csdl.reshape(I_list[4],new_shape=(shape[0],1,1))
            #         output[:,1,2] = csdl.reshape(I_list[5],new_shape=(shape[0],1,1))
                    
            #         output[:,1,0] = csdl.reshape(I_list[3],new_shape=(shape[0],1,1))
            #         output[:,2,0] = csdl.reshape(I_list[4],new_shape=(shape[0],1,1))
            #         output[:,2,1] = csdl.reshape(I_list[5],new_shape=(shape[0],1,1))
                    
            #         I_counter = 0 
            
            # elif I_str_global in str:
            #     reg_coeff = df[str].to_numpy()
            #     if I_counter == 0:
            #         I_list = []
            #     I_list.append(reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_mass + reg_coeff[4] * cruise_speed + reg_coeff[5])
            #     I_counter += 1
            #     if I_counter == 6:
            #         out_str = str[0:12] + 'I_global'
            #         output = self.create_output(out_str,shape=(shape[0],3,3))
            #         output[:,0,0] = csdl.reshape(I_list[0],new_shape=(shape[0],1,1))
            #         output[:,1,1] = csdl.reshape(I_list[1],new_shape=(shape[0],1,1))
            #         output[:,2,2] = csdl.reshape(I_list[2],new_shape=(shape[0],1,1))
            #         output[:,0,1] = csdl.reshape(I_list[3],new_shape=(shape[0],1,1))
            #         output[:,0,2] = csdl.reshape(I_list[4],new_shape=(shape[0],1,1))
            #         output[:,1,2] = csdl.reshape(I_list[5],new_shape=(shape[0],1,1))
                    
            #         output[:,1,0] = csdl.reshape(I_list[3],new_shape=(shape[0],1,1))
            #         output[:,2,0] = csdl.reshape(I_list[4],new_shape=(shape[0],1,1))
            #         output[:,2,1] = csdl.reshape(I_list[5],new_shape=(shape[0],1,1))
                    
            #         I_counter = 0 



        # # for i in range(num_components):
        # #     if (i) % 16:
        # #     index = i * (1 + )

        # wing_weight =   3.16517210e+00 * wing_area + 4.98717495e+01 * wing_AR + 2.56574260e+00 * fuselage_length + 2.31695801e-02 * battery_mass -1.37015474e-01 * cruise_speed  -878.4384764733035
        # self.register_output('wing_structural_weight',wing_weight)

