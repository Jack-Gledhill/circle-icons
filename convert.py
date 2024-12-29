import logging
import os
import platform

# Adds homebrew libraries to the list of directories that Python will search when importing libraries
# TODO: add considerations for other operating systems
if platform.system() == "Darwin":
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"

from cairosvg import svg2png, svg2ps, svg2eps, svg2pdf

SVG_DIR = "docs/svg"
SVG_EXTENSION = ".svg"

PDF_DIR = "docs/pdf"
PDF_EXTENSION = ".pdf"

PNG_DIR = "docs/png"
PNG_EXTENSION = ".png"

EPS_DIR = "docs/eps"
EPS_EXTENSION = ".eps"

PS_DIR = "docs/ps"
PS_EXTENSION = ".ps"

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s: %(message)s")

class SourceFile:
    def __init__(self, fn: str):
        self.filename = fn

    @property
    def path(self) -> str:
        return os.path.join(SVG_DIR, self.filename)

    @property
    def stem(self) -> str:
        return os.path.splitext(self.filename)[0]

    @property
    def extension(self) -> str:
        return os.path.splitext(self.filename)[1]

    def to_png(self):
        for s in RASTER_SIZES:
            w, h = s[0], s[1]
            out_path = os.path.join(PNG_DIR, f"{w}x{h}", self.stem + PNG_EXTENSION)

            try:
                svg2png(url=self.path,
                        write_to=out_path,
                        output_width=w,
                        output_height=h)

            except Exception as e:
                logging.error(f"Failed to convert {self.stem} [{out_path}] to png ({w}x{h}): {e}")

            else:
                logging.info(f"Successfully converted {self.stem} to png ({w}x{h})")

    def to_pdf(self):
        for s in RASTER_SIZES:
            w, h = s[0], s[1]
            out_path = os.path.join(PDF_DIR, f"{w}x{h}", self.stem + PDF_EXTENSION)

            try:
                svg2pdf(url=self.path,
                        write_to=out_path,
                        output_width=w,
                        output_height=h)

            except Exception as e:
                logging.error(f"Failed to convert {self.stem} [{out_path}] to pdf ({w}x{h}): {e}")

            else:
                logging.info(f"Successfully converted {self.stem} to pdf ({w}x{h})")

    def to_eps(self):
        try:
            svg2eps(url=self.path,
                    write_to=os.path.join(EPS_DIR, self.stem + EPS_EXTENSION))

        except Exception as e:
            logging.error(f"Failed to convert {self.stem} to eps: {e}")

        else:
            logging.info(f"Successfully converted {self.stem} to eps")

    def to_ps(self):
        try:
            svg2ps(url=self.path,
                   write_to=os.path.join(PS_DIR, self.stem + PS_EXTENSION))

        except Exception as e:
            logging.error(f"Failed to convert {self.stem} to ps: {e}")

        else:
            logging.info(f"Successfully converted {self.stem} to ps")

# Various sizes of raster files that each source file will be converted to
# Format is [w, h]
RASTER_SIZES = [
    # Ideal for favicons
    [16, 16],
    [32, 32],
    [48, 48],
    [64, 64],
    [96, 96],
    [128, 128],
    [192, 192],
    # Used in PWAs
    [256, 256],
    [512, 512],
    # High-res icons
    [1024, 1024],
    [2048, 2048]
]

def get_source_files() -> list[SourceFile]:
    files = []

    for fn in os.listdir(SVG_DIR):
        f = SourceFile(fn)
        if f.extension == SVG_EXTENSION and os.path.isfile(f.path):
            files.append(f)

    return files

def convert_sources(sources: list[SourceFile]):
    for s in sources:
        s.to_png()
        s.to_pdf()
        s.to_eps()
        s.to_ps()

def make_output_dirs():
    dirs = [
        *[os.path.join(PDF_DIR, f"{w}x{h}") for w, h in RASTER_SIZES],
        *[os.path.join(PNG_DIR, f"{w}x{h}") for w, h in RASTER_SIZES],
        EPS_DIR,
        PS_DIR
    ]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

if __name__ == "__main__":
    make_output_dirs()

    sources = get_source_files()
    convert_sources(sources)
    logging.info(f"Finished converting {len(sources)} sources")