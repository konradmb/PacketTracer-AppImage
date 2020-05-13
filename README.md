# AppImage for Cisco Packet Tracer
*🎶I'm already Tracer🎶*

### A configuration for [pkg2appimage](https://github.com/AppImage/pkg2appimage) to build Packet Tracer in AppImage form.

## How to use it?

1. Clone this repository and `cd` into it.
    ```shell
    git clone https://github.com/konradmb/PacketTracer-AppImage.git
    cd PacketTracer-AppImage/
    ```
2. Download pkg2appimage tool and make it executable.
   ```shell
   wget https://github.com/AppImage/pkg2appimage/raw/master/pkg2appimage
   chmod +x pkg2appimage
   ```
3. Build it:

   ```shell
   ./pkg2appimage PacketTracer.yml
   ```

4. After a short break you should get an executable inside `out/` directory.

## It doesn't work!

If you encounter an error, download Packet Tracer archive from official site: [PacketTracer_730_amd64.deb](https://www.netacad.com/portal/resources/file/aa38a51f-45bb-4eb1-89a0-01d961ae1432) (requires login).
Put it into the directory with .yml file, it will be detected automatically.

## Older versions

### Packet Tracer 7.2.1

Follow the guide, but use `PacketTracer-7.2.1.yml`.

```shell
   ./pkg2appimage PacketTracer-7.2.1.yml
```

In case of error, download [Packet Tracer 7.2.1 for Linux 64 bit.tar.gz](https://www.netacad.com/portal/resources/file/88097a5b-6dbd-43b5-9589-72797dca143c) and put it into the directory with .yml file.

### Packet Tracer 7.1

Cisco deleted previous download link. If you find one, please open an issue.

## Differences from official version 

* PacketTracer7 binary is patched to change `~/.packettracer` file name to `~/.ptappimage00` as to prevent conflicts with Packet Tracer executed from normal folder.
