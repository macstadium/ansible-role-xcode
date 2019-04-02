# Ansible Role: Xcode

![GPL-3.0 licensed][badge-license]
[![Build Status](https://travis-ci.org/macstadium/ansible-role-xcode.svg?branch=master)](https://travis-ci.org/macstadium/ansible-role-xcode)


Installs [Xcode][xcode] on MacOS according to supplied variables.

## Requirements

The role is capable of installing Xcode 8 and above.

The Xcode installation requires a pre-downloaded Xcode xip file on the target machine. You can find all Xcode versions in the [Apple Downloads Page][apple-downloads].

A UI session is also required. This means the user you are using to execute the role must be logged on to the OSX machine.

The role expects [Spotlight][spotlight] to be enabled. It uses Spotlight search to check whether Xcode is already installed.

## Role Variables

Role variables and their default values are listed below.
You can find all default variables in [`defaults/main.yml`](defaults/main.yml)

    xcode_xip_location:

The Xcode xip location on the target computer.

    xcode_major_version:

The major Xcode version to be installed. The way extra packages are installed varies between Xcode versions. That is why the major version must be known when running the provisioning scripts.

    xcode_build: /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild

The path to the `xcodebuild` tool. 

    xcode_packages_location: /Applications/Xcode.app/Contents/Resources/Packages

The directory containing all extra Xcode packages to be installed.

## Dependencies

None.

## Example Playbook

    - hosts: localhost
      vars:
        xcode_xip_location: '/Users/user/Downloads/Xcode_10.1.xip'
        xcode_major_version: 10
      roles:
        - xcode

## License

[GPL-3.0][link-license]

## Author Information

This role was created in 2019 by [MacStadium, Inc][macstadium].

#### Maintainer(s)

- [Ivan Spasov](https://github.com/ispasov)

[macstadium]: https://www.macstadium.com/
[badge-license]: https://img.shields.io/badge/License-GPL3-green.svg
[link-license]: https://raw.githubusercontent.com/macstadium/ansible-role-xcode/master/LICENSE
[xcode]: https://developer.apple.com/xcode/
[apple-downloads]: https://developer.apple.com/download/more/
[spotlight]: https://support.apple.com/en-us/HT204014