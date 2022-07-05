from email.policy import default
import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from lift_plus_cruise_weights.core.components.wing_boom_fuselage.wing_boom_fuselage_struct_regression_model import WingBoomFuselageStructRegressionModel
from lift_plus_cruise_weights.core.components.empennage.empennage_weight_regression_model import EmpennageWeightRegressionModel


class LiftPlusCruiseWeightsModel(Model):
    def initialize(self):
        self.parameters.declare('num_evaluations', default=1)
   
    def define(self):
        num_evaluations = self.parameters['num_evaluations']
        
        shape = (num_evaluations,)
        
        ft_2_to_m_2 = 1 / 10.764
        ft_to_m = 0.3048
        ktas_to_m_s = 1 / 1.944
        lbs_to_kg =  1 / 2.205

        self.declare_variable('wing_area', shape=shape, units='m^2' , val=210.28 * ft_2_to_m_2)
        self.declare_variable('wing_AR', shape=shape, val=12.1423)
        self.declare_variable('fuselage_length', shape=shape, units='m' ,val=30 * ft_to_m)
        self.declare_variable('battery_mass', shape=shape,units='kg', val=2675.27 * lbs_to_kg)
        self.declare_variable('cruise_speed', shape=shape, units='m/s', val=112 * ktas_to_m_s)
        self.declare_variable('tail_area', shape=shape, units='m^2', val=39.51 * ft_2_to_m_2)
        self.declare_variable('fin_area',shape=shape, units='m^2', val=27.34 * ft_2_to_m_2)
        

        self.add(WingBoomFuselageStructRegressionModel(
            shape=shape,
        ),name='wing_boom_fuselage_struct_regression_model')

        self.add(EmpennageWeightRegressionModel(
            shape=shape,
        ),name='empennage_weight_regression_model')
        

        wing_boom_fuselage_mass = self.declare_variable('wing_boom_fuselage_mass', shape=shape)
        wing_boom_fuselage_cg_x = self.declare_variable('wing_boom_fuselage_cg_x', shape=shape)
        wing_boom_fuselage_cg_y = self.declare_variable('wing_boom_fuselage_cg_y', shape=shape, val=0.0003731154194629254)
        wing_boom_fuselage_cg_z = self.declare_variable('wing_boom_fuselage_cg_z', shape=shape, val=2.05894386120297)
        wing_boom_fuselage_I_xx_global = self.declare_variable('wing_boom_fuselage_I_xx_global', shape=shape)
        wing_boom_fuselage_I_yy_global = self.declare_variable('wing_boom_fuselage_I_yy_global', shape=shape)
        wing_boom_fuselage_I_zz_global = self.declare_variable('wing_boom_fuselage_I_zz_global', shape=shape)
        wing_boom_fuselage_I_xy_global = self.declare_variable('wing_boom_fuselage_I_xy_global', shape=shape, val=0.023140980424183936)
        wing_boom_fuselage_I_xz_global = self.declare_variable('wing_boom_fuselage_I_xz_global', shape=shape, val=87.95770737327673)
        wing_boom_fuselage_I_yz_global = self.declare_variable('wing_boom_fuselage_I_yz_global', shape=shape, val=0.09904749249109371)


        empennage_mass = self.declare_variable('empennage_struct_mass', shape=shape)
        empennage_struct_cg_x = self.declare_variable('empennage_struct_cg_x',shape=shape)
        empennage_struct_cg_y = self.declare_variable('empennage_struct_cg_y',shape=shape,val=-4.647283670593032e-06)
        empennage_struct_cg_z = self.declare_variable('empennage_struct_cg_z',shape=shape)
        empennage_struct_I_xx_global = self.declare_variable('empennage_struct_I_xx_global',shape=shape)
        empennage_struct_I_yy_global = self.declare_variable('empennage_struct_I_yy_global',shape=shape)
        empennage_struct_I_zz_global = self.declare_variable('empennage_struct_I_zz_global',shape=shape)
        empennage_struct_I_xy_global = self.declare_variable('empennage_struct_I_xy_global',shape=shape,val=0.004868287408908892)
        empennage_struct_I_xz_global = self.declare_variable('empennage_struct_I_xz_global',shape=shape)
        empennage_struct_I_yz_global = self.declare_variable('empennage_struct_I_yz_global',shape=shape,val=0.0034687070026175955)


        total_mass = wing_boom_fuselage_mass + empennage_mass
        cg_x = (wing_boom_fuselage_cg_x * wing_boom_fuselage_mass + empennage_struct_cg_x * empennage_mass)/ total_mass
        cg_y = (wing_boom_fuselage_cg_y * wing_boom_fuselage_mass + empennage_struct_cg_y * empennage_mass)/ total_mass
        cg_z = (wing_boom_fuselage_cg_z * wing_boom_fuselage_mass + empennage_struct_cg_z * empennage_mass)/ total_mass

        Ixx = wing_boom_fuselage_I_xx_global + empennage_struct_I_xx_global
        Iyy = wing_boom_fuselage_I_yy_global + empennage_struct_I_yy_global
        Izz = wing_boom_fuselage_I_zz_global + empennage_struct_I_zz_global
        Ixy = wing_boom_fuselage_I_xy_global + empennage_struct_I_xy_global
        Ixz = wing_boom_fuselage_I_xz_global + empennage_struct_I_xz_global
        Iyz = wing_boom_fuselage_I_yz_global + empennage_struct_I_yz_global

        self.register_output('mass', total_mass)
        self.register_output('cgx', cg_x)
        self.register_output('cgy', cg_y)
        self.register_output('cgz', cg_z)
        self.register_output('ixx', Ixx)
        self.register_output('iyy', Iyy)
        self.register_output('izz', Izz)
        self.register_output('ixy', Ixy)
        self.register_output('ixz', Ixz)
        self.register_output('iyz', Iyz)


