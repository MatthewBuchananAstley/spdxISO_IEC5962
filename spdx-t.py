#!/usr/bin/python3 
#
# SPDX-License-Identifier: GPL-3.0-or-later
# PackageVersion: 1.0
# FileCopyrightText: 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl)

import os,sys
from time import gmtime, strftime 
import subprocess
import glob

def prt():
    date = strftime("%Y-%m-%dT%H:%M:%SZ")
    return date 

def print_mijndate(): 
    date = strftime("%Y%m%d.%H%M%S")
    return date

try:
    dte = sys.argv[4] 
    #DocumentName = sys.argv[1] + "-" + print_mijndate() + ".spdx"
    DocumentName = os.path.basename(sys.argv[1]) + "-" + print_mijndate() + ".spdx"
except IndexError:
    #DocumentName = sys.argv[1] + ".spdx"
    DocumentName = os.path.basename(sys.argv[1]) + ".spdx"

DocumentNamespace = sys.argv[2]
prt = prt() 
CreatorComment = sys.argv[3]

PackageDir = os.path.dirname(sys.argv[1])
#print("Ja",PackageDir)
#sys.exit() 
PackageLoc = sys.argv[1]
PackageName = os.path.basename(sys.argv[1])

d = DocumentNamespace.split("/")
PackageSPDXID = "SPDXRef-" + d[3] + "-" "Package" + "-" + PackageName.replace("_","-")   

def checkchlog(self):
    #a = open(PackageName + "/CHANGELOG", "r") 
    #a = open(self + "/CHANGELOG", "r") 
    try:
        a = open(self[0] + "/CHANGELOG", "r") 
    except FileNotFoundError:
        a = open(self[0] + "/CHANGELOG", "w")
        t1 = ""
        t1 += "#" + PackageName + " changelog " + "($id$); -*-text-*-\n"
        t1 += "\n" + PackageName + " 1.0 " + strftime("[ %Y-%m-%d ]")
        a.write(t1)
        a.close()
        a = open(self[0] + "/CHANGELOG", "r") 

    for i in a:
        a1 = i.split()
        if a1 != []:
            if a1[0] == self[1]:
                a2 = a1[1]

    return(a2)        

def chklicense(self):
    #print("JAA", self) 
    try:
        #a = open( self + "/" + self[0], "r") 
        #a = open( PackageLoc + "/" + PackageName, "r") 
        a = open( PackageLoc + "/" + self[0], "r") 
    except FileNotFoundError:
        #return("N: " + PackageName)
        return("NOASSERTION")

    for i in a:
        a1 = i.split(" ",2)
        #print("JA",a1)
        if a1 != []: 
            if len(a1) == 3:
                #if a1[1] == "SPDX-License-Identifier:":
                if a1[1] == self[1]:
                    a2 = a1[2].replace('\n','')
                    return(a2)
                #    a2 = "GPL-3.0-or-later" 
    #return("N: " + self[0]) 
    #return(getFirstCopyrightText(self)) 
    return("NOASSERTION") 

def getFirstCopyrightText(self):

    a = glob.glob(PackageLoc + "/*")

    a4 = {} 

    for i in a:
        a1 = open(i, "r") 
        a5 = int()

        try:
            for ii in a1:
                a2 = ii.split(" ", 2) 
                if a2 != []:
                    if len(a2) == 3:
                        if a2[1] == "FileCopyrightText:":
                            #print("Ja",i, a2[2]) 
                            #a3 = a2[2].replace('\n'.'')
                           
                            a3 = a2[2].replace('\n','')
                            a4[a3] = 1             
        except UnicodeDecodeError:
            next 
    #print("Ja",a4)

    a5 = [] 
    for i in a4.keys():
        #print("JA",i)
        iii = i.split("-")
        ii = iii[0].strip()
        a5.append(ii)

    a5.sort()
    #print("Ja",a5)          

    for i in a4.keys():
        if a5[0] in i:
            #print("Ja",i)
            return(i)




def ch_PackageLicenseInfoFromFiles():
    #a = glob.glob(PackageName + "/*")
    a = glob.glob(PackageLoc + "/*")
    a1 = [ ".deb", "README.md", "CHANGELOG" ]
    a3 = {} 
    #a3 = []
    for i in a:
        iii = i.split("/")
        #print("jAA", iii)
        #if iii[-1].find(".deb") != -1:
        if iii[-1].find(".deb") != -1:
            #print("JAa",iii[-1]) 
            next
        else:
            a3[iii[-1]] = 1

    #print("jA",a3)
    a4 = {} 

    for i in a3:
        #print("JaAA",i)
        #iii = i.split("/")
        #print("Ja",iii[1]) 
        #a4 = chklicense(iii[1]) 
        #print("Ja",a4)
        #a3[chklicense(iii[1])] = 1
        #a3.append(chklicense(iii[1])) 
        #a4[chklicense(i)] = 1 
        a4[chklicense([i, "SPDX-License-Identifier:"])] = 1 
    #print("Ja",a3)
    #print("JaaA", a4) 
    a5 = [] 
    for i in a4.keys():
        a5.append(i)

    return(a5)

def spdxdoc(self):

    a = { "SPDXVersion" : "SPDX-2.2", 
          "DataLicense" : "CC0-1.0",
          "SPDXID" : "SPDXRef-DOCUMENT",
          "DocumentName" : self[0],
          "DocumentNamespace" : self[1],
          "Creator: Person" : "Matthew Buchanan Astley (matthewbuchanan@astley.nl)",
          "Created" : self[2],
          "CreatorComment" : self[3] }

    #print("Ja", a)
    for i in a.keys():
        print(i +":"+ " " + a[i] ) 

    print("\n#\n#\n")


PLicenseConcluded = ch_PackageLicenseInfoFromFiles()
PkgLicenseConcluded = []

for i in PLicenseConcluded:
    ii = i.split()
    if len(ii) != 2:
        PkgLicenseConcluded.append(i)

if "NOASSERTION" in PkgLicenseConcluded:
    PkgLicenseConcluded.remove("NOASSERTION")    

#print("JaAa", PkgLicenseConcluded) 

#def g_FileCopyrightText(self):
#    
#    a = open(PackageName + "/" + self) 


def spdxpackage(self):

    #cmd = "./g_package_verification.sh " + self[0]  
    cmd = "/home/matthewbuchananastley/app/spdxISO_IEC5962/g_package_verification.sh " + self[0]  
    PackageVerificationCode = subprocess.check_output(cmd, shell=True, stderr=-3).decode().strip("\n")
    #PackageVerificationCode_1 = str(PackageVerificationCode).strip("b'").strip("\\n") + " (./" + self[0] + ".spdx" + " excluded )"
    #PackageVerificationCode_1 = str(PackageVerificationCode) + " (./" + self[0] + ".spdx" + " excluded )"
    PackageVerificationCode_1 = str(PackageVerificationCode) + " (./" + os.path.basename(self[0]) + ".spdx" + " excluded )"
    
    PLicenseConcluded = ch_PackageLicenseInfoFromFiles()
    #print("Ja", PLicenseConcluded)
    PLicenseConcluded.remove('NOASSERTION')
    #print("Ja", PLicenseConcluded)

    PkgLicenseConcluded = [] 

    for i in PLicenseConcluded:
        ii = i.split()
        if len(ii) != 2:
            PkgLicenseConcluded.append("LicenseRef-" + i)

    a = str()

    #a += "PackageName: " + self[0] + "\n"
    a += "PackageName: " + PackageName + "\n"
    a += "SPDXID: " + self[1] + "\n"
    a += "PackageVersion: " + self[2] + "\n" 
    a += "PackageVerificationCode: " + PackageVerificationCode_1 + "\n"
    a += "PackageLicenseDeclared: " + "GPL-3.0-or-later" + "\n"

    for i in PkgLicenseConcluded:
        a += "PackageLicenseInfoFromFiles: " + i + "\n"

    for i in PkgLicenseConcluded:
        a += "PackageLicenseConcluded: " + i + "\n"

    #a += "PackageCopyrightText: " + "<text> 2021 - 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text>" + "\n"
    #a += "PackageCopyrightText: " + "<text> 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text>" + "\n"
    #a += "PackageCopyrightText: " + chklicense([ PackageName, "FileCopyrightText:"]) + "\n"
    a += "PackageCopyrightText: " + getFirstCopyrightText(self) + "\n"
    a += "PackageDownloadLocation: " + DocumentNamespace + "\n"

    #print("Ja", a) 
    #for i in a:
    #    print(i + ": " + a[i]) 
    print(a)


def spdxfiles(self):

    #print("JA", self) 

    if ".spdx" in self[0]: 
        next
    else:
        a1c = "/home/matthewbuchananastley/app/spdxISO_IEC5962/g_sha256sum.sh " + self[0] + "|awk '{print $1}'"  
        a2c = "/home/matthewbuchananastley/app/spdxISO_IEC5962/g_sha1sum.sh " + self[0] + "|awk '{print $1}'"  
        #a1 = str(subprocess.check_output(a1c, shell=True, stderr=-3)).strip("b'")
        #a1 = str(subprocess.check_output(a1c, shell=True, stderr=-3)).strip("b'").strip("\\n")
        a1 = subprocess.check_output(a1c, shell=True, stderr=-3).decode().strip("\n")
        #print("JAAA", a1) 
        #a2 = str(subprocess.check_output(a2c, shell=True, stderr=-3)).strip("b'").strip("\\n")
        a2 = subprocess.check_output(a2c, shell=True, stderr=-3).decode().strip("\n")

        a3c = "/home/matthewbuchananastley/app/spdxISO_IEC5962/g_mimetype.sh " + self[0] 
        a3 = subprocess.check_output(a3c, shell=True, stderr=-3).decode().strip("\n")
        #print("jaaaa",a3)
        #a4 = str(a3).strip("[\\nb']")
        a5 = a3.split()
        a6 = a5[1].split("/")
        Ftype= a6[0].upper()
        #a11 = a6[1].split("-")
        a11 = a6[1].split(".")
        #print("JAAA", a11)
        #a12 = [ "python3", "perl" ] 
        a12 = [ "python", "perl", "x-shellscript" ] 
        if len(a11) == 2: 
            if a11[1] in a12:
                Ftype = "APPLICATION"
        elif a11[0] in a12:
            Ftype = "APPLICATION"

        a7 = self[0].split("/")
   
        #FileSPDXID = "SPDXRef-" + a7[1] 
        FileSPDXID = "SPDXRef-" + a7[-1] 
        #print("JAA",a7[-1])
        #a8 = chklicense([a7[1], "SPDX-License-Identifier:"]).split()
        a8 = chklicense([a7[-1], "SPDX-License-Identifier:"]).split()
        if a8[0] == "NOASSERTION":
            a9 = "NOASSERTION"
        else:
            a9 = a8[0]

        #a10 = chklicense([ a7[1], "FileCopyrightText:"]) 
        a10 = chklicense([ a7[-1], "FileCopyrightText:"]) 

        #a = { "FileName" : "./" + a7[1],
        #a = { "FileName" : "./" + a7[-1],
        a = ""
        a += "FileName: " + "./" + a7[-1] + "\n"
        a += "SPDXID: " + FileSPDXID.replace("_","-") + "\n"
        a += "FileType: " + Ftype + "\n"
        a += "FileChecksum: " + "SHA256: " + a1 + "\n"
        a += "FileChecksum: " + "SHA1: " + a2 + "\n"
        if a7[-1] == 'README.md':
            a += "FileCopyrightText: " + getFirstCopyrightText(self) + "\n"
        else:
            a += "FileCopyrightText: " + a10 + "\n"
        a += "LicenseInfoInFile: " + a9 + "\n"
        a += "LicenseConcluded: " + a9 + "\n"

        #print("#\n#\n#\n")

        #for i in a:
        #    print(i.replace('FileChecksum_1','FileChecksum') + ":", a[i]) 
        if Ftype != 'INODE':
            print("#\n#\n#\n")
            print(a)
        #a = {} 

#d1 = checkchlog(PackageName)
d1 = checkchlog([ PackageLoc, PackageName ])

#print("Ja",d1) 

spdxdoc([DocumentName,DocumentNamespace,prt,CreatorComment]) 
#spdxpackage([ PackageName, PackageSPDXID, d1, chklicense([PackageName, "SPDX-License-Identifier:"])]) 
#spdxpackage([ PackageLoc, PackageSPDXID, d1, chklicense([PackageName, "SPDX-License-Identifier:"])]) 
spdxpackage([ PackageLoc, PackageSPDXID, d1, "SPDX-License-Identifier:"]) 
#print("#\n#\n")

ch_PackageLicenseInfoFromFiles()

#e1 = glob.glob(PackageName + "/*")
e1 = glob.glob( PackageLoc + "/*")
for i in e1:
    #print("JA",i) 
    if i.find(".deb") != -1:
        next
    else:
        #self = [ i ] 
        self = [ i ] 
        spdxfiles(self) 
        #print("Ja",i)

