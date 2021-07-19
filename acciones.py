from pysnmp.hlapi import *
import config
import time
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import base64

#FUNCION GET 
def get(oid,ip):
    oid = oid + (0,)
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)


        result = ''
        for varBind in varBinds:
            result = result + (' = '.join([x.prettyPrint() for x in varBind]))
            
    except Exception as e:
        result = e

    return result
    
#FUNCION SET     
def set(oid,value,ip):
    oid = oid + (0,)
    try:
        iterator=setCmd(SnmpEngine(), 
               CommunityData('public', mpModel=1), 
               UdpTransportTarget((ip, 161)), 
               ContextData(), 
               ObjectType(ObjectIdentity(oid),value)
               )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        
        if errorIndication or errorStatus:
            error = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            result = errorIndication + error

        else:
            result = ''
            for varBind in varBinds:
                result = result + (' = '.join([x.prettyPrint() for x in varBind]))
    except Exception as e:
        result = e
        
    return result

#FUNCION WALK     
def walk(oid,ip):
    try:
        iterator = nextCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=1),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
            lexicographicMode=False
        )
        result = ''
        for errorIndication, errorStatus, errorIndex, varBinds in iterator:

            if errorIndication:
                print(errorIndication)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
                break

            else:
                
                for varBind in varBinds:
                    result = result + (' = '.join([x.prettyPrint() for x in varBind])) + "\n"
            
    except Exception as e:
        result = e
        
    return result
        

#Funcion sondeo
def sondeoAbs(oid,t_tot,n_m,ip):
    oid = oid + (0,)
    result=np.zeros(n_m)
    duerme=t_tot/n_m
    try:
        for i in range(n_m):
            iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
            )
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            aux=''
            for varBind in varBinds:
                aux = aux + (' = '.join([x.prettyPrint() for x in varBind]))
            valor=int(aux.split(' = ')[1])
            result[i]=valor
            time.sleep(duerme)
    except Exception as e:
        result = e

    return result


#Funcion sondeo
def sondeoDelta(oid,t_tot,n_m,ip):
    oid = oid + (0,)
    result=np.zeros(n_m)
    duerme=t_tot/n_m
    iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
            )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    aux=''
    for varBind in varBinds:
        aux = aux + (' = '.join([x.prettyPrint() for x in varBind]))
    previo=int(aux.split(' = ')[1])
    time.sleep(duerme)
    try:
        for i in range(n_m):
            iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
            )
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            aux=''
            for varBind in varBinds:
                aux = aux + (' = '.join([x.prettyPrint() for x in varBind]))
            valor=int(aux.split(' = ')[1])
            result[i]=valor-previo
            previo=valor
            time.sleep(duerme)
    except Exception as e:
        result = e

    return result



def getTabla(mibView, oid,ip):
    listado = []
    listado2=[]
    titulos = []
    try:
        for (errorIndication,errorStatus,errorIndex,varBinds) in nextCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((ip, 161)), ContextData(), 
            ObjectType(ObjectIdentity(oid)), lexicographicMode=False):
            if errorIndication:
                print(errorIndication)
                break
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), 
                                    file=sys.stderr)             
                break
            else:
                
                    
                    for varBind in varBinds:    
                        varName, varValue = varBind
                        
                        mibName, objectName, objectInstanceId = mibView.getNodeName(varName)

                        if objectName[-1] not in titulos:
                            titulos.append(objectName[-1])
                        
                        listado.append(int(str(objectInstanceId)))
                        listado2.append(str(varValue))

                        idx = '.'.join([str(indexPart) for indexPart in objectInstanceId])

        columna = []
        tabla = []

        for i in range(len(listado2)):

            if(i % max(listado) == 0 and i !=0):
                tabla.append(columna)
                columna = []
            columna.append(listado2[i])
            
            
        tabla.append(columna)
        tabla = np.array(tabla)
        tabla = np.transpose(tabla)
        tabla = np.insert(tabla, 0, titulos, axis=0)
        
    except Exception as e:
        print(e)

    return tabla

def createTable(tabla):         #Actualizar
    filename = 'tabla.txt'  # I assume you have a way of picking unique filenames
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(tabla)
        f.close()
