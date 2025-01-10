class Filesystem():

    def __init__(self, line) -> None:
        self.line = line.strip()
        self.line = list(map(int, self.line))
        self.ordered: list = []
        self.expanded: list = []
        self.cond_len: int = 0
        self.checksum: int = 0
        self.expand()
        self.calc_cond_len()

    def expand(self):
        i = 0
        fid = 0
        free_space = False
        while i in range(0, len(self.line)):
            if not free_space:
                self.expanded.extend([fid] * self.line[i])
                fid += 1
                free_space = True
            elif free_space:
                self.expanded.extend(['.'] * self.line[i])
                free_space = False
            i += 1

    def calc_cond_len(self):
        for item in self.expanded:
            if isinstance(item, int):
                self.cond_len += 1

    def move_blocks(self):
        i = 0
        j = len(self.expanded) - 1
        b_size: int = 0

        while i in range(len(self.expanded)):
            # if self.expanded[i] == '.':
            #     b_size += 1
            # else:
            #     if b_size > 0:
            breakpoint()
            i += 1
            j -= 1

    def calc_checksum(self):
        for i, n in enumerate(self.ordered):
            self.checksum += (i * n)



def main(data):
    line = str(data)
    fs = Filesystem(line)
    fs.move_blocks()
    # fs.calc_checksum()
    return fs.checksum

