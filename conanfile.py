#!/usr/bin/python
# -*- coding: utf-8 -*-
from conans import ConanFile
import os

class vulkansdkConan(ConanFile):

    name = 'vulkan-sdk'
    version = '1.0.33.0'
    license = 'Apache'
    url = 'https://github.com/alaingalvan/conan-vulkan-sdk'
    settings = ('os', 'compiler', 'build_type', 'arch')
    exports = '*'

    builddir = ''

    def build(self):
        self.builddir = 'C:/VulkanSDK/' + os.listdir('C:/VulkanSDK/')[0]

    def package(self):
        self.copy(pattern='*', dst='Include/vulkan', src='%s/include' % self.builddir, keep_path=False)

        is_32 = '' if self.settings.arch == 'x86_64' else '32'
        bin_dir = 'Bin%s' % is_32
        if self.settings.build_type == 'Debug':
            bin_dir = 'Source/lib%s' % is_32

        self.copy('*', dst='lib', src='%s/%s' % (self.builddir, bin_dir))
        self.copy('*', dst='bin', src='%s/%s' % (self.builddir, bin_dir))

    def package_info(self):
        self.cpp_info.libs = [
            'vulkan-1',
            'VKstatic.1',
            'VkLayer_utils',
            'VkLayer_unique_objects',
            'VkLayer_threading',
            'VkLayer_swapchain',
            'VkLayer_screenshot',
            'VkLayer_parameter_validation',
            'VkLayer_object_tracker',
            'VkLayer_image',
            'VkLayer_core_validation',
            'VkLayer_api_dump'
            ]
            
