import tarfile

from sh import cat, tar
from tqdm import tqdm


def extract_bigtgz(bigtgz, size, out_path):
    with tarfile.open(bigtgz, 'r|gz') as tar:
        with tqdm(total=size, unit='images', ncols=80, unit_scale=True) as pbar:
            def callback(members):
                for tarinfo in members:
                    pbar.update(1)
                    yield tarinfo
            tar.extractall(path=out_path, members=callback(tar))


def extract_chunks(self, files):
    for line in tar(cat(files, _piped=True), 'xvf', _iter=True):
        print(line)
