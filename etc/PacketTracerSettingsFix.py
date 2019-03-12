import os

homePath = os.getenv("HOME")
packetTracerHomePath = homePath + "/PacketTracer"
packetTracerPath = os.getcwd() + "/share/PacketTracer"

settingsFilePath = homePath + "/.ptappimage00"
settingsFile = open(settingsFilePath, "wb")

fileHeader = bytearray([0x00,0x00,0x00,0x01,0x00,0x00,0x00])
pathStart =  bytearray("^", "utf16")[2:]
pathSeparator = bytearray([0x00,0x00,0x00,0x32, 0x00])

packetTracerPathEncoded = bytearray(packetTracerPath, "utf16")[2:-1]
packetTracerHomePathEncoded = bytearray(packetTracerHomePath, "utf16")[2:-1]
encodedPaths = pathStart + packetTracerPathEncoded \
            + pathSeparator + packetTracerHomePathEncoded
encodedPaths = encodedPaths

bytesToWrite = fileHeader + encodedPaths 
settingsFile.write(bytesToWrite)
settingsFile.close()
