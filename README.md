# AppImage for Cisco Packet Tracer
*🎶I'm already Tracer🎶*

### A configuration for [pkg2appimage](https://github.com/AppImage/pkg2appimage) to build Packet Tracer in AppImage form.

## How to use it?

1. Clone this repository and go to its directory.
    ```shell
    git clone https://github.com/konradmb/PacketTracer-AppImage.git
    cd PacketTracer-AppImage/
    ```
2. Download Packet Tracer 7.2.1 or 7.1.1 archive from [official site](https://www.netacad.com/courses/packet-tracer):
   * `Packet Tracer 7.2.1 for Linux 64 bit.tar.gz`
   * or `Packet Tracer 7.1.1 for Linux 64 bit.tar.gz`
3. And put it into `PacketTracer-AppImage` directory.
4. Download pkg2appimage tool and make it executable.
   ```shell
   wget https://github.com/AppImage/pkg2appimage/raw/master/pkg2appimage
   chmod +x pkg2appimage
   ```
5. Build it:
   * If you want to build Packet Tracer 7.2.1:
   ```shell
   ./pkg2appimage PacketTracer.yml
   ```
   * Or if you want to build Packet Tracer 7.1.1:
   ```shell
   ./pkg2appimage PacketTracer-7.1.yml
   ```
7. After a short break you should get an executable inside `out/` directory.


## Differences from official version 

* PacketTracer7 binary is patched to change `~/.packettracer` file name to `~/.ptappimage00` as to prevent conflicts with Packet Tracer executed from normal folder.
