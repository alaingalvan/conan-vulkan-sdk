#!/usr/bin/python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools
import sys
import os

class vulkansdkConan(ConanFile):

    name = 'vulkan-sdk'
    version = '1.0.21.0'
    license = 'Apache'
    url = 'https://github.com/alaingalvan/conan-vulkan-sdk'
    settings = ('os', 'compiler', 'build_type', 'arch')
    exports = '*'

    foldername = 'Vulkan-LoaderAndValidationLayers-sdk-1.0.21.0'
    builddir = ''

    def source(self):
        zip_name = 'sdk-1.0.21.0.zip'
        tools.download('https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/archive/sdk-1.0.21.0.zip', zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)
        os.rename(self.foldername, 'v')
        self.foldername = 'v' # To Get Around Path being too long errors.

    def system_requirements(self):
        if self.settings.os == 'Linux':
            self.run('sudo apt-get install git cmake build-essential bison libx11-dev libxcb1-dev')
        elif self.settings.os == 'Macos':
            self.output.error('  ***************** Need Help here **************** ')
            self.output.error('  *** OSX not implemented yet. Please help out! *** ')
            self.output.error('  ***************** Need Help here **************** ')
            sys.exit(1)
        elif self.settings.os == 'Android':
            self.output.error('  ***************** Need Help here **************** ')
            self.output.error('  * Android not implemented yet. Please help out! * ')
            self.output.error('  ***************** Need Help here **************** ')
            sys.exit(1)

    def build(self):
        self.builddir = os.path.join(self.conanfile_directory, self.foldername)

        # if self.settings.os == 'Windows':
        #     if self.settings.arch == 'x86_64':
        #         arch = 'x64'
        #     else:
        #         arch = 'x86'
        #     self.run('cd %s & update_external_sources.bat --all' % self.builddir)
        #     self.run('cd %s & build_windows_targets.bat' % self.builddir)
        #     self.run('cd %s & msbuild build/ALL_BUILD.vcxproj /p:Platform=%s /p:Configuration=%s /m /verbosity:m' % (self.builddir, arch, self.settings.build_type))
        # elif self.settings.os == 'Linux':
        #     self.run('./update_external_sources.sh')
        #     self.run('cmake -H. -Bdbuild -DCMAKE_BUILD_TYPE=%s' % self.settings.build_type)
        #     self.run('cd dbuild')
        #     self.run('make')
        #     self.run('export LD_LIBRARY_PATH=%s/Vulkan-LoaderAndValidationLayers/dbuild/loader' % self.conanfile_directory)
        #     self.run('export VK_LAYER_PATH=%s/Vulkan-LoaderAndValidationLayers/dbuild/layers' % self.conanfile_directory)
        #     self.run('cd ../')

    def package(self):
        self.copy(pattern='*', dst='include/vulkan', src='%s/include' % self.builddir, keep_path=False)
        self.copy('*', dst='include/vulkan', src='%s/external/spirv-tools/external/spirv-headers/include/spirv/1.1' % self.builddir)
        self.copy('icd-spv.h', dst='include/vulkan', src='%s/tests' % self.builddir)

        self.copy('*', dst='lib', src='%s/build/loader/%s' % (self.builddir, self.settings.build_type))
        self.copy('*', dst='lib', src='%s/build/layers/%s' % (self.builddir, self.settings.build_type))

        self.copy('*', dst='bin', src='%s/build/loader/%s' % (self.builddir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/build/layers/%s' % (self.builddir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/external/glslang/build/StandAlone/%s' % (self.builddir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/external/spirv-tools/build/tools/%s' % (self.builddir, self.settings.build_type))

    def package_info(self):
            self.cpp_info.libs = ['vulkan-1', 'VKstatic.1', 'VkLayer_utils', 'VkLayer_unique_objects', 'VkLayer_threading', 'VkLayer_swapchain', 'VkLayer_parameter_validation', 'VkLayer_object_tracker', 'VkLayer_image', 'VkLayer_core_validation']
