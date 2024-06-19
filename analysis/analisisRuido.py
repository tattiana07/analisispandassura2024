import pandas as pd
from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido():
    #Creando un dataFrame
    datosRuido=generarDatosRuido()
    ruidoDataFrame=pd.DataFrame(datosRuido,columns=["id","nivel","ruido","comuna"])
    ruidoDataFrame.to_csv("ruido.csv",index=False)

construirDataRuido()