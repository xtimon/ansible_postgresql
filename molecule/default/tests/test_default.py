import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgres_packages(host):
    packages = [
        "postgresql-9.6",
        "postgresql-client-9.6",
        "postgresql-contrib-9.6",
    ]
    for p in packages:
        package = host.package(p)
        assert package.is_installed
        assert package.version.startswith("9.6")


def test_psycopg2_package(host):
    package = host.package("python-psycopg2")
    assert package.is_installed


def test_postgres_service(host):
    service = host.service("postgresql")
    assert service.is_running
    assert service.is_enabled


def test_postgres_sockets(host):
    socket = host.socket("tcp://127.0.0.1:5432")
    assert socket.is_listening
