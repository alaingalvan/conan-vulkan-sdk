# conan-vulkan-sdk

![Release][release-img] [![conan-img]][conan-url] [![License][license-img]][license-url]

> **NOTE**: I have no affiliation with the Khronos Group. 

[Conan](https://conan.io) package for the [Vulkan SDK](https://github.com/LunarG/VulkanTools) provided by LunarG.


## Usage

Install [Python](https://www.python.org/downloads/), [Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx), and [Conan](https://www.conan.io/), a C++ Package Manager, 

On Windows make sure that your path includes Visual Studio's `msbuild` as well as `python`.

```bash
conan install conan-vulkan-sdk --build
```

## Features

- **Windows/Linux Support** - This package supports those platforms, with android/osx on its way!

- **Vulkan's Header Files** - Gives you access to all of Vulkan's core functionality.

- **ICD Loader** - Handles Multi-GPU support as well as loading the different layers of Vulkan.

- **Validation Layers** - Enables error checking on the Vulkan Driver.

## Development

Build specs based on instructions on the [Vulkan Repo](https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/blob/master/BUILD.md), as well as what I was able to see from the sdk binaries. 

Versions correspond with releases on the KhronosGroup Repo. Please ask the Khronos Group to distribute binaries! 

### Call to Action

Let's write a Heroku app that automatically releases the latest version of the sdk to conan when the Khronos Group Repo is updated! 

[release-img]: https://img.shields.io/badge/release-1.0.21.0-B46BD6.svg?style=flat-square
[conan-img]: https://img.shields.io/badge/conan.io-1.0.21.0-green.svg?style=flat-square
[conan-url]: https://www.conan.io/source/vulkan-sdk/1.0.21.0/alaingalvan/testing
[license-img]: http://img.shields.io/:license-apache-blue.svg?style=flat-square
[license-url]: http://www.apache.org/licenses/LICENSE-2.0