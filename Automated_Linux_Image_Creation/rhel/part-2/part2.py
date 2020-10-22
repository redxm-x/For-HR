from code import *


def start():
    copy_efi_files()
    get_kernel()
    get_vmlinuz()
    get_initramfs()
    create_boot_target()
    cleanup()


start()
