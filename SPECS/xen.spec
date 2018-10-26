# -*- rpm-spec -*-

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define with_sysv 0
%define with_systemd 1

# Use the production hypervisor by default
%define default_debug_hypervisor 0

%define COMMON_OPTIONS DESTDIR=%{buildroot} %{?_smp_mflags}

# For 32bit dom0 userspace, we need to cross compile a 64bit Xen
%ifarch %ix86
%define HVSOR_OPTIONS %{COMMON_OPTIONS} XEN_TARGET_ARCH=x86_64 CROSS_COMPILE=x86_64-linux-gnu-
%define TOOLS_OPTIONS %{COMMON_OPTIONS} XEN_TARGET_ARCH=x86_32 debug=n
%endif

# For 64bit
%ifarch x86_64
%define HVSOR_OPTIONS %{COMMON_OPTIONS} XEN_TARGET_ARCH=x86_64
%define TOOLS_OPTIONS %{COMMON_OPTIONS} XEN_TARGET_ARCH=x86_64 debug=n
%endif

%define base_cset RELEASE-%{version}
%define base_dir  %{name}-%{version}

Summary: Xen is a virtual machine monitor
Name:    xen
Version: 4.7.6
Release: 6.2.1.xcp
License: GPLv2 and LGPLv2+ and BSD
URL:     http://www.xenproject.org
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=%{base_cset}&prefix=%{base_dir}&format=tar.gz#/%{base_dir}.tar.gz
Patch0: build-disable-qemu-trad.patch
Patch1: build-tweaks.patch
Patch2: disable-efi.patch
Patch3: autoconf-libjson.patch
Patch4: configure-build.patch
Patch5: builder-makefiles.patch
Patch6: changeset-info.patch
Patch7: xenserver-configuration.patch
Patch8: coverity-model.patch
Patch9: backport-087369973214.patch
Patch10: backport-dc111e9f0d99.patch
Patch11: backport-a4041364c3ae.patch
Patch12: backport-9858a1f3fb9a.patch
Patch13: backport-c0e854be515b.patch
Patch14: backport-e90e2431a4ae.patch
Patch15: backport-97aff087fd0b.patch
Patch16: backport-fa807e2ff69d.patch
Patch17: backport-bce2dd64b52e.patch
Patch18: backport-91ca84c862b1.patch
Patch19: backport-bacbf0cb7349.patch
Patch20: backport-c9e5a6a232db.patch
Patch21: backport-212d27297af9.patch
Patch22: backport-289c53a49307.patch
Patch23: backport-635c5ec3f0ee.patch
Patch24: backport-cd42ccb27f4e.patch
Patch25: backport-eb4858721050.patch
Patch26: backport-ce34d6b036ed.patch
Patch27: backport-6e908ee108ca.patch
Patch28: backport-759b9618b8a2.patch
Patch29: backport-490a39a1dbc7.patch
Patch30: backport-06f083c82683.patch
Patch31: backport-31689dcb0fbf.patch
Patch32: backport-a2c8399a91bf.patch
Patch33: backport-d72fd26d5f17.patch
Patch34: backport-e2aba42bff72.patch
Patch35: backport-2511f89d9a5e.patch
Patch36: backport-b49839ef4e6b.patch
Patch37: backport-53c300ab1ca0.patch
Patch38: backport-45aa97876683.patch
Patch39: backport-d18224766fa2.patch
Patch40: backport-559f439bfa3b.patch
Patch41: backport-56fef9e367b2.patch
Patch42: backport-c6f7d2174780.patch
Patch43: backport-ee3fd57acd90.patch
Patch44: backport-509019f42dd5.patch
Patch45: backport-a6288d5bb8b9.patch
Patch46: backport-6a962ebddce8.patch
Patch47: backport-70dda5f4e9c9.patch
Patch48: backport-5efcebc66de0.patch
Patch49: backport-668ba1f85bf2.patch
Patch50: backport-7edc10831448.patch
Patch51: backport-f755485cbd2a.patch
Patch52: backport-e04b562377b3.patch
Patch53: backport-41b61be1c244.patch
Patch54: backport-2ad72c0b4676.patch
Patch55: backport-4ef815bf611d.patch
Patch56: backport-920234259475.patch
Patch57: backport-e3eb84e33c36.patch
Patch58: backport-7179cd39efdb.patch
Patch59: backport-fa74e70500fd.patch
Patch60: backport-93340297802b.patch
Patch61: backport-cbfe4db8d750.patch
Patch62: backport-dcf22aa0dc08.patch
Patch63: backport-db6c2264e698.patch
Patch64: backport-b942c31bc1d4.patch
Patch65: backport-698d0f377d72.patch
Patch66: backport-3adef8e3270f.patch
Patch67: backport-939ba61bd376.patch
Patch68: backport-c99986fa168e.patch
Patch69: backport-5464f1210c63.patch
Patch70: backport-51e5d6c7a296.patch
Patch71: backport-222560eb0d0e.patch
Patch72: backport-de82feebf2c1.patch
Patch73: backport-d6d67b0475a1.patch
Patch74: backport-e30c8a11a9e8.patch
Patch75: backport-5c7716379ee2.patch
Patch76: backport-8695b556205f.patch
Patch77: backport-afb118e71967.patch
Patch78: backport-12b3174d945b.patch
Patch79: backport-d6be2cfccfff.patch
Patch80: backport-0831e9944612.patch
Patch81: backport-d45fae589b8d.patch
Patch82: backport-1ef5056bd627.patch
Patch83: backport-3a7f872ae427.patch
Patch84: backport-f1446de4ba52.patch
Patch85: backport-424fdc67e90b.patch
Patch86: backport-e3b002f842c0.patch
Patch87: backport-50a12dd59f23.patch
Patch88: backport-4f13e5b3f69a.patch
Patch89: backport-70c95ecd5c0e.patch
Patch90: backport-4abcd521bf46.patch
Patch91: backport-a0e98991b040.patch
Patch92: backport-7cae6b6eb743.patch
Patch93: backport-a0b421617935.patch
Patch94: backport-f948ce4371cd.patch
Patch95: backport-6a6bbedd39e3.patch
Patch96: backport-9864841914c2.patch
Patch97: backport-ac6a4500b2be.patch
Patch98: backport-c88da9ec8852.patch
Patch99: backport-08fac63ec0b8.patch
Patch100: backport-1cb650c3191f.patch
Patch101: backport-44d3196903f3.patch
Patch102: backport-bc1e0ea329ec.patch
Patch103: backport-90051a4ce585.patch
Patch104: backport-9bd6b01f9d46.patch
Patch105: backport-524a98c2ac5e.patch
Patch106: backport-a2323df5f47c.patch
Patch107: backport-86ad4d054a08.patch
Patch108: backport-7b2e218fd6eb.patch
Patch109: backport-b30c5979e02c.patch
Patch110: backport-ae20ccf070bc.patch
Patch111: backport-58cbc034dc62.patch
Patch112: backport-9b7c0ce58396.patch
Patch113: backport-f71628bc1593.patch
Patch114: backport-7581a378b0b8.patch
Patch115: backport-5a77ccf609da.patch
Patch116: backport-8844ed299a88.patch
Patch117: backport-04dbb7109614.patch
Patch118: backport-d4a24c64b60d.patch
Patch119: backport-1edbf34e63c8.patch
Patch120: backport-7f8445d9678a.patch
Patch121: backport-195ca0e1de85.patch
Patch122: backport-d18216a0c03c.patch
Patch123: backport-62c7b99a1079.patch
Patch124: backport-78da0c2a7a9c.patch
Patch125: backport-9b93c6b3695b.patch
Patch126: backport-7f11aa4b2b1f.patch
Patch127: backport-d6e9f8d4f35d.patch
Patch128: backport-b108240265de.patch
Patch129: backport-6902cb00e031.patch
Patch130: backport-e7745d8ef588.patch
Patch131: backport-8ef5f344d061.patch
Patch132: backport-9442404b91be.patch
Patch133: backport-e318fa314550.patch
Patch134: backport-f68c7c618a3a.patch
Patch135: backport-77751ed79e3c.patch
Patch136: backport-a013e1b9e95e.patch
Patch137: backport-e3f64938272e.patch
Patch138: backport-7ecd11c90a13.patch
Patch139: backport-b4f98dc0d82c.patch
Patch140: backport-0d670cd46cb5.patch
Patch141: backport-5823d6eb40af.patch
Patch142: backport-9a7fbdd6925b.patch
Patch143: backport-4c8153d97efe.patch
Patch144: backport-04f34e76ac50.patch
Patch145: backport-8198ff2cdfbc.patch
Patch146: backport-60f07f8adb5d.patch
Patch147: backport-a9404c0e5305.patch
Patch148: backport-a579c8bcf348.patch
Patch149: backport-e3b93b3c5954.patch
Patch150: backport-c5f640ea6046.patch
Patch151: backport-1366a0e76db6.patch
Patch152: backport-461f0482033b.patch
Patch153: backport-1c5e242e6d6e.patch
Patch154: backport-0d1a96043a75.patch
Patch155: backport-7cc806d7f1d9.patch
Patch156: backport-d9eb706356ad.patch
Patch157: backport-20f1976b4419.patch
Patch158: backport-90288044a67a.patch
Patch159: backport-4c09689153c3.patch
Patch160: backport-6b792e28bca8.patch
Patch161: backport-143e0c2c2d64.patch
Patch162: backport-68209ad1d2a7.patch
Patch163: backport-82942526572c.patch
Patch164: backport-62999081ca27.patch
Patch165: backport-4da2fe19232e.patch
Patch166: backport-930f7879248e.patch
Patch167: backport-f0f1a778d4d5.patch
Patch168: backport-806e07eecfe3.patch
Patch169: backport-7c275549f46c.patch
Patch170: backport-cd3ed39b9df0.patch
Patch171: backport-69d99d1b223f.patch
Patch172: backport-9e50d8adc945.patch
Patch173: backport-eb4e638a4747.patch
Patch174: backport-41d1fcb1c9bf.patch
Patch175: backport-4098b092e190.patch
Patch176: backport-4187f79dc718.patch
Patch177: backport-e7a370733bd2.patch
Patch178: backport-37f074a33831.patch
Patch179: backport-664adc5ccab1.patch
Patch180: backport-d73e68c08f1f.patch
Patch181: backport-f99b7b06378d.patch
Patch182: backport-4d69b3495986.patch
Patch183: backport-1c2ea5ee05f6.patch
Patch184: backport-71b7b4e0f5f9.patch
Patch185: backport-a08a9cd3afa6.patch
Patch186: backport-77690ea09ab2.patch
Patch187: backport-cd579578aac4.patch
Patch188: backport-ec832dddc4c5.patch
Patch189: backport-7b6546e83147.patch
Patch190: backport-a65a24209cd8.patch
Patch191: backport-6df4b481b0c5.patch
Patch192: backport-cf23c69fdd48.patch
Patch193: backport-23044a4e00c1.patch
Patch194: backport-9c23ed56d797.patch
Patch195: backport-e1ab1c03ad6a.patch
Patch196: backport-1462f9ea8f42.patch
Patch197: backport-b08da5859b72.patch
Patch198: backport-11dd1f6e2da5.patch
Patch199: backport-622620792431.patch
Patch200: backport-8d201cae61db.patch
Patch201: backport-f5a246e1c219.patch
Patch202: backport-7e781bdeaeb4.patch
Patch203: backport-83b191eaa194.patch
Patch204: backport-c688dceca59f.patch
Patch205: backport-0e318c7b354d.patch
Patch206: backport-edf4af67047c.patch
Patch207: backport-f942a9b4a120.patch
Patch208: backport-f37c2aa32347.patch
Patch209: backport-52dd77ed9361.patch
Patch210: backport-56a53ee1c11b.patch
Patch211: backport-4ed00f57f086.patch
Patch212: backport-6b6500b3cbaa.patch
Patch213: backport-89d55473ed16.patch
Patch214: backport-3b2966e72c41.patch
Patch215: backport-0de212b03066.patch
Patch216: backport-9976f3874d4c.patch
Patch217: backport-b90f86be161c.patch
Patch218: backport-f97f774b5aa6.patch
Patch219: backport-2375832c7e51.patch
Patch220: backport-34ae3fce896c.patch
Patch221: backport-6606cf3e2af0.patch
Patch222: backport-642123c5123f.patch
Patch223: backport-704538a47411.patch
Patch224: backport-af2a20e40e92.patch
Patch225: backport-7f76b3a06aef.patch
Patch226: backport-85cb15dfe4d1.patch
Patch227: backport-328ca55b7bd4.patch
Patch228: backport-f30e3cf34042.patch
Patch229: backport-730dc8d2c9e1.patch
Patch230: backport-f54b63e8617a.patch
Patch231: backport-94fda356fcdc.patch
Patch232: backport-4d94828cf111.patch
Patch233: backport-80599f0b7701.patch
Patch234: backport-be73a842e642.patch
Patch235: backport-ee7689b94ac7.patch
Patch236: backport-1ac46b556326.patch
Patch237: xsa269-4.8.patch
Patch238: xsa272.patch
Patch239: 0001-x86-spec-ctrl-Yet-more-fixes-for-xpti-parsing.patch
Patch240: 0002-x86-spec-ctrl-Calculate-safe-PTE-addresses-for-L1TF-.patch
Patch241: 0003-x86-spec-ctrl-Introduce-an-option-to-control-L1TF-mi.patch
Patch242: 0004-x86-shadow-Infrastructure-to-force-a-PV-guest-into-s.patch
Patch243: 0005-x86-mm-Plumbing-to-allow-any-PTE-update-to-fail-with.patch
Patch244: 0006-x86-pv-Force-a-guest-into-shadow-mode-when-it-writes.patch
Patch245: 0007-x86-spec-ctrl-CPUID-MSR-definitions-for-L1D_FLUSH.patch
Patch246: 0008-x86-msr-Virtualise-MSR_FLUSH_CMD-for-guests.patch
Patch247: 0009-x86-spec-ctrl-Introduce-an-option-to-control-L1D_FLU.patch
Patch248: 0010-x86-shadow-dom0-force-shadow-for-debugging-purposes.patch
Patch249: detect-nehalem-c-state.patch
Patch250: quirk-hp-gen8-rmrr.patch
Patch251: quirk-pci-phantom-function-devices.patch
Patch252: sched-credit1-use-per-pcpu-runqueue-count.patch
Patch253: 0001-x86-hpet-Pre-cleanup.patch
Patch254: 0002-x86-hpet-Use-singe-apic-vector-rather-than-irq_descs.patch
Patch255: 0003-x86-hpet-Post-cleanup.patch
Patch256: 0002-libxc-retry-shadow-ops-if-EBUSY-is-returned.patch
Patch257: avoid-gnt-unmap-tlb-flush-if-not-accessed.patch
Patch258: 0002-x86-boot-reloc-create-generic-alloc-and-copy-functio.patch
Patch259: 0003-x86-boot-use-ecx-instead-of-eax.patch
Patch260: 0004-xen-x86-add-multiboot2-protocol-support.patch
Patch261: 0005-efi-split-efi_enabled-to-efi_platform-and-efi_loader.patch
Patch262: 0007-efi-run-EFI-specific-code-on-EFI-platform-only.patch
Patch263: 0008-efi-build-xen.gz-with-EFI-code.patch
Patch264: 0017-x86-efi-create-new-early-memory-allocator.patch
Patch265: 0018-x86-add-multiboot2-protocol-support-for-EFI-platform.patch
Patch266: mkelf32-fixup.patch
Patch267: 0001-x86-efi-Find-memory-for-trampoline-relocation-if-nec.patch
Patch268: 0002-efi-Ensure-incorrectly-typed-runtime-services-get-ma.patch
Patch269: 0001-Fix-compilation-on-CentOS-7.1.patch
Patch270: 0001-x86-time-Don-t-use-EFI-s-GetTime-call.patch
Patch271: 0001-efi-Workaround-page-fault-during-runtime-service.patch
Patch272: efi-align-stack.patch
Patch273: 0001-x86-HVM-Avoid-cache-flush-operations-during-hvm_load.patch
Patch274: 0001-libxl-Don-t-insert-PCI-device-into-xenstore-for-HVM-.patch
Patch275: 0001-x86-PoD-Command-line-option-to-prohibit-any-PoD-oper.patch
Patch276: 0001-libxl-handle-an-INVALID-domain-when-removing-a-pci-d.patch
Patch277: fail-on-duplicate-symbol.patch
Patch278: livepatch-ignore-duplicate-new.patch
Patch279: default-log-level-info.patch
Patch280: livepach-Add-.livepatch.hooks-functions-and-test-cas.patch
Patch281: 0001-lib-Add-a-generic-implementation-of-current_text_add.patch
Patch282: 0002-sched-Remove-dependency-on-__LINE__-for-release-buil.patch
Patch283: 0001-tools-livepatch-Show-the-correct-expected-state-befo.patch
Patch284: 0002-tools-livepatch-Set-stdout-and-stderr-unbuffered.patch
Patch285: 0003-tools-livepatch-Improve-output.patch
Patch286: 0004-livepatch-Set-timeout-unit-to-nanoseconds.patch
Patch287: 0005-tools-livepatch-Remove-pointless-retry-loop.patch
Patch288: 0006-tools-livepatch-Remove-unused-struct-member.patch
Patch289: 0007-tools-livepatch-Exit-with-2-if-a-timeout-occurs.patch
Patch290: pygrub-Ignore-GRUB2-if-statements.patch
Patch291: libfsimage-Add-support-for-btrfs.patch
Patch292: 0001-xen-domctl-Implement-a-way-to-retrieve-a-domains-nom.patch
Patch293: quiet-broke-irq-affinity.patch
Patch294: quirk-intel-purley.patch
Patch295: xsa226-cmdline-options.patch
Patch296: 0001-Kconfig-add-BROKEN-config.patch
Patch297: 0002-xen-delete-gcno-files-in-clean-target.patch
Patch298: 0003-xen-tools-rip-out-old-gcov-implementation.patch
Patch299: 0004-gcov-add-new-interface-and-new-formats-support.patch
Patch300: 0005-gcov-userspace-tools-to-extract-and-split-gcov-data.patch
Patch301: 0006-Config.mk-expand-cc-ver-a-bit.patch
Patch302: 0007-Config.mk-introduce-cc-ifversion.patch
Patch303: 0008-gcov-provide-the-capability-to-select-gcov-format-au.patch
Patch304: 0009-flask-add-gcov_op-check.patch
Patch305: 0001-x86-vvmx-set-CR4-before-CR0.patch
Patch306: 0001-x86-msr-Blacklist-various-MSRs-which-guests-definite.patch
Patch307: 0004-x86-cpuid-Enable-new-SSE-AVX-AVX512-cpu-features.patch
Patch308: 0001-Hide-AVX-512-from-guests-by-default.patch
Patch309: 0001-xen-xsm-Rename-CONFIG_FLASK_-to-CONFIG_XSM_FLASK_.patch
Patch310: 0002-xen-xsm-Rename-CONIFIG_XSM_POLICY-to-CONFIG_XSM_FLAS.patch
Patch311: 0003-xen-xsm-Introduce-new-boot-parameter-xsm.patch
Patch312: 0004-xen-xsm-Add-new-SILO-mode-for-XSM.patch
Patch313: xen-tweak-cmdline-defaults.patch
Patch314: xen-tweak-debug-overhead.patch
Patch315: tweak-iommu-errata-policy.patch
Patch316: disable-core-parking.patch
Patch317: disable-runtime-microcode.patch
Patch318: 0001-firmware-hvmloader-save-final-MMIO-hole-size-for-the.patch
Patch319: xen-legacy-win-driver-version.patch
Patch320: xen-legacy-win-xenmapspace-quirks.patch
Patch321: xen-legacy-32bit_shinfo.patch
Patch322: xen-legacy-process-dying.patch
Patch323: xen-legacy-viridian-hypercalls.patch
Patch324: xen-legacy-hvm-console.patch
Patch325: livepatch-payload-in-header.patch
Patch326: xen-define-offsets-for-kdump.patch
Patch327: xen-scheduler-auto-privdom-weight.patch
Patch328: xen-hvm-disable-tsc-ramping.patch
Patch329: xen-default-cpufreq-governor-to-performance-on-intel.patch
Patch330: xen-override-caching-cp-26562.patch
Patch331: revert-ca2eee92df44.patch
Patch332: libxc-stubs-hvm_check_pvdriver.patch
Patch333: restrict-privcmd.patch
Patch334: pygrub-add-default-and-extra-args.patch
Patch335: pygrub-always-boot-default.patch
Patch336: pygrub-friendly-no-fs.patch
Patch337: pygrub-image-max-size.patch
Patch338: pygrub-default-xenmobile-kernel.patch
Patch339: pygrub-blacklist-support.patch
Patch340: oem-bios-xensource.patch
Patch341: oem-bios-magic-from-xenstore.patch
Patch342: misc-log-guest-consoles.patch
Patch343: fix-ocaml-libs.patch
Patch344: ocaml-cpuid-helpers.patch
Patch345: xentop-display-correct-stats.patch
Patch346: xentop-vbd3.patch
Patch347: mixed-domain-runstates.patch
Patch348: mixed-xc-sockets-per-core.patch
Patch349: xenguest.patch
Patch350: xen-vmdebug.patch
Patch351: local-xen-vmdebug.patch
Patch352: oxenstore-update.patch
Patch353: oxenstore-censor-sensitive-data.patch
Patch354: oxenstore-large-packets.patch
Patch355: nvidia-vga.patch
Patch356: hvmloader-disable-pci-option-rom-loading.patch
Patch357: xen-force-software-vmcs-shadow.patch
Patch358: 0001-x86-vvmx-add-initial-PV-EPT-support-in-L0.patch
Patch359: add-p2m-write-dm-to-ram-types.patch
Patch360: add-pv-iommu-headers.patch
Patch361: add-iommu-lookup-core.patch
Patch362: add-iommu-lookup-intel.patch
Patch363: add-pv-iommu-local-domain-ops.patch
Patch364: add-pv-iommu-foreign-support.patch
Patch365: add-pv-iommu-premap-m2b-support.patch
Patch366: add-pv-iommu-to-spec.patch
Patch367: upstream-pv-iommu-tools.patch
Patch368: allow-rombios-pci-config-on-any-host-bridge.patch
Patch369: 0007-hypercall-XENMEM_get_mfn_from_pfn.patch
Patch370: 0012-resize-MAX_NR_IO_RANGES-to-512.patch
Patch371: 0015-xen-introduce-unlimited-rangeset.patch
Patch372: 0016-ioreq-server-allocate-unlimited-rangeset-for-memory-.patch
Patch373: gvt-g-hvmloader+rombios.patch
Patch374: revert-c858e932c1dd.patch
Patch375: xen-introduce-cmdline-to-control-introspection-extensions.patch
Patch376: xen-domctl-set-privileged-domain.patch
Patch377: xen-x86-hvm-Allow-guest_request-vm_events-coming-from-us.patch
Patch378: x86-domctl-Don-t-pause-the-whole-domain-if-only-gett.patch
Patch379: xen-reexecute-instn-under-monitor-trap.patch
Patch380: xen-x86-emulate-syncrhonise-LOCKed-instruction-emulation.patch
Patch381: xen-emulate-Bypass-the-emulator-if-emulation-fails.patch
Patch382: xen-introspection-pause.patch
Patch383: xen-introspection-elide-cr4-pge.patch
Patch384: xen-xsm-default-policy.patch
Patch385: xen-xsm-allow-access-unlabeled-resources.patch
Patch386: xen-xsm-treat-unlabeled-domain-domU.patch
Patch387: 0001-cc-memory-scrubbing.patch
Patch388: xsa278-4.7.patch
Source1: sysconfig_kernel-xen
Source2: xl.conf
Source3: logrotate-xen-tools
#Patch0:  xen-development.patch

ExclusiveArch: i686 x86_64

#Cross complier
%ifarch %ix86
BuildRequires: gcc-x86_64-linux-gnu binutils-x86_64-linux-gnu
%endif

BuildRequires: gcc-xs

# For HVMLoader and 16/32bit firmware
BuildRequires: /usr/include/gnu/stubs-32.h
BuildRequires: dev86 iasl

# For the domain builder (decompression and hashing)
BuildRequires: zlib-devel bzip2-devel xz-devel
BuildRequires: openssl-devel

# For libxl
BuildRequires: yajl-devel libuuid-devel perl

# For python stubs
BuildRequires: python-devel

# For ocaml stubs
BuildRequires: ocaml ocaml-findlib

# For ipxe
BuildRequires: ipxe-source

BuildRequires: libblkid-devel

# For xentop
BuildRequires: ncurses-devel

# For the banner
BuildRequires: figlet

# For libfsimage
BuildRequires: e2fsprogs-devel
%if 0%{?centos}%{!?centos:5} < 6 && 0%{?rhel}%{!?rhel:5} < 6
#libext4fs
BuildRequires: e4fsprogs-devel
%endif
BuildRequires: lzo-devel

# For xenguest
BuildRequires: json-c-devel libempserver-devel

# Misc
BuildRequires: libtool
%if %with_systemd
BuildRequires: systemd-devel
%endif

# To placate ./configure
BuildRequires: gettext-devel glib2-devel curl-devel gnutls-devel

%description
Xen Hypervisor.

%package hypervisor
Summary: The Xen Hypervisor
Group: System/Hypervisor
Requires(post): coreutils grep
%description hypervisor
This package contains the Xen Project Hypervisor.

%package hypervisor-debuginfo
Summary: The Xen Hypervisor debug information
Group: Development/Debug
%description hypervisor-debuginfo
This package contains the Xen Hypervisor debug information.

%package tools
Summary: Xen Hypervisor general tools
Requires: xen-libs = %{version}
Group: System/Base
%description tools
This package contains the Xen Hypervisor general tools for all domains.

%package devel
Summary: The Xen Hypervisor public headers
Group: Development/Libraries
%description devel
This package contains the Xen Hypervisor public header files.

%package libs
Summary: Xen Hypervisor general libraries
Group: System/Libraries
%description libs
This package contains the Xen Hypervisor general libraries for all domains.

%package libs-devel
Summary: Xen Hypervisor general development libraries
Requires: xen-libs = %{version}
Requires: xen-devel = %{version}
Group: Development/Libraries
%description libs-devel
This package contains the Xen Hypervisor general development for all domains.

%package dom0-tools
Summary: Xen Hypervisor Domain 0 tools
Requires: xen-dom0-libs = %{version}
Requires: xen-tools = %{version}
%if %with_systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
%endif
Group: System/Base
%description dom0-tools
This package contains the Xen Hypervisor control domain tools.

%package dom0-libs
Summary: Xen Hypervisor Domain 0 libraries
Requires: xen-hypervisor = %{version}
Group: System/Libraries
%description dom0-libs
This package contains the Xen Hypervisor control domain libraries.

%package dom0-libs-devel
Summary: Xen Hypervisor Domain 0 headers
Requires: xen-devel = %{version}
Requires: xen-dom0-libs = %{version}

# Temp until the build dependencies are properly propagated
Provides: xen-dom0-devel = %{version}
Group: Development/Libraries
%description dom0-libs-devel
This package contains the Xen Hypervisor control domain headers.

%package ocaml-libs
Summary: Xen Hypervisor ocaml libraries
Requires: xen-dom0-libs = %{version}
Group: System/Libraries
%description ocaml-libs
This package contains the Xen Hypervisor ocaml libraries.

%package ocaml-devel
Summary: Xen Hypervisor ocaml headers
Requires: xen-ocaml-libs = %{version}
Requires: xen-dom0-libs-devel = %{version}
Group: Development/Libraries
%description ocaml-devel
This package contains the Xen Hypervisor ocaml headers.

%package installer-files
Summary: Xen files for the XenServer installer
Group: System Environment/Base
%description installer-files
This package contains the minimal subset of libraries and binaries required in
the XenServer installer environment.

%prep
%autosetup -p1

mkdir -p tools/firmware/etherboot/ipxe/
cp /usr/src/ipxe-source.tar.gz tools/firmware/etherboot/ipxe.tar.gz
rm -f tools/firmware/etherboot/patches/series
#%patch0 -p1 -b ~development
base_cset=$(sed -ne 's/Changeset: \(.*\)/\1/p' < .gitarchive-info)
pq_cset=$(sed -ne 's/Changeset: \(.*\)/\1/p' < .gitarchive-info-pq)
echo "${base_cset:0:12}, pq ${pq_cset:0:12}" > .scmversion

%build

# Placate ./configure, but don't pull in external content.
export WGET=/bin/false FETCHER=/bin/false

%configure \
        --disable-seabios --disable-stubdom --disable-xsmpolicy --disable-blktap2 \
	--with-system-qemu=%{_libdir}/xen/bin/qemu-system-i386 --with-xenstored=oxenstored \
	--enable-systemd

%install

# The existence of this directory causes ocamlfind to put things in it
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs

mkdir -p %{buildroot}/boot/

# Regular build of Xen
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release} \
    KCONFIG_CONFIG=../buildconfigs/config-release olddefconfig
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release} \
    KCONFIG_CONFIG=../buildconfigs/config-release build
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release} \
    KCONFIG_CONFIG=../buildconfigs/config-release MAP

cp xen/xen.gz %{buildroot}/boot/%{name}-%{version}-%{release}.gz
cp xen/System.map %{buildroot}/boot/%{name}-%{version}-%{release}.map
cp xen/xen-syms %{buildroot}/boot/%{name}-syms-%{version}-%{release}
cp buildconfigs/config-release %{buildroot}/boot/%{name}-%{version}-%{release}.config

# Debug build of Xen
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen clean
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release}-d \
    KCONFIG_CONFIG=../buildconfigs/config-debug olddefconfig
PATH=/opt/xensource/gcc/bin:$PATH %{?cov_wrap} %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release}-d \
    KCONFIG_CONFIG=../buildconfigs/config-debug build
PATH=/opt/xensource/gcc/bin:$PATH %{__make} %{HVSOR_OPTIONS} -C xen XEN_VENDORVERSION=-%{release}-d \
    KCONFIG_CONFIG=../buildconfigs/config-debug MAP

cp xen/xen.gz %{buildroot}/boot/%{name}-%{version}-%{release}-d.gz
cp xen/System.map %{buildroot}/boot/%{name}-%{version}-%{release}-d.map
cp xen/xen-syms %{buildroot}/boot/%{name}-syms-%{version}-%{release}-d
cp buildconfigs/config-debug %{buildroot}/boot/%{name}-%{version}-%{release}-d.config

# do not strip the hypervisor-debuginfo targerts
chmod -x %{buildroot}/boot/xen-syms-*

# Build tools and man pages
%{?cov_wrap} %{__make} %{TOOLS_OPTIONS} -C tools install
%{__make} %{TOOLS_OPTIONS} -C docs install-man-pages
%{?cov_wrap} %{__make} %{TOOLS_OPTIONS} -C tools/tests/mce-test/tools install

%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/kernel-xen
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xen/xl.conf
%{__install} -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/xen-tools

%files hypervisor
/boot/%{name}-%{version}-%{release}.gz
/boot/%{name}-%{version}-%{release}.map
/boot/%{name}-%{version}-%{release}.config
/boot/%{name}-%{version}-%{release}-d.gz
/boot/%{name}-%{version}-%{release}-d.map
/boot/%{name}-%{version}-%{release}-d.config
%config %{_sysconfdir}/sysconfig/kernel-xen
%ghost %attr(0644,root,root) %{_sysconfdir}/sysconfig/kernel-xen-args

%files hypervisor-debuginfo
/boot/%{name}-syms-%{version}-%{release}
/boot/%{name}-syms-%{version}-%{release}-d

%files tools
%{_bindir}/xenstore
%{_bindir}/xenstore-chmod
%{_bindir}/xenstore-control
%{_bindir}/xenstore-exists
%{_bindir}/xenstore-list
%{_bindir}/xenstore-ls
%{_bindir}/xenstore-read
%{_bindir}/xenstore-rm
%{_bindir}/xenstore-watch
%{_bindir}/xenstore-write
%{python_sitearch}/%{name}/__init__.py*
%{python_sitearch}/%{name}/lowlevel/__init__.py*
%{python_sitearch}/%{name}/lowlevel/xs.so

%files devel
%{_includedir}/%{name}/COPYING
%{_includedir}/%{name}/arch-arm.h
%{_includedir}/%{name}/arch-arm/hvm/save.h
%{_includedir}/%{name}/arch-x86/cpuid.h
%{_includedir}/%{name}/arch-x86/cpufeatureset.h
%{_includedir}/%{name}/arch-x86/hvm/save.h
%{_includedir}/%{name}/arch-x86/pmu.h
%{_includedir}/%{name}/arch-x86/xen-mca.h
%{_includedir}/%{name}/arch-x86/xen-x86_32.h
%{_includedir}/%{name}/arch-x86/xen-x86_64.h
%{_includedir}/%{name}/arch-x86/xen.h
%{_includedir}/%{name}/arch-x86_32.h
%{_includedir}/%{name}/arch-x86_64.h
%{_includedir}/%{name}/callback.h
%{_includedir}/%{name}/dom0_ops.h
%{_includedir}/%{name}/domctl.h
%{_includedir}/%{name}/elfnote.h
%{_includedir}/%{name}/errno.h
%{_includedir}/%{name}/event_channel.h
%{_includedir}/%{name}/features.h
%{_includedir}/%{name}/foreign/arm32.h
%{_includedir}/%{name}/foreign/arm64.h
%{_includedir}/%{name}/foreign/x86_32.h
%{_includedir}/%{name}/foreign/x86_64.h
%{_includedir}/%{name}/grant_table.h
%{_includedir}/%{name}/hvm/dm_op.h
%{_includedir}/%{name}/hvm/e820.h
%{_includedir}/%{name}/hvm/hvm_info_table.h
%{_includedir}/%{name}/hvm/hvm_op.h
%{_includedir}/%{name}/hvm/hvm_vcpu.h
%{_includedir}/%{name}/hvm/hvm_xs_strings.h
%{_includedir}/%{name}/hvm/ioreq.h
%{_includedir}/%{name}/hvm/params.h
%{_includedir}/%{name}/hvm/pvdrivers.h
%{_includedir}/%{name}/hvm/save.h
%{_includedir}/%{name}/io/blkif.h
%{_includedir}/%{name}/io/console.h
%{_includedir}/%{name}/io/fbif.h
%{_includedir}/%{name}/io/fsif.h
%{_includedir}/%{name}/io/kbdif.h
%{_includedir}/%{name}/io/libxenvchan.h
%{_includedir}/%{name}/io/netif.h
%{_includedir}/%{name}/io/pciif.h
%{_includedir}/%{name}/io/protocols.h
%{_includedir}/%{name}/io/ring.h
%{_includedir}/%{name}/io/tpmif.h
%{_includedir}/%{name}/io/usbif.h
%{_includedir}/%{name}/io/vscsiif.h
%{_includedir}/%{name}/io/xenbus.h
%{_includedir}/%{name}/io/xs_wire.h
%{_includedir}/%{name}/kexec.h
%{_includedir}/%{name}/memory.h
%{_includedir}/%{name}/nmi.h
%{_includedir}/%{name}/physdev.h
%{_includedir}/%{name}/platform.h
%{_includedir}/%{name}/pmu.h
%{_includedir}/%{name}/pv-iommu.h
%{_includedir}/%{name}/sched.h
%{_includedir}/%{name}/sys/evtchn.h
%{_includedir}/%{name}/sys/gntalloc.h
%{_includedir}/%{name}/sys/gntdev.h
%{_includedir}/%{name}/sys/privcmd.h
%{_includedir}/%{name}/sys/xenbus_dev.h
%{_includedir}/%{name}/sysctl.h
%{_includedir}/%{name}/tmem.h
%{_includedir}/%{name}/trace.h
%{_includedir}/%{name}/vcpu.h
%{_includedir}/%{name}/version.h
%{_includedir}/%{name}/vm_event.h
%{_includedir}/%{name}/xen-compat.h
%{_includedir}/%{name}/xen.h
%{_includedir}/%{name}/xencomm.h
%{_includedir}/%{name}/xenoprof.h
%{_includedir}/%{name}/xsm/flask_op.h

%files libs
%{_libdir}/libxenevtchn.so.1
%{_libdir}/libxenevtchn.so.1.1
%{_libdir}/libxengnttab.so.1
%{_libdir}/libxengnttab.so.1.1
%{_libdir}/libxenstore.so.3.0
%{_libdir}/libxenstore.so.3.0.3
%{_libdir}/libxentoolcore.so.1
%{_libdir}/libxentoolcore.so.1.0
%{_libdir}/libxenvchan.so.4.7
%{_libdir}/libxenvchan.so.4.7.0

%files libs-devel
# Lib Xen Evtchn
%{_includedir}/xenevtchn.h
%{_libdir}/libxenevtchn.a
%{_libdir}/libxenevtchn.so

# Lib Xen Gnttab
%{_includedir}/xengnttab.h
%{_libdir}/libxengnttab.a
%{_libdir}/libxengnttab.so

# Lib XenStore
%{_includedir}/xenstore.h
%{_includedir}/xenstore_lib.h
%{_libdir}/libxenstore.a
%{_libdir}/libxenstore.so
# Legacy XenStore header files, excluded to discourage their use
%exclude %{_includedir}/xs.h
%exclude %{_includedir}/xenstore-compat/xs.h
%exclude %{_includedir}/xs_lib.h
%exclude %{_includedir}/xenstore-compat/xs_lib.h

%{_includedir}/xentoolcore.h
%{_libdir}/libxentoolcore.a
%{_libdir}/libxentoolcore.so

# Lib Xen Vchan
%{_includedir}/libxenvchan.h
%{_libdir}/libxenvchan.a
%{_libdir}/libxenvchan.so

%files dom0-tools
%{_sysconfdir}/bash_completion.d/xl.sh
%exclude %{_sysconfdir}/rc.d/init.d/xencommons
%exclude %{_sysconfdir}/rc.d/init.d/xendomains
%exclude %{_sysconfdir}/rc.d/init.d/xendriverdomain
%exclude %{_sysconfdir}/sysconfig/xendomains
%if %with_systemd
%exclude %{_sysconfdir}/rc.d/init.d/xen-watchdog
%else
%{_sysconfdir}/rc.d/init.d/xen-watchdog
%endif
%config %{_sysconfdir}/logrotate.d/xen-tools
%config %{_sysconfdir}/sysconfig/xencommons
%config %{_sysconfdir}/xen/oxenstored.conf
%{_sysconfdir}/xen/scripts/block
%{_sysconfdir}/xen/scripts/block-common.sh
%{_sysconfdir}/xen/scripts/block-drbd-probe
%{_sysconfdir}/xen/scripts/block-dummy
%{_sysconfdir}/xen/scripts/block-enbd
%{_sysconfdir}/xen/scripts/block-iscsi
%{_sysconfdir}/xen/scripts/block-nbd
%{_sysconfdir}/xen/scripts/block-tap
%{_sysconfdir}/xen/scripts/colo-proxy-setup
%{_sysconfdir}/xen/scripts/external-device-migrate
%{_sysconfdir}/xen/scripts/hotplugpath.sh
%{_sysconfdir}/xen/scripts/locking.sh
%{_sysconfdir}/xen/scripts/logging.sh
%{_sysconfdir}/xen/scripts/vif-bridge
%{_sysconfdir}/xen/scripts/vif-common.sh
%{_sysconfdir}/xen/scripts/vif-nat
%{_sysconfdir}/xen/scripts/vif-openvswitch
%{_sysconfdir}/xen/scripts/vif-route
%{_sysconfdir}/xen/scripts/vif-setup
%{_sysconfdir}/xen/scripts/vif2
%{_sysconfdir}/xen/scripts/vscsi
%{_sysconfdir}/xen/scripts/xen-hotplug-cleanup
%{_sysconfdir}/xen/scripts/xen-hotplug-common.sh
%{_sysconfdir}/xen/scripts/xen-network-common.sh
%{_sysconfdir}/xen/scripts/xen-script-common.sh
%exclude %{_sysconfdir}/%{name}/cpupool
%exclude %{_sysconfdir}/%{name}/README
%exclude %{_sysconfdir}/%{name}/README.incompatibilities
%exclude %{_sysconfdir}/%{name}/xlexample.hvm
%exclude %{_sysconfdir}/%{name}/xlexample.pvlinux
%config %{_sysconfdir}/xen/xl.conf
%{_bindir}/pygrub
%{_bindir}/xen-cpuid
%{_bindir}/xen-detect
%{_bindir}/xenalyze
%{_bindir}/xencons
%{_bindir}/xencov_split
%{_bindir}/xentrace_format
%{python_sitearch}/fsimage.so
%{python_sitearch}/grub/ExtLinuxConf.py*
%{python_sitearch}/grub/GrubConf.py*
%{python_sitearch}/grub/LiloConf.py*
%{python_sitearch}/grub/__init__.py*
%{python_sitearch}/pygrub-*.egg-info
%{python_sitearch}/xen-*.egg-info
#{python_sitearch}/xen/__init__.py*           - Must not duplicate xen-tools
#{python_sitearch}/xen/lowlevel/__init__.py*  - Must not duplicate xen-tools
%{python_sitearch}/xen/lowlevel/xc.so
%{python_sitearch}/xen/migration/__init__.py*
%{python_sitearch}/xen/migration/legacy.py*
%{python_sitearch}/xen/migration/libxc.py*
%{python_sitearch}/xen/migration/libxl.py*
%{python_sitearch}/xen/migration/public.py*
%{python_sitearch}/xen/migration/tests.py*
%{python_sitearch}/xen/migration/verify.py*
%{python_sitearch}/xen/migration/xl.py*
%{_libexecdir}/%{name}/bin/convert-legacy-stream
%{_libexecdir}/%{name}/bin/init-xenstore-domain
%{_libexecdir}/%{name}/bin/libxl-save-helper
%{_libexecdir}/%{name}/bin/lsevtchn
%{_libexecdir}/%{name}/bin/pygrub
%{_libexecdir}/%{name}/bin/readnotes
%{_libexecdir}/%{name}/bin/verify-stream-v2
%{_libexecdir}/%{name}/bin/xen-init-dom0
%{_libexecdir}/%{name}/bin/xenconsole
%{_libexecdir}/%{name}/bin/xenctx
%{_libexecdir}/%{name}/bin/xendomains
%{_libexecdir}/%{name}/bin/xenguest
%{_libexecdir}/%{name}/bin/xenpaging
%{_libexecdir}/%{name}/bin/xenpvnetboot
%{_libexecdir}/%{name}/boot/hvmloader
%{_sbindir}/flask-get-bool
%{_sbindir}/flask-getenforce
%{_sbindir}/flask-label-pci
%{_sbindir}/flask-loadpolicy
%{_sbindir}/flask-set-bool
%{_sbindir}/flask-setenforce
%{_sbindir}/gdbsx
%{_sbindir}/kdd
%{_sbindir}/oxenstored
%{_sbindir}/xen-hptool
%{_sbindir}/xen-hvmcrash
%{_sbindir}/xen-hvmctx
%{_sbindir}/xen-livepatch
%{_sbindir}/xen-lowmemd
%{_sbindir}/xen-mceinj
%{_sbindir}/xen-mfndump
%exclude %{_sbindir}/xen-ringwatch
%{_sbindir}/xen-vmdebug
%{_sbindir}/xenbaked
%{_sbindir}/xenconsoled
%{_sbindir}/xencov
%{_sbindir}/xenmon.py
%{_sbindir}/xenperf
%{_sbindir}/xenpm
%{_sbindir}/xenpmd
%{_sbindir}/xenstored
%{_sbindir}/xentop
%{_sbindir}/xentrace
%{_sbindir}/xentrace_setmask
%{_sbindir}/xentrace_setsize
%{_sbindir}/xenwatchdogd
%{_sbindir}/xl
%exclude %{_sbindir}/gtracestat
%exclude %{_sbindir}/gtraceview
%exclude %{_sbindir}/xen-bugtool
%exclude %{_sbindir}/xen-tmem-list-parse
%exclude %{_sbindir}/xenlockprof
%{_mandir}/man1/xentop.1.gz
%{_mandir}/man1/xentrace_format.1.gz
%{_mandir}/man1/xenstore-chmod.1.gz
%{_mandir}/man1/xenstore-ls.1.gz
%{_mandir}/man1/xenstore.1.gz
%{_mandir}/man1/xl.1.gz
%{_mandir}/man5/xl.cfg.5.gz
%{_mandir}/man5/xl.conf.5.gz
%{_mandir}/man5/xlcpupool.cfg.5.gz
%{_mandir}/man8/xentrace.8.gz
%dir /var/lib/xen
%dir /var/log/xen
%if %with_systemd
%{_unitdir}/proc-xen.mount
%{_unitdir}/var-lib-xenstored.mount
%{_unitdir}/xen-init-dom0.service
%{_unitdir}/xen-watchdog.service
%{_unitdir}/xenconsoled.service
%{_unitdir}/xenstored.service
%{_unitdir}/xenstored.socket
%{_unitdir}/xenstored_ro.socket
%exclude %{_prefix}/lib/modules-load.d/xen.conf
%exclude %{_unitdir}/xen-qemu-dom0-disk-backend.service
%exclude %{_unitdir}/xendomains.service
%endif

%files dom0-libs
%{_libdir}/fs/btrfs/fsimage.so
%{_libdir}/fs/ext2fs-lib/fsimage.so
%{_libdir}/fs/fat/fsimage.so
%{_libdir}/fs/iso9660/fsimage.so
%{_libdir}/fs/reiserfs/fsimage.so
%{_libdir}/fs/ufs/fsimage.so
%{_libdir}/fs/xfs/fsimage.so
%{_libdir}/fs/zfs/fsimage.so
%{_libdir}/libfsimage.so.1.0
%{_libdir}/libfsimage.so.1.0.0
%{_libdir}/libxencall.so.1
%{_libdir}/libxencall.so.1.0
%{_libdir}/libxenctrl.so.4.7
%{_libdir}/libxenctrl.so.4.7.0
%{_libdir}/libxendevicemodel.so.1
%{_libdir}/libxendevicemodel.so.1.2
%{_libdir}/libxenforeignmemory.so.1
%{_libdir}/libxenforeignmemory.so.1.2
%{_libdir}/libxenguest.so.4.7
%{_libdir}/libxenguest.so.4.7.0
%{_libdir}/libxenlight.so.4.7
%{_libdir}/libxenlight.so.4.7.0
%{_libdir}/libxenstat.so.0
%{_libdir}/libxenstat.so.0.0
%{_libdir}/libxentoollog.so.1
%{_libdir}/libxentoollog.so.1.0
%{_libdir}/libxlutil.so.4.7
%{_libdir}/libxlutil.so.4.7.0

%files dom0-libs-devel
%{_includedir}/fsimage.h
%{_includedir}/fsimage_grub.h
%{_includedir}/fsimage_plugin.h
%{_libdir}/libfsimage.so

%{_includedir}/xencall.h
%{_libdir}/libxencall.a
%{_libdir}/libxencall.so

%{_includedir}/xenctrl.h
%{_includedir}/xenctrl_compat.h
%{_libdir}/libxenctrl.a
%{_libdir}/libxenctrl.so

%{_includedir}/xendevicemodel.h
%{_libdir}/libxendevicemodel.a
%{_libdir}/libxendevicemodel.so

%{_includedir}/xenforeignmemory.h
%{_libdir}/libxenforeignmemory.a
%{_libdir}/libxenforeignmemory.so

%{_includedir}/xenguest.h
%{_libdir}/libxenguest.a
%{_libdir}/libxenguest.so

%{_includedir}/xentoollog.h
%{_libdir}/libxentoollog.a
%{_libdir}/libxentoollog.so

%{_includedir}/_libxl_list.h
%{_includedir}/_libxl_types.h
%{_includedir}/_libxl_types_json.h
%{_includedir}/libxl.h
%{_includedir}/libxl_event.h
%{_includedir}/libxl_json.h
%{_includedir}/libxl_utils.h
%{_includedir}/libxl_uuid.h
%{_includedir}/libxlutil.h
%{_libdir}/libxenlight.a
%{_libdir}/libxenlight.so
%{_libdir}/libxlutil.a
%{_libdir}/libxlutil.so
/usr/share/pkgconfig/xenlight.pc
/usr/share/pkgconfig/xlutil.pc

%{_includedir}/xenstat.h
%{_libdir}/libxenstat.a
%{_libdir}/libxenstat.so

%files ocaml-libs
%{_libdir}/ocaml/stublibs/dllxenbus_stubs.so
%{_libdir}/ocaml/stublibs/dllxenbus_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so
%{_libdir}/ocaml/stublibs/dllxenctrl_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxeneventchn_stubs.so
%{_libdir}/ocaml/stublibs/dllxeneventchn_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so
%{_libdir}/ocaml/stublibs/dllxenlight_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxenmmap_stubs.so
%{_libdir}/ocaml/stublibs/dllxenmmap_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so
%{_libdir}/ocaml/stublibs/dllxentoollog_stubs.so.owner
%{_libdir}/ocaml/xenbus/META
%{_libdir}/ocaml/xenbus/xenbus.cma
%{_libdir}/ocaml/xenbus/xenbus.cmo
%{_libdir}/ocaml/xenctrl/META
%{_libdir}/ocaml/xenctrl/xenctrl.cma
%{_libdir}/ocaml/xeneventchn/META
%{_libdir}/ocaml/xeneventchn/xeneventchn.cma
%{_libdir}/ocaml/xenlight/META
%{_libdir}/ocaml/xenlight/xenlight.cma
%{_libdir}/ocaml/xenmmap/META
%{_libdir}/ocaml/xenmmap/xenmmap.cma
%exclude %{_libdir}/ocaml/xenstore/META
%exclude %{_libdir}/ocaml/xenstore/xenstore.cma
%exclude %{_libdir}/ocaml/xenstore/xenstore.cmo
%{_libdir}/ocaml/xentoollog/META
%{_libdir}/ocaml/xentoollog/xentoollog.cma

%files ocaml-devel
%{_libdir}/ocaml/xenbus/libxenbus_stubs.a
%{_libdir}/ocaml/xenbus/xenbus.a
%{_libdir}/ocaml/xenbus/xenbus.cmi
%{_libdir}/ocaml/xenbus/xenbus.cmx
%{_libdir}/ocaml/xenbus/xenbus.cmxa
%{_libdir}/ocaml/xenctrl/libxenctrl_stubs.a
%{_libdir}/ocaml/xenctrl/xenctrl.a
%{_libdir}/ocaml/xenctrl/xenctrl.cmi
%{_libdir}/ocaml/xenctrl/xenctrl.cmx
%{_libdir}/ocaml/xenctrl/xenctrl.cmxa
%{_libdir}/ocaml/xeneventchn/libxeneventchn_stubs.a
%{_libdir}/ocaml/xeneventchn/xeneventchn.a
%{_libdir}/ocaml/xeneventchn/xeneventchn.cmi
%{_libdir}/ocaml/xeneventchn/xeneventchn.cmx
%{_libdir}/ocaml/xeneventchn/xeneventchn.cmxa
%{_libdir}/ocaml/xenlight/libxenlight_stubs.a
%{_libdir}/ocaml/xenlight/xenlight.a
%{_libdir}/ocaml/xenlight/xenlight.cmi
%{_libdir}/ocaml/xenlight/xenlight.cmx
%{_libdir}/ocaml/xenlight/xenlight.cmxa
%{_libdir}/ocaml/xenmmap/libxenmmap_stubs.a
%{_libdir}/ocaml/xenmmap/xenmmap.a
%{_libdir}/ocaml/xenmmap/xenmmap.cmi
%{_libdir}/ocaml/xenmmap/xenmmap.cmx
%{_libdir}/ocaml/xenmmap/xenmmap.cmxa
%exclude %{_libdir}/ocaml/xenstore/xenstore.a
%exclude %{_libdir}/ocaml/xenstore/xenstore.cmi
%exclude %{_libdir}/ocaml/xenstore/xenstore.cmx
%exclude %{_libdir}/ocaml/xenstore/xenstore.cmxa
%{_libdir}/ocaml/xentoollog/libxentoollog_stubs.a
%{_libdir}/ocaml/xentoollog/xentoollog.a
%{_libdir}/ocaml/xentoollog/xentoollog.cmi
%{_libdir}/ocaml/xentoollog/xentoollog.cmx
%{_libdir}/ocaml/xentoollog/xentoollog.cmxa

%files installer-files
%{_libdir}/libxenctrl.so.4.7
%{_libdir}/libxenctrl.so.4.7.0
%{_libdir}/libxenguest.so.4.7
%{_libdir}/libxenguest.so.4.7.0
%{python_sitearch}/xen/__init__.py*
%{python_sitearch}/xen/lowlevel/__init__.py*
%{python_sitearch}/xen/lowlevel/xc.so

%doc

%post hypervisor
# Update the debug and release symlinks
ln -sf %{name}-%{version}-%{release}-d.gz /boot/xen-debug.gz
ln -sf %{name}-%{version}-%{release}.gz /boot/xen-release.gz

# Point /boot/xen.gz appropriately
if [ ! -e /boot/xen.gz ]; then
%if %{default_debug_hypervisor}
    # Use a debug hypervisor by default
    ln -sf %{name}-%{version}-%{release}-d.gz /boot/xen.gz
%else
    # Use a production hypervisor by default
    ln -sf %{name}-%{version}-%{release}.gz /boot/xen.gz
%endif
else
    # Else look at the current link, and whether it is debug
    path="`readlink -f /boot/xen.gz`"
    if [ ${path} != ${path%%-d.gz} ]; then
        ln -sf %{name}-%{version}-%{release}-d.gz /boot/xen.gz
    else
        ln -sf %{name}-%{version}-%{release}.gz /boot/xen.gz
    fi
fi

if [ -e %{_sysconfdir}/sysconfig/kernel ] && ! grep -q '^HYPERVISOR' %{_sysconfdir}/sysconfig/kernel ; then
  cat %{_sysconfdir}/sysconfig/kernel-xen >> %{_sysconfdir}/sysconfig/kernel
fi

mkdir -p %{_rundir}/reboot-required.d/%{name}
touch %{_rundir}/reboot-required.d/%{name}/%{version}-%{release}

# Update grub.cfg to avoid Dom0 vCPU oversubscription

%triggerin hypervisor -- grub
if [ -e /boot/grub/grub.cfg ]; then
    sed -i 's/dom0_max_vcpus=\([0-9a-fA-FxX]\+\)\( \|$\)/dom0_max_vcpus=1-\1\2/g' /boot/grub/grub.cfg
fi

%triggerin hypervisor -- grub-efi
if [ -e /boot/efi/EFI/xenserver/grub.cfg ]; then
    sed -i 's/dom0_max_vcpus=\([0-9a-fA-FxX]\+\)\( \|$\)/dom0_max_vcpus=1-\1\2/g' /boot/efi/EFI/xenserver/grub.cfg
fi

%if %with_systemd
%post dom0-tools
%systemd_post proc-xen.mount
%systemd_post var-lib-xenstored.mount
%systemd_post xen-init-dom0.service
%systemd_post xen-watchdog.service
%systemd_post xenconsoled.service
%systemd_post xenstored.service
%systemd_post xenstored.socket
%systemd_post xenstored_ro.socket

%preun dom0-tools
%systemd_preun proc-xen.mount
%systemd_preun var-lib-xenstored.mount
%systemd_preun xen-init-dom0.service
%systemd_preun xen-watchdog.service
%systemd_preun xenconsoled.service
%systemd_preun xenstored.service
%systemd_preun xenstored.socket
%systemd_preun xenstored_ro.socket

%postun dom0-tools
%systemd_postun proc-xen.mount
%systemd_postun var-lib-xenstored.mount
%systemd_postun xen-init-dom0.service
%systemd_postun xen-watchdog.service
%systemd_postun xenconsoled.service
%systemd_postun xenstored.service
%systemd_postun xenstored.socket
%systemd_postun xenstored_ro.socket
%endif

%changelog
* Fri Oct 26 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 4.7.6-6.2.1.xcp
- Security update
- Fix CVE-2018-TBA: Nested VT-x usable even when disabled

* Thu Sep 13 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 4.7.6-6.1.1.xcp
- Update for XCP-ng 7.6

* Wed Aug 15 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 4.7.5-5.5.1xcp
- Multiple security updates

* Thu Aug 02 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 4.7.5-5.4.1xcp
- Security update
- Fix CVE-2018-12893: x86: #DB exception safety check can be triggered by a guest
- Fix CVE-2018-12891: preemption checks bypassed in x86 PV MM handling
