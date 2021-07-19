from pysnmp.smi import builder, view, compiler, error



def traductor(mibView, label):
    
    oid, test, suffix = mibView.getNodeName((label,))

    return oid

def traductorInverso(mibView, oid):
    
    modName, symName, suffix = mibView.getNodeLocation(oid)
    
    print(modName, symName, suffix)
