<img align="center" src="Macast2_slogan.png" alt="slogan" height="auto"/>

# Macast2

[![visitor](https://visitor-badge.glitch.me/badge?page_id=isdkz.Macast2)](https://github.com/isdkz/Macast2/releases/latest)
![stars](https://img.shields.io/badge/dynamic/json?label=github%20stars&query=stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fisdkz%2FMacast2)
[![downloads](https://img.shields.io/github/downloads/isdkz/Macast2/total?color=blue)](https://github.com/isdkz/Macast2/releases/latest)
[![plugins](https://shields-staging.herokuapp.com/github/directory-file-count/isdkz/Macast2-plugins?type=dir&label=plugins)](https://github.com/isdkz/Macast2-plugins)
[![pypi](https://img.shields.io/pypi/v/Macast2)](https://pypi.org/project/Macast2/)
[![aur](https://img.shields.io/aur/version/Macast2-git?color=yellowgreen)](https://aur.archlinux.org/packages/Macast2-git/)
[![build](https://img.shields.io/github/workflow/status/isdkz/Macast2/Build%20Macast2)](https://github.com/isdkz/Macast2/actions/workflows/build-Macast2.yaml)
[![mac](https://img.shields.io/badge/MacOS-10.14%20and%20higher-lightgrey?logo=Apple)](https://github.com/isdkz/Macast2/releases/latest)
[![windows](https://img.shields.io/badge/Windows-7%20and%20higher-lightgrey?logo=Windows)](https://github.com/isdkz/Macast2/releases/latest)
[![linux](https://img.shields.io/badge/Linux-Xorg-lightgrey?logo=Linux)](https://github.com/isdkz/Macast2/releases/latest)



[中文说明](README_ZH.md)

A menu bar application using mpv as **DLNA Media Renderer**. You can push videos, pictures or musics from your mobile phone to your computer.


## Installation

- ### MacOS || Windows || Debian

  Download link:  [Macast2 release latest](https://github.com/isdkz/Macast2/releases/latest)

- ### Package manager

  ```shell
  pip install Macast2
  Macast2-gui # or Macast2-cli
  ```

  Please see our wiki for more information(like **aur** support): [#package-manager](https://github.com/isdkz/Macast2/wiki/Installation#package-manager)  
  Linux users may have problems installing using pip. Two additional libraries that I have modified need to be installed:

  ```shell
  pip install git+https://github.com/isdkz/pystray.git
  pip install git+https://github.com/isdkz/pyperclip.git
  ```

  **See [this](https://github.com/isdkz/Macast2/wiki/Installation#linux) for Linux compatibility**

- ### Build from source

  Please refer to: [Macast2 Development](docs/Development.md)


## Usage

- **For ordinary users**  
After opening this app, a small icon will appear in the **menubar** / **taskbar** / **desktop panel**, then you can push your media files from a local DLNA client to your computer.

- **For advanced users**  
  1. By loading the [Macast2-plugins](https://github.com/isdkz/Macast2-plugins), Macast2 can support third-party players like IINA and PotPlayer.  
  For more information, see: [#how-to-use-third-party-player-plug-in](https://github.com/isdkz/Macast2/wiki/FAQ#how-to-use-third-party-player-plug-in)
  2. You can modify the shortcut keys or configuration of the default mpv player by yourself, see: [#how-to-set-personal-configurations-to-mpv](https://github.com/isdkz/Macast2/wiki/FAQ#how-to-set-personal-configurations-to-mpv)

- **For developer**  
You can use a few lines of code to add support for other players like IINA and PotPlayer or even add additional features, like downloading media files while playing videos.  
Tutorials and examples are shown in: [Macast2/wiki/Custom-Renderer](https://github.com/isdkz/Macast2/wiki/Custom-Renderer).  
Fell free to submit a pull request to [Macast2-plugins](https://github.com/isdkz/Macast2-plugins).  


## FAQ
If you have any questions about this application, please check: [Macast2/wiki/FAQ](https://github.com/isdkz/Macast2/wiki/FAQ).  
If this does not solve your problem, please open a new issue to notify us, we are willing to help you solve the problem.

## Screenshots

You can copy the video link after the video is casted：  
<img align="center" width="400" src="https://github.com/isdkz/isdkz.github.io/raw/master/assets/img/Macast2/copy_uri.png" alt="copy_uri" height="auto"/>

Or select a third-party player plug-in  
<img align="center" width="400" src="https://github.com/isdkz/isdkz.github.io/raw/master/assets/img/Macast2/select_renderer.png" alt="select_renderer" height="auto"/>

## Relevant links

[UPnP™ Device Architecture 1.1](http://upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.1.pdf)

[UPnP™ Resources](http://upnp.org/resources/upnpresources.zip)

[UPnP™ ContentDirectory:1 service](http://upnp.org/specs/av/UPnP-av-ContentDirectory-v1-Service.pdf)

[UPnP™ MediaRenderer:1 device](http://upnp.org/specs/av/UPnP-av-MediaRenderer-v1-Device.pdf)

[UPnP™ AVTransport:1 service](http://upnp.org/specs/av/UPnP-av-AVTransport-v1-Service.pdf)

[UPnP™ RenderingControl:1 service](http://upnp.org/specs/av/UPnP-av-RenderingControl-v1-Service.pdf)

[python-upnp-ssdp-example](https://github.com/ZeWaren/python-upnp-ssdp-example)
