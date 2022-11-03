from image_cut import cli, cutter
from pathlib import Path
import shutil


def test_cli(tmp_path, capsys):
    shutil.copy("64x32.png", tmp_path)
    cli.cut(tmp_path / "64x32.png", "1x1")
    assert Path(tmp_path / "64x32.1-1.png").exists()


def test_cut_into_one(tmp_path):
    shutil.copy("64x32.png", tmp_path)
    cutter.cut(tmp_path / "64x32.png", "1x1")
    assert Path(tmp_path / "64x32.1-1.png").exists()


def test_cut_into_2x1(tmp_path):
    shutil.copy("64x32.png", tmp_path)
    cutter.cut(tmp_path / "64x32.png", "2x1")
    assert Path(tmp_path / "64x32.1-1.png").exists()
    assert Path(tmp_path / "64x32.2-1.png").exists()


def test_cut_into_4x2(tmp_path):
    shutil.copy("64x32.png", tmp_path)
    cutter.cut(tmp_path / "64x32.png", "4x2")
    assert Path(tmp_path / "64x32.1-1.png").exists()
    assert Path(tmp_path / "64x32.2-1.png").exists()
    assert Path(tmp_path / "64x32.3-1.png").exists()
    assert Path(tmp_path / "64x32.4-1.png").exists()
    assert Path(tmp_path / "64x32.1-2.png").exists()
    assert Path(tmp_path / "64x32.2-2.png").exists()
    assert Path(tmp_path / "64x32.3-2.png").exists()
    assert Path(tmp_path / "64x32.4-2.png").exists()
