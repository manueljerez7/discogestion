import discord
from pysnmp.hlapi import *
from pysnmp.smi import builder, view, compiler, error
import config
import time
import matplotlib.pyplot as plt
from acciones import *
from traductor import traductor
import os
import numpy as np
from tabulate import tabulate
from traductor import traductorInverso
from informe import *
from trap import *

# Create MIB loader/builder
mibBuilder = builder.MibBuilder()

# Optionally set an alternative path to compiled MIBs
print('Setting MIB sources...')
mibBuilder.addMibSources(builder.DirMibSource(os.path.join( os.getcwd(), 'mibs')))
print(mibBuilder.getMibSources())
print('done')

print('Loading MIB modules...'),
mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-FRAMEWORK-MIB', 'SNMP-COMMUNITY-MIB', 'SNMPv2-SMI', 'RFC1213-MIB', 'HOST-RESOURCES-MIB', 'IF-MIB')
print('done')

print('Indexing MIB objects...'),
mibView = view.MibViewController(mibBuilder)
print('done')

cfg = config.Config(".config")
TOKEN = cfg["TOKEN"]

dicc={'local':'localhost'}

client = discord.Client()
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    else:
        if(message.content.startswith("$help")):
            await message.channel.send("Los comandos disponibles son:\n\n  $help: muestra la ayuda\n\n  $add [NOMBRE] [IP]: Añade un equipo con un nombre especificando su IP. Por defecto, viene creada la pareja {'local':'localhost'}\n\n  $snmp get [OID] [EQUIPO]: Realiza un get usando el protocolo SNMP\n \n $snmp set [OID] [EQUIPO] [VALUE]: Realiza un set usando el protocolo SNMP\n\n $snmp walk [OID] [EQUIPO]: Realiza un walk de una tabla usando el protocolo SNMP\n\n $snmp tabla [OID] [EQUIPO]: Devuelve una tabla en formato .txt\n\n $sondeo ABS/DELTA [OID] [TIEMPO:SEGUNDOS] [NUMERO-MUESTRAS] [EQUIPO]: Realiza un sondeo de la variable especificada\n\n $snmp informe [EQUIPO]\n\n $monitorizar [MODO(ABS o DELTA)] [mayor/menor] [OID] [umbral] [intervalo(segundos)]\n\n NO HACE FALTA INTRODUCIR EL .0 AL INTRODUCIR EL OID\n\n")
        
        if(message.content.startswith("$add")):
            argumentos = message.content.split(' ')
            dicc[argumentos[1]]=argumentos[2]
            await message.channel.send("Se ha añadido el equipo con dirección IP "+argumentos[2]+" con el nombre "+argumentos[1])

        if(message.content.startswith("$snmp")):
            if(message.content.startswith("$snmp get")):
                argumentos = message.content.split(' ')
                oid = traductor(mibView,argumentos[2])
                result = get(oid,dicc[argumentos[3]])
                #traductorInverso(mibView, oid)
                await message.channel.send(result)

            if(message.content.startswith("$snmp set")):
                argumentos = message.content.split(' ')
                oid = traductor(mibView,argumentos[2])
                values = argumentos[4:]
                value = ' '.join(values)
                result = set(oid, value,dicc[argumentos[3]])
                await message.channel.send(result)

            if(message.content.startswith("$snmp walk")):
                argumentos = message.content.split(' ')
                oid = traductor(mibView, argumentos[2])
                result = walk(oid,dicc[argumentos[3]])
                
                #nMensajes = np.ceil(longitud/2000)
                #for i in range(nMensajes):
                with open('walk.txt', 'w', encoding='utf-8') as f:
                    f.write(result)
                    f.close()
                    
                await message.channel.send(file=discord.File('walk.txt'))
            
            if(message.content.startswith("$snmp tabla")):
                argumentos = message.content.split(' ')
                oid = traductor(mibView, argumentos[2])
                tabla = getTabla(mibView,oid,dicc[argumentos[3]])
                tabla=tabulate(tabla)
                createTable(tabla)

                await message.channel.send(file=discord.File('tabla.txt'))
                
            if(message.content.startswith("$snmp informe")):
                argumentos = message.content.split(' ')
                getInforme(mibView,dicc[argumentos[2]])
                
                await message.channel.send(file=discord.File('informe.pdf'))
                

        if(message.content.startswith("$sondeo ABS")):
            argumentos = message.content.split(' ')
            oid = traductor(mibView, argumentos[2])
            tiempo=int(argumentos[3])
            numero=int(argumentos[4])
            vector = sondeoAbs(oid,tiempo,numero,dicc[argumentos[5]])
            plt.figure()
            plt.plot(np.arange(numero),vector)
            plt.grid()
            plt.title('Sondeo del valor absoluto de '+argumentos[2]+' durante '+argumentos[3]+'s')
            plt.plot()
            plt.savefig('figura.png')
            await message.channel.send(file=discord.File('figura.png'))
            
            
        if(message.content.startswith("$sondeo DELTA")):
            argumentos = message.content.split(' ')
            oid = traductor(mibView, argumentos[2])
            tiempo=int(argumentos[3])
            numero=int(argumentos[4])
            vector = sondeoDelta(oid,tiempo,numero,dicc[argumentos[5]])
            plt.figure()
            plt.plot(np.arange(numero),vector)
            plt.grid()
            plt.title('Sondeo del incremento de '+argumentos[2]+' durante '+argumentos[3]+'s')
            plt.plot()
            plt.savefig('figura.png')
            await message.channel.send(file=discord.File('figura.png'))
            
            
        if(message.content.startswith("$monitorizar")):
            if(message.content.startswith("$monitorizar ABS")):
                argumentos = message.content.split(' ')
                mayor = argumentos[2]
                oid = traductor(mibView, argumentos[3])
                umbral = float(argumentos[4])
                intervalo = float(argumentos[5])
                
                await message.channel.send("Se ha configurado un aviso {}".format(argumentos))

                if (mayor == "mayor"):
                    return_value = await monitorizarABSMayor(mibView, oid, umbral, intervalo)
                    await message.channel.send(return_value)
                elif (mayor == "menor"):
                    return_value = await monitorizarABSMenor(mibView, oid, umbral, intervalo)
                    await message.channel.send(return_value)
                else:
                    await message.channel.send("Error con los parametros, use $help para obtener mas ayuda")

            elif (message.content.startswith("$monitorizar DELTA")):
                argumentos = message.content.split(' ')
                mayor = argumentos[2]
                oid = traductor(mibView, argumentos[3])
                umbral = float(argumentos[4])
                intervalo = float(argumentos[5])
                
                await message.channel.send("Se ha configurado un aviso {}".format(argumentos))

                if (mayor == "mayor"):
                    return_value = await monitorizarDeltaMayor(mibView, oid, umbral, intervalo)
                    await message.channel.send(return_value)
                elif (mayor == "menor"):
                    return_value = await monitorizarDeltaMenor(mibView, oid, umbral, intervalo)
                    await message.channel.send(return_value)
                else:
                    await message.channel.send("Error con los parametros, use $help para obtener mas ayuda")
            
            
client.run(TOKEN)
