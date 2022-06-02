import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from lift_plus_cruise_weights.core.weights_inputs_model import WeightsInputsModel
from lift_plus_cruise_weights.core.components.boom_weight_regression_model import BoomWeightRegressionModel
from lift_plus_cruise_weights.core.components.empennage_weight_regression_model import EmpennageWeightRegressionModel
from lift_plus_cruise_weights.core.components.fuselage_weight_regression_model import FuselageWeightRegressionModel
from lift_plus_cruise_weights.core.components.wing_weight_regression_model import WingWeightRegressionModel
from lift_plus_cruise_weights.core.components.total_structural_weight_regression_model import TotalStructuralWeightRegressionModel 
from lift_plus_cruise_weights.core.components.non_structural_weight_regression_model import NonStructuralWeightRegressionModel
# from lift_plus_cruise_weights.core.components.gross_weight_regression_model import GrossWeightRegressionModel


class CoreWeightsModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
       
        self.add(WeightsInputsModel(
            shape=shape,
        ), name='weights_inputs_model')
        
        self.add(BoomWeightRegressionModel(
            shape=shape,
        ),name='boom_weight_regression_model')
        
        self.add(EmpennageWeightRegressionModel(
            shape=shape,
        ),name='empennage_weight_regression_model')
        
        self.add(FuselageWeightRegressionModel(
            shape=shape,
        ), name='fuselage_weight_regression_model')
        
        self.add(WingWeightRegressionModel(
            shape=shape,
        ), name='wing_weight_regression_model')
        
        self.add(TotalStructuralWeightRegressionModel(
            shape=shape,
        ), )

        self.add(NonStructuralWeightRegressionModel(
            shape=shape,
        ),name='non_structural_weight_regression_model')


        boom_weight = self.declare_variable('boom_weight', shape=shape)
        empennage_weight = self.declare_variable('empennage_weight', shape=shape)
        fuselage_weight = self.declare_variable('fuselage_weight', shape=shape)
        wing_weight = self.declare_variable('wing_weight', shape=shape)
        non_structural_weight = self.declare_variable('non_structural_weight', shape=shape)

        total_structural_weight = boom_weight + empennage_weight + fuselage_weight + wing_weight
        gross_weight = total_structural_weight + non_structural_weight
    
        self.register_output('gross_weight', gross_weight)
        # self.add_objective('gross_weight')
