class Utils:
    def load_txt(filepath):
        js = {}
        with open(filepath,'r') as f:
            lines = f.readlines()
            for line in lines:
                start, end = line.split(' ')
                js[start] = end
        return js