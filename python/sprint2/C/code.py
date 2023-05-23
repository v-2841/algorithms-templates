# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(node, i):
    while i:
        node = node.next_item
        i -= 1
    return node


def delete_node(head, index):
    if index == 0:
        return get_node_by_index(head, 1)
    dnode = get_node_by_index(head, index)
    if dnode.next_item is None:
        pnode = get_node_by_index(head, index-1)
        pnode.next_item = None
        return head
    pnode = get_node_by_index(head, index-1)
    pnode.next_item = get_node_by_index(head, index+1)
    return head


def solution(node, idx):
    node = delete_node(node, idx)
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
