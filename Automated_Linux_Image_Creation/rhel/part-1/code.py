import subprocess
import time


def fstab_edit():
    print('Creating new fstab...')
    command = subprocess.run(['''printf '/dev/sda1 / ext3 defaults 1 1\n/dev/sda2 /boot/efi vfat umask=0077,shortname=winnt 0 2\n/dev/sda6 swap swap defaults 0 0' > /etc/fstab'''], shell= True)

    if command.returncode == 0:
        print('Fstab edited succesfully!')
        result = True

    else:
        print('Script did not edit fstab!')
        result = False

    return result


def grub_edit():
    print('Editing grub...')
    command = subprocess.run(["""printf 'GRUB_TIMEOUT=5\nGRUB_DEFAULT=0\nGRUB_DISABLE_SUBMENU=true\nGRUB_TERMINAL_OUTPUT="console"\nGRUB_CMDLINE_LINUX="/dev/sda1 rhgb quiet"\nGRUB_DISABLE_RECOVERY="true"\nGRUB_ENABLE_BLSCFG=true\nGRUB_DISABLE_LINUX_UUID="true"\nGRUB_ENABLE_LINUX_LABEL="true"' > /etc/default/grub"""], shell= True)

    if command.returncode == 0:
        print('Grub edited successfully!')
        result = True
    else:
        print('Script did not edit grub!')
        result = False

    return result


def grub_rebuild():
    print('Rebuilding grub...')
    command = subprocess.run(['grub2-mkconfig -o /boot/grub2/grub.cfg'], shell= True)

    if command.returncode == 0:
        print('Grub rebuild successful!')
        result = True

    else:
        print('Script did not rebuild grub!')
        result = False

    return result


def add_dhclient_to_systemctl():
    print('Adding dhclient to: rc.local...')
    command = subprocess.run(['''echo '#!/bin/bash\ndhclient' > /etc/rc.local'''], shell= True)

    if command.returncode == 0:
        print('DHCLIENT added to rc.local')
        result = True

    else:
        print('Could not add dhclient.')
        result = False

    return result


def curl_repos(repos_list):

    for repo in repos_list:

        command = subprocess.run(f'''curl -o /etc/yum.repos.d/{repo} http://link_to_your_project_repo/{repo}''', shell= True)

        if command.returncode == 0:
            print(f'{repo} added successfully!')
            result = True

        else:
            print(f'Could not create {repo}.')
            result = False

        return result


def yum_packages():
    print('Installing needed packages...')
    command = subprocess.run(['''yum install -y ALL_NEEDED_PACKAGES_HERE --skip-broken'''], shell= True)
    time.sleep(1)

    if command.returncode == 0:
        print('Packages installed successfully!')
        result = True

    else:
        print('Some packages was not installed!')
        result = False

    return result


def systemctl_stop_services():
    command = subprocess.run(['''systemctl stop firewalld && systemctl disable firewalld && systemctl stop NetworkManager && systemctl disable NetworkManager && printf 'SELINUX=disabled\n SELINUXTYPE=targeted' > /etc/selinux/config'''], shell= True)

    if command.returncode == 0:
        print('Services stopped!')
        result = True

    else:
        print('Services not stopped.')
        result = False

    return result


def mkdir_dirs():
    print('Creating dirs...')
    command = subprocess.run(['''mkdir /efi && mkdir /root/python'''], shell= True)

    if command.returncode == 0:
        print('Dirs created successfully!')
        result = True

    else:
        print('Dirs not created!')
        result = False

    return result


def untar_python(file):
    print(f'Untaring python from: {file}')
    command = subprocess.run([f'''tar -C /root/python/ -xzvf /root/Automated_Linux_Image_Creation/packages/{file}'''], shell= True)

    if command.returncode == 0:
        print('Untared successfully!')
        result = True

    else:
        print('Pyhton not untared!')
        result = False

    return result


def configure_python(file):
    print('Configuring python!')
    command = subprocess.run([f'''/root/python/{file}/configure'''], shell= True)

    if command.returncode == 0:
        print('Configured successfully!')
        result = True

    else:
        print('Pyhton not configured!')
        result = False

    return result


def make_python(file):
    print('Making python!')
    command = subprocess.run([f'''make /root/python/{file}/'''], shell=True)

    if command.returncode == 0:
        print('Configured successfully!')
        result = True

    else:
        print('Pyhton not configured!')
        result = False

    return result


def make_install_python(file):
    print('Installing python!')
    command = subprocess.run([f'''make install /root/python/{file}/'''], shell=True)

    if command.returncode == 0:
        print('Installed successfully!')
        result = True

    else:
        print('Pyhton not installed!')
        result = False

    return result

