import numpy as np 
import csdl 
from csdl import Model 
import pandas as pd

from lift_plus_cruise_weights.regression_parameters import RegressionPararmeters

class BoomWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
        
    def define(self):
        shape = self.parameters['shape']
        
        df = pd.read_csv('core/components/boom/boom_linear_regression_model.csv')
        num_items = df.shape[1]
        
        # regression_parameters = self.parameters['regression_parameters']
       
        wing_area = self.declare_variable('wing_area', shape=shape)
        wing_AR = self.declare_variable('wing_AR', shape=shape)
        fuselage_length = self.declare_variable('fuselage_length', shape=shape)
        battery_weight = self.declare_variable('battery_weight', shape=shape)
        cruise_speed = self.declare_variable('cruise_speed', shape=shape)
      
        # Unit conversions 
        slug_to_lbs = 32.1740
        slug_ft_2_to_kg_m_2 = 1.35581795
        slug_to_kg = 14.5939
        ft_to_m = 0.3048

        mass_str = 'mass'
        cg_str ='cg'

        for i in range(10):
            str = df.columns[i]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_weight + reg_coeff[4] * cruise_speed + reg_coeff[5]
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

        for i in range(10):
            index = i + 16
            str = df.columns[index]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_weight + reg_coeff[4] * cruise_speed + reg_coeff[5]
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

        for i in range(10):
            index = i + 32
            str = df.columns[index]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_weight + reg_coeff[4] * cruise_speed + reg_coeff[5]
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

        for i in range(10):
            index = i + 48
            str = df.columns[index]
            print(str)
            reg_coeff = df[str].to_numpy()
            pred = reg_coeff[0] * wing_area + reg_coeff[1] * wing_AR + reg_coeff[2] * fuselage_length + reg_coeff[3] * battery_weight + reg_coeff[4] * cruise_speed + reg_coeff[5]
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
            
            # # self.print_var(out)
            
            



        # boom_weight =  6.64226897e-01 * wing_area + 1.18429889e+01 * wing_AR -3.00395573e-01 * fuselage_length -1.22160336e-03 * battery_weight -1.18242922e-02 * cruise_speed - 15.090980695937446
        # self.register_output('boom_total_structural_weight',boom_weight)

        # boom_inner_right_cg_x = regression_parameters['BoomInStar_struct_cg_X'][0] * wing_area + regression_parameters['BoomInStar_struct_cg_X'][1] * wing_AR + regression_parameters['BoomInStar_struct_cg_X'][2] * fuselage_length + regression_parameters['BoomInStar_struct_cg_X'][3] * battery_weight + regression_parameters['BoomInStar_struct_cg_X'][4] * cruise_speed + regression_parameters['BoomInStar_struct_cg_X'][5]
        # boom_inner_right_cg_y = regression_parameters['BoomInStar_struct_cg_Y'][0] * wing_area + regression_parameters['BoomInStar_struct_cg_Y'][1] * wing_AR + regression_parameters['BoomInStar_struct_cg_Y'][2] * fuselage_length + regression_parameters['BoomInStar_struct_cg_Y'][3] * battery_weight + regression_parameters['BoomInStar_struct_cg_Y'][4] * cruise_speed + regression_parameters['BoomInStar_struct_cg_Y'][5]
        # boom_inner_right_cg_z = regression_parameters['BoomInStar_struct_cg_Z'][0] * wing_area + regression_parameters['BoomInStar_struct_cg_Z'][1] * wing_AR + regression_parameters['BoomInStar_struct_cg_Z'][2] * fuselage_length + regression_parameters['BoomInStar_struct_cg_Z'][3] * battery_weight + regression_parameters['BoomInStar_struct_cg_Z'][4] * cruise_speed + regression_parameters['BoomInStar_struct_cg_Z'][5]
        # boom_inner_right_Ixx = regression_parameters['BoomInStar_struct_Ixx_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Ixx_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Ixx_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Ixx_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Ixx_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Ixx_local'][5]
        # boom_inner_right_Iyy = regression_parameters['BoomInStar_struct_Iyy_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Iyy_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Iyy_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Iyy_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Iyy_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Iyy_local'][5]
        # boom_inner_right_Izz = regression_parameters['BoomInStar_struct_Izz_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Izz_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Izz_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Izz_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Izz_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Izz_local'][5]
        # boom_inner_right_Ixy = regression_parameters['BoomInStar_struct_Ixy_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Ixy_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Ixy_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Ixy_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Ixy_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Ixy_local'][5]
        # boom_inner_right_Ixz = regression_parameters['BoomInStar_struct_Ixz_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Ixz_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Ixz_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Ixz_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Ixz_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Ixz_local'][5]
        # boom_inner_right_Iyz = regression_parameters['BoomInStar_struct_Iyz_local'][0] * wing_area + regression_parameters['BoomInStar_struct_Iyz_local'][1] * wing_AR + regression_parameters['BoomInStar_struct_Iyz_local'][2] * fuselage_length + regression_parameters['BoomInStar_struct_Iyz_local'][3] * battery_weight + regression_parameters['BoomInStar_struct_Iyz_local'][4] * cruise_speed + regression_parameters['BoomInStar_struct_Iyz_local'][5]
        
        # boom_outer_right_cg_x = regression_parameters['BoomOutStar_struct_cg_X'][0] * wing_area + regression_parameters['BoomOutStar_struct_cg_X'][1] * wing_AR + regression_parameters['BoomOutStar_struct_cg_X'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_cg_X'][3] * battery_weight + regression_parameters['BoomOutStar_struct_cg_X'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_cg_X'][5]
        # boom_outer_right_cg_y = regression_parameters['BoomOutStar_struct_cg_Y'][0] * wing_area + regression_parameters['BoomOutStar_struct_cg_Y'][1] * wing_AR + regression_parameters['BoomOutStar_struct_cg_Y'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_cg_Y'][3] * battery_weight + regression_parameters['BoomOutStar_struct_cg_Y'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_cg_Y'][5]
        # boom_outer_right_cg_z = regression_parameters['BoomOutStar_struct_cg_Z'][0] * wing_area + regression_parameters['BoomOutStar_struct_cg_Z'][1] * wing_AR + regression_parameters['BoomOutStar_struct_cg_Z'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_cg_Z'][3] * battery_weight + regression_parameters['BoomOutStar_struct_cg_Z'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_cg_Z'][5]
        # boom_outer_right_Ixx = regression_parameters['BoomOutStar_struct_Ixx_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Ixx_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Ixx_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Ixx_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Ixx_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Ixx_local'][5]
        # boom_outer_right_Iyy = regression_parameters['BoomOutStar_struct_Iyy_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Iyy_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Iyy_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Iyy_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Iyy_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Iyy_local'][5]
        # boom_outer_right_Izz = regression_parameters['BoomOutStar_struct_Izz_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Izz_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Izz_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Izz_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Izz_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Izz_local'][5]
        # boom_outer_right_Ixy = regression_parameters['BoomOutStar_struct_Ixy_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Ixy_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Ixy_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Ixy_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Ixy_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Ixy_local'][5]
        # boom_outer_right_Ixz = regression_parameters['BoomOutStar_struct_Ixz_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Ixz_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Ixz_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Ixz_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Ixz_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Ixz_local'][5]
        # boom_outer_right_Iyz = regression_parameters['BoomOutStar_struct_Iyz_local'][0] * wing_area + regression_parameters['BoomOutStar_struct_Iyz_local'][1] * wing_AR + regression_parameters['BoomOutStar_struct_Iyz_local'][2] * fuselage_length + regression_parameters['BoomOutStar_struct_Iyz_local'][3] * battery_weight + regression_parameters['BoomOutStar_struct_Iyz_local'][4] * cruise_speed + regression_parameters['BoomOutStar_struct_Iyz_local'][5]
    
        # boom_inner_left_cg_x = regression_parameters['BoomInPort_struct_cg_X'][0] * wing_area + regression_parameters['BoomInPort_struct_cg_X'][1] * wing_AR + regression_parameters['BoomInPort_struct_cg_X'][2] * fuselage_length + regression_parameters['BoomInPort_struct_cg_X'][3] * battery_weight + regression_parameters['BoomInPort_struct_cg_X'][4] * cruise_speed + regression_parameters['BoomInPort_struct_cg_X'][5]
        # boom_inner_left_cg_y = regression_parameters['BoomInPort_struct_cg_Y'][0] * wing_area + regression_parameters['BoomInPort_struct_cg_Y'][1] * wing_AR + regression_parameters['BoomInPort_struct_cg_Y'][2] * fuselage_length + regression_parameters['BoomInPort_struct_cg_Y'][3] * battery_weight + regression_parameters['BoomInPort_struct_cg_Y'][4] * cruise_speed + regression_parameters['BoomInPort_struct_cg_Y'][5]
        # boom_inner_left_cg_z = regression_parameters['BoomInPort_struct_cg_Z'][0] * wing_area + regression_parameters['BoomInPort_struct_cg_Z'][1] * wing_AR + regression_parameters['BoomInPort_struct_cg_Z'][2] * fuselage_length + regression_parameters['BoomInPort_struct_cg_Z'][3] * battery_weight + regression_parameters['BoomInPort_struct_cg_Z'][4] * cruise_speed + regression_parameters['BoomInPort_struct_cg_Z'][5]
        # boom_inner_left_Ixx = regression_parameters['BoomInPort_struct_Ixx_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Ixx_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Ixx_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Ixx_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Ixx_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Ixx_local'][5]
        # boom_inner_left_Iyy = regression_parameters['BoomInPort_struct_Iyy_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Iyy_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Iyy_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Iyy_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Iyy_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Iyy_local'][5]
        # boom_inner_left_Izz = regression_parameters['BoomInPort_struct_Izz_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Izz_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Izz_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Izz_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Izz_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Izz_local'][5]
        # boom_inner_left_Ixy = regression_parameters['BoomInPort_struct_Ixy_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Ixy_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Ixy_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Ixy_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Ixy_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Ixy_local'][5]
        # boom_inner_left_Ixz = regression_parameters['BoomInPort_struct_Ixz_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Ixz_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Ixz_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Ixz_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Ixz_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Ixz_local'][5]
        # boom_inner_left_Iyz = regression_parameters['BoomInPort_struct_Iyz_local'][0] * wing_area + regression_parameters['BoomInPort_struct_Iyz_local'][1] * wing_AR + regression_parameters['BoomInPort_struct_Iyz_local'][2] * fuselage_length + regression_parameters['BoomInPort_struct_Iyz_local'][3] * battery_weight + regression_parameters['BoomInPort_struct_Iyz_local'][4] * cruise_speed + regression_parameters['BoomInPort_struct_Iyz_local'][5]
        
        # boom_outer_left_cg_x = regression_parameters['BoomOutPort_struct_cg_X'][0] * wing_area + regression_parameters['BoomOutPort_struct_cg_X'][1] * wing_AR + regression_parameters['BoomOutPort_struct_cg_X'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_cg_X'][3] * battery_weight + regression_parameters['BoomOutPort_struct_cg_X'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_cg_X'][5]
        # boom_outer_left_cg_y = regression_parameters['BoomOutPort_struct_cg_Y'][0] * wing_area + regression_parameters['BoomOutPort_struct_cg_Y'][1] * wing_AR + regression_parameters['BoomOutPort_struct_cg_Y'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_cg_Y'][3] * battery_weight + regression_parameters['BoomOutPort_struct_cg_Y'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_cg_Y'][5]
        # boom_outer_left_cg_z = regression_parameters['BoomOutPort_struct_cg_Z'][0] * wing_area + regression_parameters['BoomOutPort_struct_cg_Z'][1] * wing_AR + regression_parameters['BoomOutPort_struct_cg_Z'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_cg_Z'][3] * battery_weight + regression_parameters['BoomOutPort_struct_cg_Z'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_cg_Z'][5]
        # boom_outer_left_Ixx = regression_parameters['BoomOutPort_struct_Ixx_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Ixx_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Ixx_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Ixx_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Ixx_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Ixx_local'][5]
        # boom_outer_left_Iyy = regression_parameters['BoomOutPort_struct_Iyy_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Iyy_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Iyy_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Iyy_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Iyy_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Iyy_local'][5]
        # boom_outer_left_Izz = regression_parameters['BoomOutPort_struct_Izz_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Izz_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Izz_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Izz_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Izz_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Izz_local'][5]
        # boom_outer_left_Ixy = regression_parameters['BoomOutPort_struct_Ixy_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Ixy_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Ixy_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Ixy_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Ixy_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Ixy_local'][5]
        # boom_outer_left_Ixz = regression_parameters['BoomOutPort_struct_Ixz_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Ixz_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Ixz_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Ixz_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Ixz_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Ixz_local'][5]
        # boom_outer_left_Iyz = regression_parameters['BoomOutPort_struct_Iyz_local'][0] * wing_area + regression_parameters['BoomOutPort_struct_Iyz_local'][1] * wing_AR + regression_parameters['BoomOutPort_struct_Iyz_local'][2] * fuselage_length + regression_parameters['BoomOutPort_struct_Iyz_local'][3] * battery_weight + regression_parameters['BoomOutPort_struct_Iyz_local'][4] * cruise_speed + regression_parameters['BoomOutPort_struct_Iyz_local'][5]
        
        # boom_inner_right_cg = self.create_output('boom_inner_right_cg', shape=(shape[0],3))
        # boom_inner_right_I = self.create_output('boom_inner_right_I', shape=(shape[0],3,3)) 
        # boom_inner_right_cg[:,0] = csdl.reshape(boom_inner_right_cg_x,new_shape=(shape[0],1))
        # boom_inner_right_cg[:,1] = csdl.reshape(boom_inner_right_cg_y,new_shape=(shape[0],1))
        # boom_inner_right_cg[:,2] = csdl.reshape(boom_inner_right_cg_z,new_shape=(shape[0],1))
        # boom_inner_right_I[:,0,0] = csdl.reshape(boom_inner_right_Ixx,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,0,1] = csdl.reshape(boom_inner_right_Ixy,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,0,2] = csdl.reshape(boom_inner_right_Ixz,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,1,0] = csdl.reshape(boom_inner_right_Ixy,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,1,1] = csdl.reshape(boom_inner_right_Iyy,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,1,2] = csdl.reshape(boom_inner_right_Iyz,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,2,0] = csdl.reshape(boom_inner_right_Ixz,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,2,1] = csdl.reshape(boom_inner_right_Iyz,new_shape=(shape[0],1,1))
        # boom_inner_right_I[:,2,2] = csdl.reshape(boom_inner_right_Izz,new_shape=(shape[0],1,1))
        
        # boom_outer_right_cg = self.create_output('boom_outer_right_cg', shape=(shape[0],3))
        # boom_outer_right_I = self.create_output('boom_outer_right_I', shape=(shape[0],3,3))
        # boom_outer_right_cg[:,0] = csdl.reshape(boom_outer_right_cg_x,new_shape=(shape[0],1))
        # boom_outer_right_cg[:,1] = csdl.reshape(boom_outer_right_cg_y,new_shape=(shape[0],1))
        # boom_outer_right_cg[:,2] = csdl.reshape(boom_outer_right_cg_z,new_shape=(shape[0],1))
        # boom_outer_right_I[:,0,0] = csdl.reshape(boom_outer_right_Ixx,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,0,1] = csdl.reshape(boom_outer_right_Ixy,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,0,2] = csdl.reshape(boom_outer_right_Ixz,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,1,0] = csdl.reshape(boom_outer_right_Ixy,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,1,1] = csdl.reshape(boom_outer_right_Iyy,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,1,2] = csdl.reshape(boom_outer_right_Iyz,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,2,0] = csdl.reshape(boom_outer_right_Ixz,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,2,1] = csdl.reshape(boom_outer_right_Iyz,new_shape=(shape[0],1,1))
        # boom_outer_right_I[:,2,2] = csdl.reshape(boom_outer_right_Izz,new_shape=(shape[0],1,1))
        
        # boom_inner_left_cg = self.create_output('boom_inner_left_cg', shape=(shape[0],3))
        # boom_inner_left_I = self.create_output('boom_inner_left_I', shape=(shape[0],3,3))
        # boom_inner_left_cg[:,0] = csdl.reshape(boom_inner_left_cg_x,new_shape=(shape[0],1))
        # boom_inner_left_cg[:,1] = csdl.reshape(boom_inner_left_cg_y,new_shape=(shape[0],1))
        # boom_inner_left_cg[:,2] = csdl.reshape(boom_inner_left_cg_z,new_shape=(shape[0],1))
        # boom_inner_left_I[:,0,0] = csdl.reshape(boom_inner_left_Ixx,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,0,1] = csdl.reshape(boom_inner_left_Ixy,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,0,2] = csdl.reshape(boom_inner_left_Ixz,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,1,0] = csdl.reshape(boom_inner_left_Ixy,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,1,1] = csdl.reshape(boom_inner_left_Iyy,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,1,2] = csdl.reshape(boom_inner_left_Iyz,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,2,0] = csdl.reshape(boom_inner_left_Ixz,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,2,1] = csdl.reshape(boom_inner_left_Iyz,new_shape=(shape[0],1,1))
        # boom_inner_left_I[:,2,2] = csdl.reshape(boom_inner_left_Izz,new_shape=(shape[0],1,1))

        # boom_outer_left_cg = self.create_output('boom_outer_left_cg', shape=(shape[0],3))
        # boom_outer_left_I = self.create_output('boom_outer_left_I', shape=(shape[0],3,3))
        # boom_outer_left_cg[:,0] = csdl.reshape(boom_outer_left_cg_x,new_shape=(shape[0],1))
        # boom_outer_left_cg[:,1] = csdl.reshape(boom_outer_left_cg_y,new_shape=(shape[0],1))
        # boom_outer_left_cg[:,2] = csdl.reshape(boom_outer_left_cg_z,new_shape=(shape[0],1))
        # boom_outer_left_I[:,0,0] = csdl.reshape(boom_outer_left_Ixx,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,0,1] = csdl.reshape(boom_outer_left_Ixy,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,0,2] = csdl.reshape(boom_outer_left_Ixz,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,1,0] = csdl.reshape(boom_outer_left_Ixy,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,1,1] = csdl.reshape(boom_outer_left_Iyy,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,1,2] = csdl.reshape(boom_outer_left_Iyz,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,2,0] = csdl.reshape(boom_outer_left_Ixz,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,2,1] = csdl.reshape(boom_outer_left_Iyz,new_shape=(shape[0],1,1))
        # boom_outer_left_I[:,2,2] = csdl.reshape(boom_outer_left_Izz,new_shape=(shape[0],1,1))


