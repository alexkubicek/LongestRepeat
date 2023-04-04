import sys


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def trie_construction(Patterns):
    count = 0
    root = TrieNode("")
    for pattern in Patterns:
        current_node = root
        for c in pattern:
            if c not in current_node.children.keys():
                current_node.children[c] = TrieNode(c)
            current_node = current_node.children.get(c)
        current_node.children['$'] = TrieNode('$')
    return root


# class from github
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

    def print(self):
        print(self.char)
        for n in self.children.values():
            n.print()


def get_suffixes(text):
    suffixes = []
    while len(text) > 0:
        suffixes.append(text)
        text = text[1:]
    return suffixes


def condense_tree(tree):
    for child_key in tree.children.keys():
        condense_tree(tree.children[child_key])
    if len(tree.children) == 1:
        key = ''
        for k in tree.children.keys():
            key = k
        child = tree.children[key]
        tree.char += child.char
        tree.children = child.children


def get_longest_found_twice(tree_to_search, longest_found):
    if len(tree_to_search.children) < 2:
        return str()
    longest_in_node = str()
    for key in tree_to_search.children.keys():
        each_node = tree_to_search.children[key]
        # print(each_node.char)
        cur_longest = get_longest_found_twice(each_node, longest_found)
        if len(each_node.children) > 1:
            cur_longest = each_node.char + cur_longest
        if len(cur_longest) > len(longest_in_node):
            # print("replaced " + longest_found + " with " + cur_longest)
            longest_in_node = cur_longest
    if len(longest_in_node) > len(longest_found):
        longest_found = longest_in_node
    if tree_to_search.char == '':
        return longest_found
    return longest_in_node


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    for line in inFile:
        input_text = line
    inFile.close()
    if input_text.endswith("\n"):
        input_text = input_text[0:(len(input_text)-1)]
    patterns = get_suffixes(input_text)
    trie = trie_construction(patterns)
    sys.setrecursionlimit(len(patterns) * len(input_text))
    condense_tree(trie)
    # trie.print()
    f = open("output.txt", 'w')
    sys.stdout = f
    print(get_longest_found_twice(trie, ''), end='')
    f.close()
