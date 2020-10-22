import subprocess


def copy_efi_files():
    print('Copying files...')
    command = subprocess.run(['''cp /boot/initr* /efi/ && cp /boot/vmlinuz-* /efi/'''], shell= True)

    if command.returncode == 0:
        print('Files copied successfully!')
        result = True

    else:
        print('Files not copied!')
        result = False

    return result


def get_kernel():
    print('Saving kernel version for next step purposes...')
    command = subprocess.run(['''uname -r > /efi/kernel_version.txt'''], shell= True)

    if command.returncode == 0:
        print('Kernel version saved successfully!')
        result = True

    else:
        print('Could not save kernel!')
        result = False

    return result


def get_vmlinuz():
    print('Saving vmlinuz into vmlinuz.txt...')
    command = subprocess.run(['''find /boot/vmlinuz* > /efi/vmlinuz.txt'''], shell= True)

    if command.returncode == 0:
        print('Saved successfully!')
        result = True

    else:
        print('Not saved')
        result = False

    return result


def get_initramfs():
    print('Saving initramfs into initramfs.txt...')
    command = subprocess.run(['''find /boot/initramfs* > /efi/initramfs.txt'''], shell=True)
    if command.returncode == 0:
        print('Saved successfully!')
        result = True

    else:
        print('Not saved')
        result = False

    return result


def create_boot_target():
    print('Creating boot_target.nsh...')
    with open('/efi/kernel_version.txt', 'r') as file_0:
        kernel_version = file_0.readline().replace('\n', '')

    with open('/efi/vmlinuz.txt', 'r') as file_1:
        vmlinuz_list = list(file_1.readlines())

    with open('/efi/initramfs.txt', 'r') as file_2:
        initramfs_list = list(file_2.readlines())

    vmlinuz_string = ''.join([v for v in vmlinuz_list if kernel_version in v]).replace("'", "").strip()
    initramfs_string = ''.join([i for i in initramfs_list if kernel_version in i]).replace("'", "").strip()

    vmlinuz = f'{vmlinuz_string[6:]}'
    initramfs = f'{initramfs_string[6:]}'

    boot_target_nsh_string = f'fs0:\nfs0:\Shell.efi \EFI\{vmlinuz} initrd=\EFI\{initramfs} root=/dev/sda1 quiet showopts iomm=1 iomem=relaxed biosdevname=0 intel_iommu=on net.ifnames=0 crashkernel=171M,high crashkernel=72M,low'
    try:
        with open('/efi/boot_target.nsh', 'x') as boot_target_nsh:
            boot_target_nsh.write(boot_target_nsh_string)

        boot_target_nsh.close()
        print('Created boot_target.nsh!')
        result = True

    except FileExistsError:
        print('boot_target.nsh already exists, validate for errors!')
        result = False

    file_0.close()
    file_1.close()
    file_2.close()

    return result


def cleanup():
    command = subprocess.run(['''rm -rf /efi/kernel_version.txt && rm -rf /efi/vmlinuz.txt && rm -rf /efi/initramfs.txt'''], shell= True)

    if command.returncode == 0:
        print('Cleanup complete. Reboot!')
        result = True

    else:
        print('Cleanup not completed.')
        result = False

    return result
