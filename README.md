# AppImage for Cisco Packet Tracer
*🎶I'm already Tracer🎶*

### A configuration for [pkg2appimage](https://github.com/AppImage/pkg2appimage) to build Packet Tracer in AppImage form.

## How to use it?

1. Clone this repository and go to its directory.
    ```shell
    git clone https://github.com/konradmb/PacketTracer-AppImage.git
    cd PacketTracer-AppImage/
    ```
2. Download Packet Tracer 7.3.0 archive from official site: [PacketTracer_730_amd64.deb](https://www.netacad.com/portal/resources/file/aa38a51f-45bb-4eb1-89a0-01d961ae1432) (requires login).
3. And put it into `PacketTracer-AppImage` directory.
4. Download pkg2appimage tool and make it executable.
   ```shell
   wget https://github.com/AppImage/pkg2appimage/raw/master/pkg2appimage
   chmod +x pkg2appimage
   ```
5. Build it:

   ```shell
   ./pkg2appimage PacketTracer.yml
   ```

7. After a short break you should get an executable inside `out/` directory.

### Older versions

#### Packet Tracer 7.2.1

Follow the guide, but download [Packet Tracer 7.2.1 for Linux 64 bit.tar.gz](https://www.netacad.com/portal/resources/file/88097a5b-6dbd-43b5-9589-72797dca143c).

And build using:

```shell
   ./pkg2appimage PacketTracer-7.2.1.yml
```

#### Packet Tracer 7.1

Cisco deleted previous download link. If you find one, please open an issue.

## Differences from official version 

* PacketTracer7 binary is patched to change `~/.packettracer` file name to `~/.ptappimage00` as to prevent conflicts with Packet Tracer executed from normal folder.
