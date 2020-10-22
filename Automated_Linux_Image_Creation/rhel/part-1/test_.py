from part1 import *


def test_fstab_edit():
    assert fstab_edit() == True


def test_grub_edit():
    assert grub_edit() == True


def test_grub_rebuild():
    assert grub_rebuild() == True


def test_add_dhclient_to_systemctl():
    assert add_dhclient_to_systemctl() == True


def test_curl_repos():
    assert curl_repos(repos_list=['', '']) == True


def test_yum_packages():
    assert yum_packages() == True


def test_systemctl_stop_services():
    assert systemctl_stop_services() == True


def test_mkdir_dirs():
    assert mkdir_dirs() == True


def test_untar_python():
    assert untar_python(file='Python-2.7.18.tgz') == True


def test_configure_python():
    assert configure_python(file='Python-2.7.18') == True


def test_make_python():
    assert make_python(file='Python-2.7.18') == True


def test_make_install_python():
    assert make_install_python(file='Python-2.7.18') == True
