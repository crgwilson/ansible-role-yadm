def test_default_files(host):
    d = host.file("/root/lib/yadm-3.1.1")
    assert d.is_directory
    assert d.user == "root"
    assert d.group == "root"
    assert d.mode == 0o755

    f = host.file("/root/lib/yadm-3.1.1/yadm")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755

    b = host.file("/root/bin/yadm")
    assert b.is_symlink
