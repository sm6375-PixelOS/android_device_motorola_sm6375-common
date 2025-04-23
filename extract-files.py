#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/motorola/sm6375-common',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8350',
    'hardware/qcom-caf/wlan',
    'hardware/motorola',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
    (
        'libdiag_system',
        'libqsap_sdk',
        'libthermalclient',
        'libwpa_client',
        'vendor.qti.qspmhal@1.0',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/bin/wfdservice': blob_fixup()
        .add_needed('libwfdservice_shim.so'),
    'system_ext/etc/permissions/moto-telephony.xml': blob_fixup()
        .regex_replace('/system/', '/system_ext/'),
    'system_ext/priv-app/ims/ims.apk': blob_fixup()
        .apktool_patch('ims-patches'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
        'odm/bin/hw/vendor.dolby_sp.media.c2@1.0-service': blob_fixup()
         .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0_sp.so')
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     'odm/lib64/libcodec2_store_dolby_sp.so': blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     ('odm/lib64/libcodec2_soft_ac4dec_sp.so', 'odm/lib64/libcodec2_soft_ddpdec_sp.so'): blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
         .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     ('odm/lib64/libcodec2_soft_common_sp.so', 'odm/lib64/libcodec2_hidl_plugin_sp.so'): blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     (
         'odm/lib/libdlbdsservice_v3_6.so',
         'odm/lib/libstagefright_soft_ddpdec.so',
         'odm/lib64/libdlbdsservice_sp.so',
         'odm/lib64/libdlbdsservice_v3_6.so'
     ): blob_fixup().replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     'odm/lib64/libcodec2_vndk_sp.so': blob_fixup()
         .replace_needed('libui.so', 'libui_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     'odm/lib64/libcodec2_hidl@1.0_sp.so': blob_fixup()
         .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin_sp.so')
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     'odm/lib64/libui_sp.so': blob_fixup()
         .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V6-ndk.so')
         .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
    ('system_ext/lib/libwfdmmsrc_system.so', 'system_ext/lib64/libwfdmmsrc_system.so'): blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    'odm/bin/hw/vendor.dolby_sp.media.c2@1.0-service': blob_fixup()
         .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0_sp.so')
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     'odm/lib64/libcodec2_store_dolby_sp.so': blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     ('odm/lib64/libcodec2_soft_ac4dec_sp.so', 'odm/lib64/libcodec2_soft_ddpdec_sp.so'): blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
         .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     ('odm/lib64/libcodec2_soft_common_sp.so', 'odm/lib64/libcodec2_hidl_plugin_sp.so'): blob_fixup()
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     (
         'odm/lib/libdlbdsservice_v3_6.so',
         'odm/lib/libstagefright_soft_ddpdec.so',
         'odm/lib64/libdlbdsservice_sp.so',
         'odm/lib64/libdlbdsservice_v3_6.so'
     ): blob_fixup().replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     'odm/lib64/libcodec2_vndk_sp.so': blob_fixup()
         .replace_needed('libui.so', 'libui_sp.so')
         .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
     'odm/lib64/libcodec2_hidl@1.0_sp.so': blob_fixup()
         .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin_sp.so')
         .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
     'odm/lib64/libui_sp.so': blob_fixup()
         .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V6-ndk.so')
         .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
    ('system_ext/lib/libwfdservice.so', 'system_ext/lib64/libwfdservice.so'): blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V4-cpp.so'),
    'vendor/etc/vintf/manifest/vendor.dolby.media.c2@1.0-service.xml': blob_fixup()
        .regex_replace('IComponentStore/default9', 'IComponentStore/default'),
    'vendor/etc/qcril_database/qcrilNr.db': blob_fixup()
        .patch_file('qcril-patches/qcrilNr.db.patch'),
    'vendor/etc/qcril_database/upgrade/config/6.0_config.sql': blob_fixup()
        .patch_file('qcril-patches/6.0_config.sql.patch'),
}  # fmt: skip

module = ExtractUtilsModule(
    'sm6375-common',
    'motorola',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
