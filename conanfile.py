#!/usr/bin/python
# -*- coding: utf-8 -*-
from conans import ConanFile, CMake, tools
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

    def source(self):
        zip_name = 'sdk-1.0.21.0.zip'
        tools.download('https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/archive/sdk-1.0.21.0.zip', zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)

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
        curdir = self.conanfile_directory + '/' + self.foldername
        cmake = CMake(self.settings)
        self.run("cd %s & dir" % curdir)

        if self.settings.os == 'Windows':
            if self.settings.arch == 'x86_64':
                arch = 'x64'
            else:
                arch = 'x86'
            self.run('cd %s & update_external_sources.bat --all' % curdir)
            self.run('cd %s & build_windows_targets.bat' % curdir)
            self.run('cd %s & msbuild build/ALL_BUILD.vcxproj /p:Platform=%s /p:Configuration=%s /m ' % (curdir, arch, self.settings.build_type))
        elif self.settings.os == 'Linux':
            self.run('./update_external_sources.sh')
            self.run('cmake -H. -Bdbuild -DCMAKE_BUILD_TYPE=%s' % self.settings.build_type)
            self.run('cd dbuild')
            self.run('make')
            self.run('export LD_LIBRARY_PATH=%s/Vulkan-LoaderAndValidationLayers/dbuild/loader' % self.conanfile_directory)
            self.run('export VK_LAYER_PATH=%s/Vulkan-LoaderAndValidationLayers/dbuild/layers' % self.conanfile_directory)
            self.run('cd ../')

    def package(self):
        curdir = self.conanfile_directory + '/' + self.foldername
        self.copy('*', dst='include', src='%s/include' % curdir)
        self.copy('*', dst='include', src='%s/external/spirv-tools/external/spirv-headers/include/spirv/1.1' % curdir)
        self.copy('icd-spv.h', dst='include', src='%s/tests' % curdir)

        self.copy('*', dst='lib', src='%s/build/loader/%s' % (curdir, self.settings.build_type))
        self.copy('*', dst='lib', src='%s/build/layers/%s' % (curdir, self.settings.build_type))

        self.copy('*', dst='bin', src='%s/build/loader/%s' % (curdir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/build/layers/%s' % (curdir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/external/glslang/build/StandAlone/%s' % (curdir, self.settings.build_type))
        self.copy('*', dst='bin', src='%s/external/spirv-tools/build/tools/%s' % (curdir, self.settings.build_type))