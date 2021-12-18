import os
import sys


def write_pt_file(pathStartChar, pathSeparatorChar, packetTracerRoot, settingsFileName, homeFolder):
    homePath = os.getenv("HOME")
    packetTracerHomePath = homePath + homeFolder

    settingsFilePath = homePath + settingsFileName
    settingsFile = open(settingsFilePath, "wb")

    fileHeader = bytearray([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00])
    if type(pathStartChar) == str:
        pathStart = bytearray(pathStartChar, "utf16")[2:]
    else:
        pathStart = bytearray(pathStartChar)
    pathSeparator = bytearray([0x00, 0x00, 0x00, pathSeparatorChar, 0x00])
    packetTracerPath = os.getcwd() + packetTracerRoot

    packetTracerPathEncoded = bytearray(packetTracerPath, "utf16")[2:-1]
    packetTracerHomePathEncoded = bytearray(
        packetTracerHomePath, "utf16")[2:-1]
    encodedPaths = pathStart + packetTracerPathEncoded \
        + pathSeparator + packetTracerHomePathEncoded
    encodedPaths = encodedPaths

    bytesToWrite = fileHeader + encodedPaths
    settingsFile.write(bytesToWrite)
    settingsFile.close()


if sys.argv[1] == "8.1":
    write_pt_file([0x82, 0x00], 0x1E, "/opt/pt", "/.ptappimage00", "/pt")
elif sys.argv[1] == "7.3":
    write_pt_file(">", 0x32, "/opt/pt", "/.ptappimage00", "/PacketTracer")
elif sys.argv[1] == "7.2":
    write_pt_file("^", 0x32, "/share/PacketTracer",
                  "/.ptappimage00", "/PacketTracer")
