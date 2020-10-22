from part2 import *



def test_copy_efi_files():
    assert copy_efi_files() == True


def test_get_kernel():
    assert get_kernel() == True


def test_get_vmlinuz():
    assert get_vmlinuz() == True


def test_get_initramfs():
    assert get_initramfs() == True


def test_create_boot_target():
    assert create_boot_target() == True


def test_cleanup():
    assert cleanup() == True