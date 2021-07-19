#
# PySNMP MIB module MPLS-FTN-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/MPLS-FTN-STD-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:20:35 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, OctetString, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
( Dscp, ) = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
( InterfaceIndexOrZero, ifGeneralInformationGroup, ifCounterDiscontinuityGroup, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifGeneralInformationGroup", "ifCounterDiscontinuityGroup")
( InetAddressType, InetPortNumber, InetAddress, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ObjectGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
( iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Integer32, Counter32, Counter64, ObjectIdentity, MibIdentifier, TimeTicks, NotificationType, Gauge32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "Gauge32")
( RowPointer, TextualConvention, StorageType, RowStatus, DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TextualConvention", "StorageType", "RowStatus", "DisplayString", "TimeStamp")
mplsFTNStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 8)).setRevisions(("2004-06-03 00:00",))
if mibBuilder.loadTexts: mplsFTNStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsFTNStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsFTNStdMIB.setContactInfo('\n                     Thomas D. Nadeau\n             Postal: Cisco Systems, Inc.\n                     250 Apollo Drive\n                     Chelmsford, MA 01824\n             Tel:    +1-978-244-3051\n             Email:  tnadeau@cisco.com\n    \n                     Cheenu Srinivasan\n             Postal: Bloomberg L.P.\n                     499 Park Avenue\n                     New York, NY 10022\n             Tel:    +1-212-893-3682\n             Email:  cheenu@bloomberg.net\n    \n                     Arun Viswanathan\n             Postal: Force10 Networks, Inc.\n                     1440 McCarthy Blvd\n                     Milpitas, CA 95035\n             Tel:    +1-408-571-3516\n             Email:  arunv@force10networks.com\n    \n             IETF MPLS Working Group email: mpls@uu.net')
if mibBuilder.loadTexts: mplsFTNStdMIB.setDescription('Copyright (C) The Internet Society (2004). The\n             initial version of this MIB module was published\n             in RFC 3814. For full legal notices see the RFC\n             itself or see:\n             http://www.ietf.org/copyrights/ianamib.html\n    \n             This MIB module contains managed object definitions for\n             specifying FEC to NHLFE (FTN) mappings and corresponding\n             performance for MPLS.')
class MplsFTNEntryIndex(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class MplsFTNEntryIndexOrZero(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

mplsFTNNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 0))
mplsFTNObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 1))
mplsFTNConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2))
mplsFTNIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 1), MplsFTNEntryIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNIndexNext.setDescription('This object contains the next available valid value to\n             be used for mplsFTNIndex when creating entries in the\n             mplsFTNTable.\n    \n             When creating a new conceptual row (configuration\n             entry) in mplsFTNTable with an SNMP SET operation the\n             command generator (Network Management Application) must\n             first issue a management protocol retrieval operation\n             to obtain the current value of this object.\n    \n             If the command responder (agent) does not wish to allow\n             creation of more entries in mplsFTNTable, possibly\n             because of resource exhaustion, this object MUST return\n             a value of 0.\n    \n             If a non-zero value is returned the Network Management\n    \n             Application must determine whether the value is indeed\n             still unused since two Network Management Applications\n             may attempt to create a row simultaneously and use the\n             same value.\n    \n             If it is currently unused and the SET succeeds, the\n             agent MUST change the value of this object to a\n             currently unused non-zero value (according to an\n             implementation specific algorithm) or zero (if no\n             further row creation will be permitted).\n    \n             If the value is in use, however, the SET fails and the\n             Network Management Application must then reread this\n             object to obtain a new usable value.')
mplsFTNTableLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNTableLastChanged.setDescription('Indicates the last time an entry was added, deleted or\n             modified in mplsFTNTable.  Management stations should\n             consult this object to determine if mplsFTNTable\n             requires their attention.  This object is particularly\n             useful for applications performing a retrieval on\n             mplsFTNTable to ensure that the table is not modified\n             during the retrieval operation.')
mplsFTNTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3), )
if mibBuilder.loadTexts: mplsFTNTable.setDescription('This table contains the currently defined FTN entries.\n             This table allows FEC to NHLFE mappings to be\n             specified.  Each entry in this table defines a rule to\n             be applied to incoming packets (on interfaces that the\n             FTN entry is activated on using mplsFTNMapTable) and an\n             action to be taken on matching packets\n             (mplsFTNActionPointer).\n    \n             This table supports 6-tuple matching rules based on one\n             or more of source address range, destination address\n             range, source port range, destination port range, IPv4\n    \n             Protocol field or IPv6 next-header field and the\n             DiffServ Code Point (DSCP) to be specified.\n    \n             The action pointer points either to instance of\n             mplsXCEntry in MPLS-LSR-STD-MIB when the NHLFE is a non-\n             TE LSP, or to an instance of mplsTunnelEntry in the\n             MPLS-TE-STD-MIB when the NHLFE is an originating TE\n             tunnel.')
mplsFTNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1), ).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNIndex"))
if mibBuilder.loadTexts: mplsFTNEntry.setDescription('Each entry represents one FTN entry which defines a\n             rule to compare incoming packets with and an action to\n             be taken on matching packets.')
mplsFTNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 1), MplsFTNEntryIndex())
if mibBuilder.loadTexts: mplsFTNIndex.setDescription('This is the unique index for a conceptual row in\n             mplsFTNTable.\n    \n             To create a new conceptual row in mplsFTNTable a\n             Network Management Application SHOULD retrieve the\n             current value of mplsFTNIndexNext to determine the next\n             valid available value of mplsFTNIndex.')
mplsFTNRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNRowStatus.setDescription("Used for controlling the creation and deletion of this\n             row. All writeable objects in this row may be modified\n             at any time. If a Network Management Application\n             attempts to delete a conceptual row by setting this\n             object to 'destroy' and there are one or more entries\n             in mplsFTNMapTable pointing to the row (i.e., when\n             mplsFTNIndex of the conceptual row being deleted is\n             equal to mplsFTNMapCurrIndex for one or more entries in\n             mplsFTNMapTable), the agent MUST also destroy the\n             corresponding entries in mplsFTNMapTable.")
mplsFTNDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDescr.setDescription('The description of this FTN entry. Since the index for\n             this table has no particular significance or meaning,\n             this object should contain some meaningful text that an\n             operator could use to further distinguish entries in\n             this table.')
mplsFTNMask = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 4), Bits().clone(namedValues=NamedValues(("sourceAddr", 0), ("destAddr", 1), ("sourcePort", 2), ("destPort", 3), ("protocol", 4), ("dscp", 5),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNMask.setDescription('This bit map indicates which of the fields described\n             next, namely source address range, destination address\n             range, source port range, destination port range, IPv4\n             Protocol field or IPv6 next-header field and\n             Differentiated Services Code Point (DSCP) is active for\n             this FTN entry. If a particular bit is set to zero then\n             the corresponding field in the packet MUST be ignored\n             for comparison purposes.')
mplsFTNAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNAddrType.setDescription('This object determines the type of address contained in\n             the source and destination address objects\n             (mplsFTNSourceAddrMin, mplsFTNSourceAddrMax,\n             mplsFTNDestAddrMin and mplsFTNDestAddrMax) of a\n             conceptual row.\n    \n             This object MUST NOT be set to unknown(0) when\n             mplsFTNMask has bit positions sourceAddr(0) or\n             destAddr(1) set to one.\n    \n             When both these bit positions of mplsFTNMask are set to\n             zero the value of mplsFTNAddrType SHOULD be set to\n             unknown(0) and the corresponding source and destination\n             address objects SHOULD be set to zero-length strings.')
mplsFTNSourceAddrMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNSourceAddrMin.setDescription('The lower end of the source address range. The type of\n             this object is determined by the corresponding\n             mplsFTNAddrType object.')
mplsFTNSourceAddrMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNSourceAddrMax.setDescription('The upper end of the source address range. The type of\n             this object is determined by the corresponding\n             mplsFTNAddrType object.')
mplsFTNDestAddrMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 8), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDestAddrMin.setDescription('The lower end of the destination address range. The\n             type of this object is determined by the corresponding\n             mplsFTNAddrType object.')
mplsFTNDestAddrMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 9), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDestAddrMax.setDescription('The higher end of the destination address range. The\n             type of this object is determined by the corresponding\n             mplsFTNAddrType object.')
mplsFTNSourcePortMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 10), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNSourcePortMin.setDescription('The lower end of the source port range.')
mplsFTNSourcePortMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 11), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNSourcePortMax.setDescription('The higher end of the source port range ')
mplsFTNDestPortMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 12), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDestPortMin.setDescription('The lower end of the destination port range.')
mplsFTNDestPortMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 13), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDestPortMax.setDescription('The higher end of the destination port range.')
mplsFTNProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNProtocol.setDescription('The IP protocol to match against the IPv4 protocol\n             number or IPv6 Next-Header number in the packet. A\n             value of 255 means match all.  Note that the protocol\n             number of 255 is reserved by IANA, and Next-Header\n             number of 0 is used in IPv6.')
mplsFTNDscp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 15), Dscp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNDscp.setDescription('The contents of the DSCP field.')
mplsFTNActionType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("redirectLsp", 1), ("redirectTunnel", 2),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNActionType.setDescription('The type of action to be taken on packets matching this\n             FTN entry.')
mplsFTNActionPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 17), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNActionPointer.setDescription('If mplsFTNActionType is redirectLsp(1), then this\n             object MUST contain zeroDotZero or point to a instance\n             of mplsXCEntry indicating the LSP to redirect matching\n             packets to.\n    \n             If mplsFTNActionType is redirectTunnel(2), then this\n             object MUST contain zeroDotZero or point to a instance\n             of mplsTunnelEntry indicating the MPLS TE tunnel to\n             redirect matching packets to.\n    \n             If this object points to a conceptual row instance in a\n             table consistent with mplsFTNActionType but this\n             instance does not currently exist then no action will\n             be taken on packets matching such an FTN entry till\n             this instance comes into existence.\n    \n             If this object contains zeroDotZero then no action will\n             be taken on packets matching such an FTN entry till it\n             is populated with a valid pointer consistent with the\n             value of mplsFTNActionType as explained above.')
mplsFTNStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 18), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNStorageType.setDescription("The storage type for this FTN entry. Conceptual rows\n             having the value 'permanent' need not allow write-\n             access to any columnar objects in the row.")
mplsFTNMapTableLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNMapTableLastChanged.setDescription('Indicates the last time an entry was added, deleted or\n             modified in mplsFTNMapTable. Management stations should\n             consult this object to determine if the table requires\n             their attention.  This object is particularly useful\n             for applications performing a retrieval on\n             mplsFTNMapTable to ensure that the table is not\n             modified during the retrieval operation.')
mplsFTNMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5), )
if mibBuilder.loadTexts: mplsFTNMapTable.setDescription("This table contains objects which provide the\n             capability to apply or map FTN rules as defined by\n             entries in mplsFTNTable to specific interfaces in the\n             system.  FTN rules are compared with incoming packets\n             in the order in which they are applied on an interface.\n    \n             The indexing structure of mplsFTNMapTable is as\n             follows.\n    \n             - mplsFTNMapIndex indicates the interface to which the\n                rule is being applied.  A value of 0 represents the\n                application of the rule to all interfaces.\n    \n             - mplsFTNMapPrevIndex specifies the rule on the\n                interface prior to the one being applied.  A value of\n                0 specifies that the rule is being inserted at the\n                head of the list of rules currently applied to the\n                interface.\n    \n             - mplsFTNMapCurrIndex is the index in mplsFTNTable\n                corresponding to the rule being applied.\n    \n             This indexing structure makes the entries in the table\n             behave like items in a linked-list.  The object\n             mplsFTNMapPrevIndex in each conceptual row is a pointer\n             to the previous entry that is applied to a particular\n             interface.  This allows a new entry to be 'inserted' at\n             an arbitrary position in a list of entries currently\n             applied to an interface.  This object is self-\n             adjusting, i.e., its value is automatically adjusted by\n             the agent, if necessary, after an insertion or deletion\n             operation.\n    \n             Using this linked-list structure, one can retrieve FTN\n             entries in the order of application on a per-interface\n             basis as follows:\n    \n             - To determine the first FTN entry on an interface\n                with index ifIndex perform a GETNEXT retrieval\n                operation on mplsFTNMapRowStatus.ifIndex.0.0; the\n                returned object, if one exists, is (say)\n                mplsFTNMapRowStatus.ifIndex.0.n (mplsFTNMapRowStatus\n                is the first accessible columnar object in the\n                conceptual row). Then the index of the first FTN\n                entry applied on this interface is n.\n    \n             - To determine the FTN entry applied to an interface\n                after the one indexed by n perform a GETNEXT\n                retrieval operation on\n                mplsFTNMapRowStatus.ifIndex.n.0.  If such an entry\n                exists the returned object would be of the form\n                mplsFTNMapRowStatus.ifIndex.n.m.  Then the index of\n                the next FTN entry applied on this interface is m.\n    \n             - If the FTN entry indexed by n is the last entry\n                applied to the interface with index ifIndex then the\n                object returned would either be:\n    \n                1.mplsFTNMapRowStatus.ifIndexNext.0.k, where\n                   ifIndexNext is the index of the next interface in\n                   ifTable to which an FTN entry has been applied, in\n                   which case k is the index of the first FTN entry\n                   applied to the interface with index ifIndexNext;\n    \n                or:\n    \n                2.mplsFTNMapStorageType.firstIfIndex.0.p, if there\n                   are no more entries in mplsFTNMapTable, where\n                   firstIfIndex is the first entry in ifTable to\n                   which an FTN entry has been mapped.\n    \n             Use the above steps to retrieve all the applied FTN\n             entries on a per-interface basis in application order.\n             Note that the number of retrieval operations is the\n             same as the number of applied FTN entries (i.e., the\n             minimum number of GETNEXT operations needed using any\n             indexing scheme).\n    \n             Agents MUST NOT allow the same FTN entry as specified\n             by mplsFTNMapCurrIndex to be applied multiple times to\n             the same interface.\n    \n             Agents MUST NOT allow the creation of rows in this\n             table until the corresponding rows are created in the\n             mplsFTNTable.\n    \n             If a row in mplsFTNTable is destroyed, the agent MUST\n             destroy the corresponding entries (i.e., ones with a\n             matching value of mplsFTNCurrIndex) in this table as\n             well.")
mplsFTNMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1), ).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNMapIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNMapPrevIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNMapCurrIndex"))
if mibBuilder.loadTexts: mplsFTNMapEntry.setDescription('Each conceptual row represents the application of an\n             FTN rule at a specific position in the list of FTN\n             rules applied on an interface. ')
mplsFTNMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: mplsFTNMapIndex.setDescription('The interface index that this FTN entry is being\n             applied to. A value of zero indicates an entry that is\n             applied all interfaces.\n    \n             Entries mapped to an interface by specifying its (non-\n             zero) interface index in mplsFTNMapIndex are applied\n             ahead of entries with mplsFTNMapIndex equal to zero.')
mplsFTNMapPrevIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 2), MplsFTNEntryIndexOrZero())
if mibBuilder.loadTexts: mplsFTNMapPrevIndex.setDescription('The index of the previous FTN entry that was applied to\n             this interface. The special value zero indicates that\n             this should be the first FTN entry in the list.')
mplsFTNMapCurrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 3), MplsFTNEntryIndex())
if mibBuilder.loadTexts: mplsFTNMapCurrIndex.setDescription('Index of the current FTN entry that is being applied to\n             this interface.')
mplsFTNMapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 4), RowStatus().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6,))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNMapRowStatus.setDescription('Used for controlling the creation and deletion of this\n             row.\n    \n             All writable objects in this row may be modified at any\n             time.\n    \n             If a conceptual row in mplsFTNMapTable points to a\n             conceptual row in mplsFTNTable which is subsequently\n             deleted, the corresponding conceptual row in\n             mplsFTNMapTable MUST also be deleted by the agent.')
mplsFTNMapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsFTNMapStorageType.setDescription("The storage type for this entry.  Conceptual rows\n             having the value 'permanent' need not allow write-\n             access to any columnar objects in this row.")
mplsFTNPerfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6), )
if mibBuilder.loadTexts: mplsFTNPerfTable.setDescription('This table contains performance statistics on FTN\n             entries on a per-interface basis.')
mplsFTNPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1), ).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNPerfIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNPerfCurrIndex"))
if mibBuilder.loadTexts: mplsFTNPerfEntry.setDescription('Each entry contains performance information for the\n             specified interface and an FTN entry mapped to this\n             interface.')
mplsFTNPerfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: mplsFTNPerfIndex.setDescription('The interface index of an interface that an FTN entry\n             has been applied/mapped to.  Each instance of this\n             object corresponds to an instance of mplsFTNMapIndex.')
mplsFTNPerfCurrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 2), MplsFTNEntryIndex())
if mibBuilder.loadTexts: mplsFTNPerfCurrIndex.setDescription('Index of an FTN entry that has been applied/mapped to\n             the specified interface.  Each instance of this object\n             corresponds to an instance of mplsFTNMapCurrIndex.')
mplsFTNPerfMatchedPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNPerfMatchedPackets.setDescription('Number of packets that matched the specified FTN entry\n             if it is applied/mapped to the specified interface.\n             Discontinuities in the value of this counter can occur\n             at re-initialization of the management system, and at\n             other times as indicated by the value of\n             mplsFTNDiscontinuityTime.')
mplsFTNPerfMatchedOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNPerfMatchedOctets.setDescription('Number of octets that matched the specified FTN entry\n             if it is applied/mapped to the specified interface.\n             Discontinuities in the value of this counter can occur\n             at re-initialization of the management system, and at\n             other times as indicated by the value of\n             mplsFTNDiscontinuityTime.')
mplsFTNPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsFTNPerfDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at\n             which any one or more of this entry's counters suffered\n             a discontinuity.  If no such discontinuities have\n             occurred since the last re-initialization of the local\n             management subsystem, then this object contains a zero\n             value.")
mplsFTNGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1))
mplsFTNCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2))
mplsFTNModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2, 1)).setObjects(*(("IF-MIB", "ifGeneralInformationGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNRuleGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNMapGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfGroup"),))
if mibBuilder.loadTexts: mplsFTNModuleFullCompliance.setDescription('Compliance statement for agents that provide full\n             support for MPLS-FTN-STD-MIB.')
mplsFTNModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2, 2)).setObjects(*(("IF-MIB", "ifGeneralInformationGroup"), ("IF-MIB", "ifCounterDiscontinuityGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNRuleGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNMapGroup"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfGroup"),))
if mibBuilder.loadTexts: mplsFTNModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only\n             provide read-only support for MPLS-FTN-STD-MIB. Such\n             devices can then be monitored but cannot be configured\n             using this MIB module.')
mplsFTNRuleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 1)).setObjects(*(("MPLS-FTN-STD-MIB", "mplsFTNIndexNext"), ("MPLS-FTN-STD-MIB", "mplsFTNTableLastChanged"), ("MPLS-FTN-STD-MIB", "mplsFTNRowStatus"), ("MPLS-FTN-STD-MIB", "mplsFTNDescr"), ("MPLS-FTN-STD-MIB", "mplsFTNMask"), ("MPLS-FTN-STD-MIB", "mplsFTNAddrType"), ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMin"), ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMax"), ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMin"), ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMax"), ("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMin"), ("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMax"), ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMin"), ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMax"), ("MPLS-FTN-STD-MIB", "mplsFTNProtocol"), ("MPLS-FTN-STD-MIB", "mplsFTNActionType"), ("MPLS-FTN-STD-MIB", "mplsFTNActionPointer"), ("MPLS-FTN-STD-MIB", "mplsFTNDscp"), ("MPLS-FTN-STD-MIB", "mplsFTNStorageType"),))
if mibBuilder.loadTexts: mplsFTNRuleGroup.setDescription('Collection of objects that implement MPLS FTN rules.')
mplsFTNMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 2)).setObjects(*(("MPLS-FTN-STD-MIB", "mplsFTNMapTableLastChanged"), ("MPLS-FTN-STD-MIB", "mplsFTNMapRowStatus"), ("MPLS-FTN-STD-MIB", "mplsFTNMapStorageType"),))
if mibBuilder.loadTexts: mplsFTNMapGroup.setDescription('Collection of objects that implement activation of MPLS\n             FTN entries on interfaces.')
mplsFTNPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 3)).setObjects(*(("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedPackets"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedOctets"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfDiscontinuityTime"),))
if mibBuilder.loadTexts: mplsFTNPerfGroup.setDescription('Collection of objects providing MPLS FTN performance\n             information.')
mibBuilder.exportSymbols("MPLS-FTN-STD-MIB", mplsFTNProtocol=mplsFTNProtocol, mplsFTNModuleReadOnlyCompliance=mplsFTNModuleReadOnlyCompliance, mplsFTNObjects=mplsFTNObjects, mplsFTNPerfMatchedPackets=mplsFTNPerfMatchedPackets, mplsFTNDescr=mplsFTNDescr, mplsFTNMapGroup=mplsFTNMapGroup, mplsFTNSourcePortMin=mplsFTNSourcePortMin, mplsFTNStdMIB=mplsFTNStdMIB, mplsFTNEntry=mplsFTNEntry, mplsFTNStorageType=mplsFTNStorageType, mplsFTNMask=mplsFTNMask, mplsFTNSourceAddrMin=mplsFTNSourceAddrMin, mplsFTNDestAddrMin=mplsFTNDestAddrMin, mplsFTNNotifications=mplsFTNNotifications, MplsFTNEntryIndexOrZero=MplsFTNEntryIndexOrZero, MplsFTNEntryIndex=MplsFTNEntryIndex, mplsFTNSourceAddrMax=mplsFTNSourceAddrMax, mplsFTNPerfTable=mplsFTNPerfTable, mplsFTNMapPrevIndex=mplsFTNMapPrevIndex, mplsFTNMapRowStatus=mplsFTNMapRowStatus, mplsFTNRuleGroup=mplsFTNRuleGroup, mplsFTNGroups=mplsFTNGroups, mplsFTNMapIndex=mplsFTNMapIndex, mplsFTNPerfMatchedOctets=mplsFTNPerfMatchedOctets, mplsFTNDestPortMax=mplsFTNDestPortMax, mplsFTNAddrType=mplsFTNAddrType, mplsFTNDestPortMin=mplsFTNDestPortMin, mplsFTNPerfIndex=mplsFTNPerfIndex, mplsFTNIndex=mplsFTNIndex, mplsFTNDscp=mplsFTNDscp, mplsFTNTableLastChanged=mplsFTNTableLastChanged, mplsFTNActionPointer=mplsFTNActionPointer, mplsFTNIndexNext=mplsFTNIndexNext, mplsFTNPerfCurrIndex=mplsFTNPerfCurrIndex, mplsFTNMapEntry=mplsFTNMapEntry, mplsFTNPerfEntry=mplsFTNPerfEntry, PYSNMP_MODULE_ID=mplsFTNStdMIB, mplsFTNMapStorageType=mplsFTNMapStorageType, mplsFTNCompliances=mplsFTNCompliances, mplsFTNRowStatus=mplsFTNRowStatus, mplsFTNPerfGroup=mplsFTNPerfGroup, mplsFTNDestAddrMax=mplsFTNDestAddrMax, mplsFTNPerfDiscontinuityTime=mplsFTNPerfDiscontinuityTime, mplsFTNMapCurrIndex=mplsFTNMapCurrIndex, mplsFTNConformance=mplsFTNConformance, mplsFTNTable=mplsFTNTable, mplsFTNActionType=mplsFTNActionType, mplsFTNModuleFullCompliance=mplsFTNModuleFullCompliance, mplsFTNSourcePortMax=mplsFTNSourcePortMax, mplsFTNMapTableLastChanged=mplsFTNMapTableLastChanged, mplsFTNMapTable=mplsFTNMapTable)
