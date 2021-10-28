class Block:
    def __init__(self, codewords_list, EC_codewords_list):
        self.codewords_list = codewords_list
        self.EC_codewords_list = EC_codewords_list

class Group:
    def __init__(self, blocks_list):
        self.blocks_list = blocks_list