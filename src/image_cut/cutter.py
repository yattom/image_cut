from pathlib import Path
from PIL import Image
from dataclasses import dataclass


@dataclass
class CutParam:
    x: int
    y: int
    width: int = None
    height: int = None

    def set_size(self, width, height):
        self.width = width
        self.height = height


def cut(filename: Path, cut_param_str: str):
    cut_param = CutParam(*[int(v) for v in cut_param_str.split("x")])
    im = Image.open(filename)
    cut_param.set_size(im.width / cut_param.x, im.height / cut_param.y)
    for x in range(cut_param.x):
        for y in range(cut_param.y):
            box = im.crop((x * cut_param.width, y * cut_param.height,
                     (x + 1) * cut_param.width, (y + 1) * cut_param.height))
            box.save(filename.parent / f"64x32.{x + 1}-{y + 1}.png")