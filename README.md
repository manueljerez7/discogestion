DISCOGESTION
Discord API that allows the user to execute SNMP commands and manage network nodes with Discord interface
Video of a demonstration of the project (in spanish): https://www.youtube.com/watch?v=nCViH_UeI2s
Made by:
enrsancar1		https://github.com/enrsancar1
manueljerez7 	https://github.com/manueljerez7
marreyhen		https://github.com/marreyhen
As final project in the course "Gestion de Redes" (Network Management), Ingenieria de las Tecnologías de las Telecomunicaciones, University of Seville

AVAILABLE COMMANDS:
	$help: shows help
	$add [NAME] [IP]: Adds a new device, with its IP and an ID. By default, it is created the device {'local':'localhost'}
	$snmp get [OID] [DEVICE_NAME]: Execute a SNMP-GET command 
	$snmp set [OID] [DEVICE_NAME] [VALUE]: Execute a SNMP-SET command 
	$snmp walk [OID] [DEVICE_NAME]: Returns all values of a table as a list
	$snmp tabla [OID] [DEVICE_NAME]: Returns a table as a .txt file
	$sondeo [MODE(ABS o DELTA)] [OID] [TIME_SECONDS] [N_SAMPLES] [DEVICE_NAME]: Returns a graphic with the evolution of the specified value
	$snmp informe [DEVICE_NAME]: Returns a PDF document with some relevant information about the device
	$monitorizar [MODE(ABS o DELTA)] [mayor(higher)/menor(lower)] [OID] [THRESHOLD] [TIME_SECONDS]: Monitors the value of the specified OID and returns an alert
	NOTE: It is not necessary to add .0 when writing the OID

REQUIREMENTS:
Have the SNMP Agent active on the managed device and set the "Community" as "public"

PYTHON LIBRARIES REQUIRED:
	pysnmp
	config
	os
	time
	asyncio
	threading
	fpdf
	matplotlib
	tabulate
	PIL
	math
	base64
	datetime

NOTES ABOUT THE PROJECT:
We are aware that the code written is not nice, we are not proffessional programmers and we had a lot of problems during the development of the project
The generation of the PDF can take some time as it has some graphics and photos that need to be proccessed
The monitoring function stops when generates an alert, the command has to be re-sent if tou want to continue with the comparation
Some tables doesn't display properly if they don't have an integer index column
MIBS available are in the folder "mibs", and they can be added to the project changing the parametrs of loadModules function in index.py, but we do not guarantee that they will
	work, as we only tried some of them.
	
Explanation of the files:
index.py: Main file
acciones.py, trap.py, informe.py: Functions of the different commands available
CrearFoto.py: Auxiliar function that converts .txt files to photos to add them to the PDF
traductor.py: Auxiliar function that converts OID names to values




