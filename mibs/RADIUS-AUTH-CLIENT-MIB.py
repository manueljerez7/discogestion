#
# PySNMP MIB module RADIUS-AUTH-CLIENT-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:25:31 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( OctetString, Integer, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
( InetAddressType, InetAddress, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
( MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, mib_2, Bits, Integer32, Unsigned32, ModuleIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "mib-2", "Bits", "Integer32", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Counter32")
( TextualConvention, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
radiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 2)).setRevisions(("2006-08-21 00:00", "1999-06-11 00:00",))
if mibBuilder.loadTexts: radiusAuthClientMIB.setLastUpdated('200608210000Z')
if mibBuilder.loadTexts: radiusAuthClientMIB.setOrganization('IETF RADIUS Extensions Working Group.')
if mibBuilder.loadTexts: radiusAuthClientMIB.setContactInfo(' Bernard Aboba\n                Microsoft\n                One Microsoft Way\n                Redmond, WA  98052\n\n                US\n                Phone: +1 425 936 6605\n                EMail: bernarda@microsoft.com')
if mibBuilder.loadTexts: radiusAuthClientMIB.setDescription('The MIB module for entities implementing the client\n              side of the Remote Authentication Dial-In User Service\n              (RADIUS) authentication protocol.  Copyright (C) The\n              Internet Society (2006).  This version of this MIB\n              module is part of RFC 4668; see the RFC itself for\n              full legal notices.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setDescription('The OID assigned to RADIUS MIB work by the IANA.')
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1))
radiusAuthClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1))
radiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientInvalidServerAddresses.setDescription('The number of RADIUS Access-Response packets\n             received from unknown addresses.')
radiusAuthClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setDescription('The NAS-Identifier of the RADIUS authentication client.\n              This is not necessarily the same as sysName in MIB II.')
radiusAuthServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3), )
if mibBuilder.loadTexts: radiusAuthServerTable.setDescription('The (conceptual) table listing the RADIUS authentication\n             servers with which the client shares a secret.')
radiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
if mibBuilder.loadTexts: radiusAuthServerEntry.setDescription('An entry (conceptual row) representing a RADIUS\n             authentication server with which the client shares\n             a secret.')
radiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: radiusAuthServerIndex.setDescription('A number uniquely identifying each RADIUS\n             Authentication server with which this client\n             communicates.')
radiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerAddress.setDescription('The IP address of the RADIUS authentication server\n             referred to in this table entry.')
radiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setDescription('The UDP port the client is using to send requests to\n             this server.')
radiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientRoundTripTime.setDescription('The time interval (in hundredths of a second) between\n             the most recent Access-Reply/Access-Challenge and the\n             Access-Request that matched it from this RADIUS\n             authentication server.')
radiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setDescription('The number of RADIUS Access-Request packets sent\n             to this server.  This does not include retransmissions.')
radiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setDescription('The number of RADIUS Access-Request packets\n             retransmitted to this RADIUS authentication server.')
radiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setDescription('The number of RADIUS Access-Accept packets\n             (valid or invalid) received from this server.')
radiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setDescription('The number of RADIUS Access-Reject packets\n             (valid or invalid) received from this server.')
radiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setDescription('The number of RADIUS Access-Challenge packets\n             (valid or invalid) received from this server.')
radiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientMalformedAccessResponses.setDescription('The number of malformed RADIUS Access-Response\n             packets received from this server.\n             Malformed packets include packets with\n             an invalid length.  Bad authenticators or\n             Message Authenticator attributes or unknown types\n             are not included as malformed access responses.')
radiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setDescription('The number of RADIUS Access-Response packets\n             containing invalid authenticators or Message\n             Authenticator attributes received from this server.')
radiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setDescription('The number of RADIUS Access-Request packets\n             destined for this server that have not yet timed out\n             or received a response.  This variable is incremented\n\n             when an Access-Request is sent and decremented due to\n             receipt of an Access-Accept, Access-Reject,\n             Access-Challenge, timeout, or retransmission.')
radiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setDescription('The number of authentication timeouts to this server.\n             After a timeout, the client may retry to the same\n             server, send to a different server, or\n             give up.  A retry to the same server is counted as a\n             retransmit as well as a timeout.  A send to a different\n             server is counted as a Request as well as a timeout.')
radiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientUnknownTypes.setDescription('The number of RADIUS packets of unknown type that\n             were received from this server on the authentication\n             port.')
radiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPacketsDropped.setDescription('The number of RADIUS packets that were\n             received from this server on the authentication port\n             and dropped for some other reason.')
radiusAuthServerExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4), )
if mibBuilder.loadTexts: radiusAuthServerExtTable.setDescription('The (conceptual) table listing the RADIUS authentication\n             servers with which the client shares a secret.')
radiusAuthServerExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerExtIndex"))
if mibBuilder.loadTexts: radiusAuthServerExtEntry.setDescription('An entry (conceptual row) representing a RADIUS\n             authentication server with which the client shares\n             a secret.')
radiusAuthServerExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: radiusAuthServerExtIndex.setDescription('A number uniquely identifying each RADIUS\n             Authentication server with which this client\n             communicates.')
radiusAuthServerInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddressType.setDescription('The type of address format used for the\n             radiusAuthServerInetAddress object.')
radiusAuthServerInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddress.setDescription('The IP address of the RADIUS authentication\n             server referred to in this table entry, using\n             the version-neutral IP address format.')
radiusAuthClientServerInetPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerInetPortNumber.setDescription('The UDP port the client is using to send requests\n             to this server.  The value of zero (0) is invalid.')
radiusAuthClientExtRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtRoundTripTime.setDescription('The time interval (in hundredths of a second) between\n             the most recent Access-Reply/Access-Challenge and the\n             Access-Request that matched it from this RADIUS\n             authentication server.')
radiusAuthClientExtAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRequests.setDescription('The number of RADIUS Access-Request packets sent\n             to this server.  This does not include retransmissions.\n             This counter may experience a discontinuity when the\n             RADIUS Client module within the managed entity is\n             reinitialized, as indicated by the current value of\n             radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRetransmissions.setDescription('The number of RADIUS Access-Request packets\n             retransmitted to this RADIUS authentication server.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed entity\n             is reinitialized, as indicated by the current value\n             of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessAccepts.setDescription('The number of RADIUS Access-Accept packets\n             (valid or invalid) received from this server.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed entity\n             is reinitialized, as indicated by the current value\n\n             of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRejects.setDescription('The number of RADIUS Access-Reject packets\n             (valid or invalid) received from this server.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed\n             entity is reinitialized, as indicated by the\n             current value of\n             radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessChallenges.setDescription('The number of RADIUS Access-Challenge packets\n             (valid or invalid) received from this server.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed\n             entity is reinitialized, as indicated by the\n             current value of\n             radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtMalformedAccessResponses.setDescription('The number of malformed RADIUS Access-Response\n             packets received from this server.\n             Malformed packets include packets with\n\n             an invalid length.  Bad authenticators or\n             Message Authenticator attributes or unknown types\n             are not included as malformed access responses.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed entity\n             is reinitialized, as indicated by the current value\n             of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 12), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtBadAuthenticators.setDescription('The number of RADIUS Access-Response packets\n             containing invalid authenticators or Message\n             Authenticator attributes received from this server.\n             This counter may experience a discontinuity when\n             the RADIUS Client module within the managed entity\n             is reinitialized, as indicated by the current value\n             of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 13), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPendingRequests.setDescription('The number of RADIUS Access-Request packets\n             destined for this server that have not yet timed out\n             or received a response.  This variable is incremented\n             when an Access-Request is sent and decremented due to\n             receipt of an Access-Accept, Access-Reject,\n             Access-Challenge, timeout, or retransmission.')
radiusAuthClientExtTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 14), Counter32()).setUnits('timeouts').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtTimeouts.setDescription('The number of authentication timeouts to this server.\n\n             After a timeout, the client may retry to the same\n             server, send to a different server, or\n             give up.  A retry to the same server is counted as a\n             retransmit as well as a timeout.  A send to a different\n             server is counted as a Request as well as a timeout.\n             This counter may experience a discontinuity when the\n             RADIUS Client module within the managed entity is\n             reinitialized, as indicated by the current value of\n             radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 15), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtUnknownTypes.setDescription('The number of RADIUS packets of unknown type that\n             were received from this server on the authentication\n             port.  This counter may experience a discontinuity\n             when the RADIUS Client module within the managed\n             entity is reinitialized, as indicated by the current\n             value of radiusAuthClientCounterDiscontinuity.')
radiusAuthClientExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 16), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPacketsDropped.setDescription('The number of RADIUS packets that were\n             received from this server on the authentication port\n             and dropped for some other reason.  This counter may\n             experience a discontinuity when the RADIUS Client\n             module within the managed entity is reinitialized,\n             as indicated by the current value of\n             radiusAuthClientCounterDiscontinuity.')
radiusAuthClientCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 17), TimeTicks()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientCounterDiscontinuity.setDescription('The number of centiseconds since the last discontinuity\n             in the RADIUS Client counters.  A discontinuity may\n             be the result of a reinitialization of the RADIUS\n             Client module within the managed entity.')
radiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2))
radiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1))
radiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2))
radiusAuthClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)).setObjects(*(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMIBGroup"),))
if mibBuilder.loadTexts: radiusAuthClientMIBCompliance.setDescription('The compliance statement for authentication clients\n            implementing the RADIUS Authentication Client MIB.\n            Implementation of this module is for IPv4-only\n            entities, or for backwards compatibility use with\n            entities that support both IPv4 and IPv6.')
radiusAuthClientExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 2)).setObjects(*(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMIBGroup"),))
if mibBuilder.loadTexts: radiusAuthClientExtMIBCompliance.setDescription('The compliance statement for authentication\n            clients implementing the RADIUS Authentication\n            Client IPv6 Extensions MIB.  Implementation of\n            this module is for entities that support IPv6,\n            or support IPv4 and IPv6.')
radiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)).setObjects(*(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"),))
if mibBuilder.loadTexts: radiusAuthClientMIBGroup.setDescription('The basic collection of objects providing management of\n            RADIUS Authentication Clients.')
radiusAuthClientExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 2)).setObjects(*(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddressType"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerInetPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPacketsDropped"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientCounterDiscontinuity"),))
if mibBuilder.loadTexts: radiusAuthClientExtMIBGroup.setDescription('The collection of extended objects providing\n            management of RADIUS Authentication Clients\n            using version-neutral IP address format.')
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusAuthClientExtMIBCompliance=radiusAuthClientExtMIBCompliance, radiusAuthClientBadAuthenticators=radiusAuthClientBadAuthenticators, radiusAuthClientExtAccessAccepts=radiusAuthClientExtAccessAccepts, radiusAuthClientExtAccessChallenges=radiusAuthClientExtAccessChallenges, radiusAuthClientExtBadAuthenticators=radiusAuthClientExtBadAuthenticators, radiusAuthClientExtAccessRetransmissions=radiusAuthClientExtAccessRetransmissions, radiusAuthClientMIBCompliances=radiusAuthClientMIBCompliances, radiusAuthClientExtPendingRequests=radiusAuthClientExtPendingRequests, radiusAuthServerEntry=radiusAuthServerEntry, radiusAuthClientInvalidServerAddresses=radiusAuthClientInvalidServerAddresses, radiusAuthClientExtAccessRejects=radiusAuthClientExtAccessRejects, radiusAuthClientMIBConformance=radiusAuthClientMIBConformance, radiusAuthServerTable=radiusAuthServerTable, radiusAuthClient=radiusAuthClient, radiusAuthClientAccessRejects=radiusAuthClientAccessRejects, radiusAuthClientAccessRetransmissions=radiusAuthClientAccessRetransmissions, radiusAuthClientExtMalformedAccessResponses=radiusAuthClientExtMalformedAccessResponses, radiusAuthClientIdentifier=radiusAuthClientIdentifier, radiusAuthClientExtPacketsDropped=radiusAuthClientExtPacketsDropped, radiusAuthServerInetAddress=radiusAuthServerInetAddress, radiusAuthServerIndex=radiusAuthServerIndex, radiusAuthClientCounterDiscontinuity=radiusAuthClientCounterDiscontinuity, radiusAuthentication=radiusAuthentication, radiusAuthClientExtRoundTripTime=radiusAuthClientExtRoundTripTime, radiusAuthClientServerPortNumber=radiusAuthClientServerPortNumber, radiusAuthServerExtTable=radiusAuthServerExtTable, radiusAuthClientRoundTripTime=radiusAuthClientRoundTripTime, radiusAuthServerExtEntry=radiusAuthServerExtEntry, radiusAuthClientExtAccessRequests=radiusAuthClientExtAccessRequests, radiusAuthServerExtIndex=radiusAuthServerExtIndex, radiusAuthClientMIBGroups=radiusAuthClientMIBGroups, radiusAuthClientAccessRequests=radiusAuthClientAccessRequests, radiusAuthClientPendingRequests=radiusAuthClientPendingRequests, radiusAuthClientExtUnknownTypes=radiusAuthClientExtUnknownTypes, radiusAuthClientMIB=radiusAuthClientMIB, radiusAuthServerAddress=radiusAuthServerAddress, PYSNMP_MODULE_ID=radiusAuthClientMIB, radiusAuthClientUnknownTypes=radiusAuthClientUnknownTypes, radiusAuthClientAccessAccepts=radiusAuthClientAccessAccepts, radiusAuthClientMalformedAccessResponses=radiusAuthClientMalformedAccessResponses, radiusMIB=radiusMIB, radiusAuthClientServerInetPortNumber=radiusAuthClientServerInetPortNumber, radiusAuthClientPacketsDropped=radiusAuthClientPacketsDropped, radiusAuthClientMIBCompliance=radiusAuthClientMIBCompliance, radiusAuthClientTimeouts=radiusAuthClientTimeouts, radiusAuthClientMIBGroup=radiusAuthClientMIBGroup, radiusAuthClientAccessChallenges=radiusAuthClientAccessChallenges, radiusAuthClientExtTimeouts=radiusAuthClientExtTimeouts, radiusAuthClientExtMIBGroup=radiusAuthClientExtMIBGroup, radiusAuthServerInetAddressType=radiusAuthServerInetAddressType, radiusAuthClientMIBObjects=radiusAuthClientMIBObjects)
