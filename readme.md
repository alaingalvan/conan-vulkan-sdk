# conan-vulkan-sdk

![Release][release-img]
[![conan-img]][conan-url]
[![License][license-img]][license-url]

[Conan](https://conan.io) package for the [Vulkan SDK](https://github.com/LunarG/VulkanTools) provided by LunarG. Automatically fetches and installs the Vulkan SDK on your Windows/Linux setup.


## Install

Install [Python](https://www.python.org/downloads/) and [Conan](https://www.conan.io/), a C++ Package Manager.

```bash
conan install vulkan-sdk
```

## Deploying

```bash
conan export alaingalvan/stable
conan upload vulkan-sdk/1.0.46.0@alaingalvan/stable
```

[release-img]: https://img.shields.io/badge/release-1.0.46.0-B46BD6.svg?style=flat-square
[conan-img]: https://img.shields.io/badge/conan.io-1.0.46.0-green.svg?style=flat-square
[conan-url]: https://www.conan.io/source/vulkan-sdk/1.0.46.0/alaingalvan/stable
[license-img]: http://img.shields.io/:license-apache-blue.svg?style=flat-square
[license-url]: http://www.apache.org/licenses/LICENSE-2.0
