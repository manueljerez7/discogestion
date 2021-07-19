from fpdf import FPDF
from acciones import *
from traductor import traductor

import matplotlib.pyplot as plt
from pysnmp.hlapi import *
from traductor import traductor
import os
from tabulate import tabulate
from CrearFoto import *
import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import math

def getInforme(mibView, ip):
    ##RECOGER PARÁMETROS
    oid = traductor(mibView,'sysName')
    sysName = get(oid, ip)
    sysName = sysName.split('=')[1]
    oid = traductor(mibView,'sysLocation')
    sysLocation = get(oid, ip)
    sysLocation = sysLocation.split('=')[1]
    oid = traductor(mibView,'sysDescr')
    sysDescr = get(oid, ip)
    sysDescr = sysDescr.split('=')[1]
    oid = traductor(mibView,'sysContact')
    sysContact = get(oid, ip)
    sysContact = sysContact.split('=')[1]
    oid = traductor(mibView,'hrSystemNumUsers')
    hrSystemNumUsers = get(oid, ip)
    hrSystemNumUsers = hrSystemNumUsers.split('=')[1]
    oid = traductor(mibView,'ifNumber')
    ifNumber = get(oid, ip)
    ifNumber = ifNumber.split('=')[1]
    oid = traductor(mibView,'hrSystemProcesses')
    hrSystemProcesses = get(oid, ip)
    hrSystemProcesses = hrSystemProcesses.split('=')[1]
    oid = traductor(mibView,'hrMemorySize')
    hrMemorySize = get(oid, ip)
    hrMemorySize = hrMemorySize.split('=')[1]
    oid = traductor(mibView,'tcpActiveOpens')
    tcpActiveOpens = get(oid, ip)
    tcpActiveOpens = tcpActiveOpens.split('=')[1]
    
    ##COMPLETAR PDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    
    pdf.add_page()
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.rect(8.0, 8.0, 194.0,281.0)
    pdf.image('logo.png', x = 160, y = 12, w = 34, h = 20, type = 'PNG', link = '')
    
    ##TÍTULO
    pdf.set_font('Times', 'B', 18)
    pdf.cell(40, 10, 'INFORME\n', 0, 1)
    ##VARIABLES ESCALARES
    pdf.set_font('Courier', '', 12)
    pdf.cell(40, 10, 'Nombre del equipo: '+sysName, 0, 1)
    pdf.cell(40, 10, 'Localización del equipo: '+sysLocation, 0, 1)
    pdf.multi_cell(180, 10, 'Descripción: '+sysDescr, 0, 1)
    pdf.cell(40, 10, 'Persona responsable: '+sysContact, 0, 1)
    pdf.cell(40, 10, 'Número de usuarios del equipo: '+hrSystemNumUsers, 0, 1)
    pdf.cell(40, 10, 'Número de interfaces del equipo: '+ifNumber, 0, 1)
    pdf.cell(40, 10, 'Número de procesos activos en el equipo: '+hrSystemProcesses, 0, 1)
    pdf.cell(40, 10, 'Tamaño de la memoria: '+hrMemorySize+'kBytes', 0, 1)
    pdf.cell(40, 10, 'Conexiones activas tcp: '+tcpActiveOpens, 0, 1)
    
    
    ##RECOGER E IMPRIMIR TABLAS
    #1º
    oid = traductor(mibView, 'hrStorageTable')
    hrStorageTable = getTabla(mibView,oid, ip)
    hrStorageTable = tabulate(hrStorageTable)
    createTable(hrStorageTable)
    hrStorageTable = text_image('tabla.txt')
    hrStorageTable.save('hrStorageTable.png')
    pdf.add_page()
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.set_font('Courier', '', 12)
    pdf.cell(40, 10, 'hrStorageTable', 0, 1)
    pdf.image('hrStorageTable.png', x = 6, y = 20, w = 198, h = 30, type = 'PNG', link = '')
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    #2º (misma pág)
    oid = traductor(mibView, 'hrDeviceTable')
    hrDeviceTable = getTabla(mibView,oid, ip)
    hrDeviceTable = tabulate(hrDeviceTable)
    createTable(hrDeviceTable)
    hrDeviceTable = text_image('tabla.txt')
    hrDeviceTable.save('hrDeviceTable.png')
    pdf.set_font('Courier', '', 12)
    pdf.cell(40, 10, 'hrDeviceTable', 0, 1)
    pdf.image('hrDeviceTable.png', x = 6, y = 70, w = 198, h = 220, type = 'PNG', link = '')
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    pdf.cell(40, 10, ' ', 0, 1)
    
    ##RECOGER E IMPRIMIR SONDEOS (otra pág)
    #1º
    oid = traductor(mibView, 'ipInDiscards')
    tiempo = 20
    numero = 10
    vector = sondeoDelta(oid,tiempo,numero, ip)
    plt.figure()
    plt.plot(np.arange(numero),vector)
    plt.grid()
    plt.title('Sondeo del valor incremental de ipInDiscards durante '+str(tiempo)+'s')
    plt.plot()
    plt.savefig('ipInDiscards.png')
    pdf.add_page()
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.image('ipInDiscards.png', x = 60, y = 10, w = 90, h = 90, type = 'PNG', link = '')
    #2º
    tiempo = 20
    numero = 10
    vector = sondeoDelta((1,3,6,1,2,1,6,10),tiempo,numero, ip)
    plt.figure()
    plt.plot(np.arange(numero),vector)
    plt.grid()
    plt.title('Sondeo del valor incremental de tcpInSegs durante '+str(tiempo)+'s')
    plt.plot()
    plt.savefig('tcpInSegs.png')
    pdf.image('tcpInSegs.png', x = 60, y = 100, w = 90, h = 90, type = 'PNG', link = '')
    #3º
    oid = traductor(mibView, 'udpInDatagrams')
    tiempo = 20
    numero = 10
    vector = sondeoDelta(oid,tiempo,numero, ip)
    plt.figure()
    plt.plot(np.arange(numero),vector)
    plt.grid()
    plt.title('Sondeo del valor incremental de udpInDatagrams durante '+str(tiempo)+'s')
    plt.plot()
    plt.savefig('udpInDatagrams.png')
    pdf.image('udpInDatagrams.png', x = 60, y = 190, w = 90, h = 90, type = 'PNG', link = '')
    
    ##GRÁFICO COMPARATIVA E IMPRIMIR (otra pág)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Paquetes tcp', 'Paquetes udp'
    
    tcpInSegs = get((1,3,6,1,2,1,6,10), ip)
    tcpInSegs = tcpInSegs.split('=')[1]
    udpInDatagrams = get((1,3,6,1,2,1,7,4), ip)
    udpInDatagrams = udpInDatagrams.split('=')[1]
    
    sizes = [tcpInSegs, udpInDatagrams]
    
    if tcpInSegs > udpInDatagrams:
        explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    else:
        explode = (0, 0.1)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.title('Comparación de paquetes tcp y udp recibidos')
    plt.plot()
    plt.savefig('pieChart.png')
    
    pdf.add_page()
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.image('pieChart.png', x = 25, y = 10, w = 160, h = 115, type = 'PNG', link = '')
    
    ##GENERAR PDF
    pdf.output('Informe.pdf', 'F')