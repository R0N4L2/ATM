# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:13:48 2019

@author: Ronald Castillo Capino
"""
from doopl.factory import *
import pandas as pd
import os

dr=str(os.getcwdb())[2:-1].replace("\\\\","/")
def FuncionJoshua(ATMd,dist,Tecnicos): # Aqui iria la funcion de Joshua para que ingrese la datay haga los calculs respectivos.
    # Create an OPL model from a .mod file
    with create_opl_model(model=dr+"/reparacionATM.mod") as opl:
        # tuple can be a list of tuples, a pandas dataframe...
        opl.set_input("TupleSet1", tuples)
    
        # Generate the problem and solve it.
        opl.run()
    
        # Get the names of post processing tables
        print("Table names are: "+ str(opl.output_table_names))
    
        # Get all the post processing tables as dataframes.
        for name, table in iteritems(opl.report):
            print("Table : " + name)
            for t in table.itertuples(index=False):
                print(t)


dr=str(os.getcwdb())[2:-1].replace("\\\\","/")
ATMs=pd.read_excel(dr+"/DatosparaTodaslasFechas.xlsx",sheet_name="atmInformation")
Tecnicos=pd.read_excel(dr+"/DatosparaTodaslasFechas.xlsx",sheet_name="tecnicoInfo")
Distancias=pd.read_excel(dr+"/DatosparaTodaslasFechas.xlsx",sheet_name="m")
for k in ATMs['date'].drop_duplicates():
    ATMd=ATMs[ATMs['date']==k][['ATM','ATM ID','maxDesplazamiento','tiempoReparacionAvg','maxLlegada']].reset_index(drop=True)
    ids=pd.concat([Tecnicos['ubicacionInicial'],ATMd['ATM']]).values.tolist()
    dist=Distancias[Distancias['loc1'].isin(ids)&Distancias['loc2'].isin(ids)].reset_index(drop=True)
    #FuncionJoshua(ATMd,dist,Tecnicos) Aqui iria la funcion de Joshua para que ingrese la datay haga los calculs respectivos.
    