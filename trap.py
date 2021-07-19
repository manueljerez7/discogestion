from pysnmp.hlapi import *
from pysnmp.smi import builder, view, compiler, error
import os
import time
import asyncio
from threading import Thread

async def monitorizarABSMayor(mibView, oid, umbral, intervalo):
    print("Monitorizando ", oid)
    oid = oid + (0,)

    while True:
        await asyncio.sleep(intervalo)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        value = varBinds[0][1]

        if(value > umbral):
            result = "======\nTRAP: El {} es mayor que {} (value={})\n======".format(oid,umbral,value)
            return result

async def monitorizarABSMenor(mibView, oid, umbral, intervalo):
    print("Monitorizando ", oid)
    oid = oid + (0,)

    while True:
        await asyncio.sleep(intervalo)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        value = varBinds[0][1]

        if(value < umbral):
            result = "======\nTRAP: El {} es menor que {} (value={})\n======".format(oid,umbral,value)
            return result


async def monitorizarDeltaMayor(mibView, oid, umbral, intervalo):
    print("Monitorizando ", oid)
    umbral = float(umbral)
    oid = oid + (0,)
    iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    anterior = float(varBinds[0][1])

    while True:
        await asyncio.sleep(intervalo)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        value = float(varBinds[0][1])

        if((value-anterior) > umbral):
            result = "======\nTRAP: El {} es mayor que {} (value={})\n======".format(oid,umbral,(value-anterior))
            print("Saliendo del trap ", oid)
            return result

        anterior = value
async def monitorizarDeltaMenor(mibView, oid, umbral, intervalo):
    print("Monitorizando ", oid)
    umbral = float(umbral)
    oid = oid + (0,)
    iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    anterior = float(varBinds[0][1])

    while True:
        await asyncio.sleep(intervalo)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        value = float(varBinds[0][1])

        if((value-anterior) < umbral):
            result = "======\nTRAP: El {} es menor que {} (value={})\n======".format(oid,umbral,(value-anterior))
            print("Saliendo del trap ", oid)
            return result

        anterior = value

