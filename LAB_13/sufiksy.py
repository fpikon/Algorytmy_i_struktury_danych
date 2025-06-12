class SuffixTreeNode:
    def __init__(self):
        self.children = dict()
        self.leaf_count = 0


class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.text)):
            current = self.root
            for j in range(i, len(self.text)):
                char = self.text[j]
                if char not in current.children:
                    current.children[char] = SuffixTreeNode()
                current = current.children[char]

            current.leaf_count = 1

        self.compress(self.root)

    def compress(self, node):
        for char, child in list(node.children.items()):
            self.compress(child)

            if len(child.children) == 1:
                next_child = list(child.children.values())[0]
                next_char = list(child.children.keys())[0]

                new_char = char + next_char
                node.children[new_char] = next_child
                node.children.pop(char)

            if len(child.children) >= 1:
                child.leaf_count = sum(next_child.leaf_count for next_child in child.children.values())

    def search(self, suffix):
        current = self.root
        i = 0
        while i < len(suffix):
            found = False
            for char, child in list(current.children.items()):
                if char.startswith(suffix[i:]):
                    return child.leaf_count
                if suffix[i:].startswith(char):
                    current = child
                    i += len(char)
                    found = True
                    break
            if not found:
                return 0

        return current.leaf_count



    def display(self, node=None, prefix="", level=0):
        if node is None:
            node = self.root
        for char, child in sorted(node.children.items()):
            print("    " * level + f"[{char}]")
            self.display(child, prefix + char, level + 1)


def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    return [index for _, index in suffixes]

def binary_search_suffix_array(text, pattern, suffix_array = None, count = None):
    if suffix_array is None:
        suffix_array = build_suffix_array(text)

    start = 0
    end = len(suffix_array) - 1
    if count is None:
        count = 0

    if start > end:
        return count

    middle = (start + end) // 2
    suffix_idx = suffix_array[middle]
    suffix = text[suffix_idx:]
    if start == end:
        return count + int(suffix.startswith(pattern))

    if suffix.startswith(pattern):
        count += 1
        count = binary_search_suffix_array(text, pattern, suffix_array[start:middle], count)
        count = binary_search_suffix_array(text, pattern, suffix_array[middle + 1:], count)
        return count
    elif pattern < suffix:
        count = binary_search_suffix_array(text, pattern, suffix_array[start:middle], count)
    else:
        count = binary_search_suffix_array(text, pattern, suffix_array[middle + 1:], count)
    return count


def main():
    text = "banana\0"
    suffix_tree = SuffixTree(text)
    suffix_tree.display()
    pattern_list = ["a", "ban", "lit", "agh", "anan"]
    for pattern in pattern_list:
        count = suffix_tree.search(pattern)
        print(pattern, count)

    print("\n")
    text = "banana\0"
    pattern_list = ["a", "ban", "lit", "agh", "anan"]
    suffix_array = build_suffix_array(text)
    print(suffix_array)
    for pattern in pattern_list:
        count = binary_search_suffix_array(text, pattern, suffix_array)
        print(pattern, count)


if __name__ == '__main__':
    main()