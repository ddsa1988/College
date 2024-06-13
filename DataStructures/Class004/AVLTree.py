from BinarySearchTree import BST
from BalanceFactor import BalanceFactor


class AVL(BST):
    pass

    def __get_node_height(self, node):
        if node is None:
            return - 1

        return max(self.__get_node_height(node.left), self.__get_node_height(node.right)) + 1

    def __get_balance_factor(self, node):
        height_difference = self.__get_node_height(node.left) - self.__get_node_height(node.right)

        match height_difference:
            case -2:
                return BalanceFactor.UNBALANCED_RIGHT
            case -1:
                return BalanceFactor.SLIGHTLY_UNBALANCED_RIGHT
            case 1:
                return BalanceFactor.SLIGHTLY_UNBALANCED_LEFT
            case 2:
                return BalanceFactor.UNBALANCED_LEFT
            case _:
                return BalanceFactor.BALANCED
