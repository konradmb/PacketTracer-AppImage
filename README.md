# AppImage for Cisco Packet Tracer

*🎶I'm already Tracer🎶*

### A configuration for [pkg2appimage](https://github.com/AppImage/pkg2appimage) to build Packet Tracer in AppImage form.

## Version: 8.2.1

If you find out that there's a new version available, please let me know by [opening an issue](https://github.com/konradmb/PacketTracer-AppImage/issues/new/?title=Update%20PacketTracer%20to%20x.x&body=Dear%20konradmb,%0APlease%20update%20this%20AppImage%20to%20a%20new%20version%20x.x!%20I%20hate%20you%20because%20I%20have%20a%20**very**%20important%20assignment%20to%20do%20and%20I%20will%20fail%20it%20because%20you%27re%20so%20lazy!%20%F0%9F%98%A1%F0%9F%98%A1%F0%9F%98%A1%0ASincerely,%20xoxo)!

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

### Can't you just put AppImage in releases, so I can simply download one file?

I can't put the resulting AppImage here, because the Packet Tracer license forbids redistribution (at least it said so when I checked the old license, I can't find it in new EULAs, but there is a reason that NetAcad account is required to download PT).

I don't know if Cisco enforces it, but they could send a DMCA takedown request (and GitHub would have to delete whole repo).

## It doesn't work!

If you encounter an error, download Packet Tracer archive from official site: [Cisco_Packet_Tracer_820_Ubuntu_64bit_696ae64b25.deb](https://skillsforall.com/resources/lab-downloads)  (requires login).
Put it into the directory with .yml file, it will be detected automatically.

## Older versions

#### Packet Tracer 7.3.0

Follow the guide, but use `PacketTracer-7.3.0.yml`.

```shell
   ./pkg2appimage PacketTracer-7.2.1.yml
```

In case of error, download [PacketTracer_730_amd64.deb](https://www.netacad.com/portal/resources/file/aa38a51f-45bb-4eb1-89a0-01d961ae1432) and put it into the directory with .yml file.

#### Packet Tracer 7.2.1

Follow the guide, but use `PacketTracer-7.2.1.yml`.

```shell
   ./pkg2appimage PacketTracer-7.2.1.yml
```

In case of error, download [Packet Tracer 7.2.1 for Linux 64 bit.tar.gz](https://www.netacad.com/portal/resources/file/88097a5b-6dbd-43b5-9589-72797dca143c) and put it into the directory with .yml file.

### Packet Tracer 7.1

Cisco deleted previous download link. If you find one, please open an issue.

## Differences from official version 

* PacketTracer binary is patched to change `~/.packettracer` file name to `~/.ptappimage00` as to prevent conflicts with Packet Tracer executed from normal folder.
