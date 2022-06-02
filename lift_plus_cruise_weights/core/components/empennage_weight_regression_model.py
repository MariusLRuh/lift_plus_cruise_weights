import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

class EmpennageWeightRegressionModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
   
    def define(self):
        shape = self.parameters['shape']
    
        tail_area = self.declare_variable('tail_area', shape=shape)
        fin_area = self.declare_variable('fin_area', shape=shape)
         
        empennage_weight = 7.57715283e-02 * tail_area  - 5.07300739e-02 * fin_area  + 8.42532575e-05 * tail_area**2 + 6.72483630e-02 * tail_area * fin_area  - 2.05722127e-03 * fin_area**2 + 70.80119198401702
        
        self.register_output('empennage_weight',empennage_weight)
  
