from code import *
'''
author: Mateusz Redzynia
version: 0.01
if there are some errors feedback will be appreciated.
WARNING! Script is experimental and interferes into FSTAB and GRUB config files.
create copy of this two files, located in: /etc/fstab and /etc/default/grub.
'''

def start():
    fstab_edit()
    grub_edit()
    grub_rebuild()
    add_dhclient_to_systemctl()
    curl_repos(repos_list=['', ''])
    yum_packages()
    systemctl_stop_services()
    mkdir_dirs()
    untar_python(file='Python-2.7.18.tgz')
    configure_python(file='Python-2.7.18')
    make_python(file='Python-2.7.18')
    make_install_python(file='Python-2.7.18')


start()
