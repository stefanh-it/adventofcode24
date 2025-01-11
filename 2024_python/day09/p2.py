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

    def __str__(self) -> str:
        return "".join([str(x)[-1] for x in range(0, len(self.expanded))]) + "\n" \
            + "".join([str(x) for x in self.expanded])

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
        frontpointer = self.expanded.index('.')
        backpointer = len(self.expanded) - 1
        file_id = self.expanded[backpointer]

        while file_id >= 0:
            file_len = 0
            b_size = 0
            file_len, backpointer = self.calc_file_len(backpointer, file_id)
            b_size, frontpointer = self.calc_free_space(frontpointer)
            if b_size >= file_len:
                self.push_file(backpointer, file_len, frontpointer, b_size)
                frontpointer -= b_size - file_len
            file_id -= 1

    def calc_file_len(self, backpointer, char):
        file_len = 0

        while True:
            if self.expanded[backpointer] == '.':
                backpointer -= 1
                continue
            if self.expanded[backpointer] == char:
                file_len += 1
                backpointer -= 1
            else:
                print(f"Calculated file len: {file_len}, bp: {backpointer}, char: {char}")
                return file_len, backpointer

    def calc_free_space(self, frontpointer):
        b_size = 0
        while True:
            if self.expanded[frontpointer] != '.' and b_size == 0:
                frontpointer += 1
                continue
            if self.expanded[frontpointer] == '.':
                b_size += 1
                frontpointer += 1
            else:
                print(f"Calculated free space: {b_size}, fp: {frontpointer}")
                return b_size, frontpointer

    def push_file(self, bp, file_len, fp, b_size):
        print(self)
        i = bp + 1
        fi = None
        while i in range(bp + 1, bp + file_len + 1):
            fi = self.expanded[i]
            # print(i)
            # print(self.expanded[i])
            self.expanded[i] = '.'
            i += 1

        j = fp - b_size
        while j in range(fp - b_size, fp - b_size + file_len):
            self.expanded[j] = fi
            j += 1

        print(self)
        breakpoint()
        
    def calc_checksum(self):
        for i, n in enumerate(self.ordered):
            self.checksum += (i * n)


def main(data):
    line = str(data)
    fs = Filesystem(line)
    fs.move_blocks()
    # fs.calc_checksum()
    return fs.checksum
