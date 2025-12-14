import hashlib
import json


class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class MerklePatriciaTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        node = self.root
        for char in key:
            node = node.children.setdefault(char, TrieNode())
        node.value = value

    def root_hash(self):
        content = json.dumps(self.serialize(self.root), sort_keys=True).encode()
        return hashlib.sha256(content).hexdigest()

    def serialize(self, node):
        return {
            "children": {k: self.serialize(v) for k, v in node.children.items()},
            "value": node.value,
        }
