"""
Projet 2
Nom : Secundar
Prénom : Ismael
Matricule : 504107
"""


import copy
import sys
from random import randint

sys.setrecursionlimit(40000)


class BinaryTree:
    def __init__(self, rootVal, leftBinaryTree=None, rightBinaryTree=None):
        self.key = rootVal
        self.left = leftBinaryTree
        self.right = rightBinaryTree

    def getRootVal(self):  # donne la valeur de la racine
        return self.key

    def setRootVal(self, obj):  # ajouter une valeur à la racine
        self.key = obj

    def getLeftChild(self):  # donne l'arbre gauche
        return self.left

    def setLeftChild(self, leftChild):
        self.left = leftChild

    def getRightChild(self):
        return self.right

    def setRightChild(self, rightChild):
        self.right = rightChild

    def insert(self, value):
        if self.getRootVal() == None:
            self.setRootVal(value)
        elif value <= self.getRootVal():
            if self.getLeftChild() == None:
                self.setLeftChild(BinaryTree(value))  # rajoute un arbre gauche à la valeur en question
            else:
                self.getLeftChild().insert(value)  # rajoute une valeur à l'arbre gauche
        else:
            if self.getRightChild() == None:
                self.setRightChild(BinaryTree(value))
            else:
                self.getRightChild().insert(value)

    def init_values(self, values):
        self.setLeftChild(None)
        self.setRightChild(None)
        self.setRootVal(None)
        for v in values:
            self.insert(v)

    def remove_maximum(self):
        """
        Fonction qui renvoie le maximum d'un arbre et qui enleve le maximum de l'arbre
        :return:
        """

        maximum = self                      # on stocke les valeurs qu'on aura besoin pour plus tard
                                            # certaines valeurs sont initialisées ici pour les utiliser plus tard
        root = self.key
        current = self
        old_max = self

        if root:                            # s'il y une racine à ce moment là on rentre dans la condition vue
                                            # qu'il y a une racine dans l'abre

            while maximum != None:          # Tant que l'arbre droit de l'arbre droit n'est pas vide on continue
                if current.getRightChild() != None:
                    if current.getRightChild().getRightChild():
                        old_max = maximum   # on stock le père du maximum pour pouvoir enlever le maximum sans perdre
                                            # ses noeuds
                current = maximum
                maximum = maximum.getRightChild()  # on change la valeur de maximum et le maximum est

            maximum = copy.deepcopy(current)    # on stock la valeur du maximum pour ne pas la perdre

            if current.getLeftChild():          # si le maximum a un noeud gauche

                left = None
                right = None
                if current.getLeftChild().getLeftChild():   # si le fils gauche a encore un fils gauche
                    left = current.getLeftChild().getLeftChild()    # on stock ce noeud

                if current.getLeftChild().getRightChild():  # si le fils droit a encore un fils droit
                    right = current.getLeftChild().getRightChild()  # on stock ce noeud

                if left is not None or right is not None:
                    current.setRootVal(current.getLeftChild().key)
                    current.setRightChild(right)            # on mets le noeud à la place du maximum avec son fils droit

                    current.setLeftChild(left)              # on mets le noeud à la place du maximum avec son fils gauche

                else:

                    current.setRootVal(current.getLeftChild().key)
                    current.setLeftChild(None)              # on mets son fils droit à None
            else:

                old_max.setRightChild(None)                 # sinon on mets le fils droit du pere à None
        return maximum

    def size(self):
        """
        fonction qui permet d'avoir le nombre de noeud dans un arbre
        :return:
        """
        noeud_total = 1

        if self.getLeftChild() != None:
            noeud_total += self.getLeftChild().size()
        if self.getRightChild() != None:
            noeud_total += self.getRightChild().size()
        return noeud_total

    def remove_minimum(self):
        """
        Cette méthode supprime le minimum d’un arbre et retourne sa valeur. Par contre le cas où la racine est elle même
        le minimum n'a pas été évoqué dans notre cas il est pas supprimé de l'arbre.
        Cette fonction fait la même chose que le maximum à la différence qu'on prend le minimum et on fait un parcours
        sur le fils gauche
        :return: la valeur maximale
        """
        minimum = self
        root = self.key
        current = self
        old_min = self

        if root:                    # si l'arbre a une racine
            if self.getLeftChild() is None and self.getRightChild() is None:    # s'il a ni fils gauche ni fils droit
                return minimum                                                  # on retourne le minimum mais
                                                                                # on l'enleve pas
            while minimum != None:  # Tant que l'arbre droit de l'arbre droit n'est pas vide
                if current.getLeftChild() != None:
                    if current.getLeftChild().getLeftChild():
                        old_min = minimum
                current = minimum
                minimum = minimum.getLeftChild()  # on change la valeur de maximum et le maximum est

            minimum = copy.deepcopy(current)

            if current.getRightChild():

                left = None
                right = None
                if current.getRightChild().getLeftChild():
                    left = current.getRightChild().getLeftChild()

                if current.getRightChild().getRightChild():
                    right = current.getRightChild().getRightChild()

                if left is not None or right is not None:
                    current.setRootVal(current.getRightChild().key)
                    current.setLeftChild(left)

                    current.setRightChild(right)

                else:

                    current.setRootVal(current.getRightChild().key)
                    current.setRightChild(None)
            else:

                old_min.setLeftChild(None)
        return minimum

    def rotate_root_right(self):
        """
        Fonction qui permet de faire une rotation de la racine
        :return:
        """

        if self.getLeftChild() == None:
            return

        else:
            a = self.getRootVal()                    # on stock la racine dans une variable
            sous_arbre_gauche = self.getLeftChild()  # on stock les fils gauches dans une variable
            sous_arbre_droit = self.getRightChild()  # on stock les fils droits dans une variable

            self.setRootVal(self.getLeftChild())  # on met le fils gauche à la racine

            self.setLeftChild(sous_arbre_gauche.getLeftChild())
            self.setRightChild(BinaryTree(a))     # on met l'ancienne racine au fils gauche de l'arbre

            self.getRightChild().setLeftChild(sous_arbre_gauche.getRightChild())    # on récupère les anciennes valeurs

            self.getRightChild().setRightChild(sous_arbre_droit)

            return None

    def rotate_root_left(self):
        """
        Cette fonction fait une rotation de la racine vers la gauche cette fois-ci
        :return:
        """

        if self.getRightChild() == None:
            return

        else:
            a = self.getRootVal()                    # on stock la racine dans une variable
            sous_arbre_droit = self.getRightChild()  # on stock les fils gauches dans une variable
            sous_arbre_gauche = self.getLeftChild()  # on stock les fils droits dans une variable

            self.setRootVal(self.getRightChild())

            self.setRightChild(sous_arbre_droit.getRightChild())
            self.setLeftChild(BinaryTree(a))

            self.getLeftChild().setRightChild(sous_arbre_droit.getLeftChild())

            self.getLeftChild().setLeftChild(sous_arbre_gauche)

        return None

    def rotate_simple_right(self):
        """
        Effectue une rotation simple droite sur l’arbre courant ou ne modifie pas l’arbre si celle-ci est impossible.
        :return:
        """
        if self.getLeftChild() == None:         # si la rotation est impossible on ne change rien à l'arbre
            return

        elif self.getLeftChild() is not None:   # s'il y a bien un fils gauche
            sous_arbre_gauche = self.getLeftChild()
            sous_arbre_droite = self.getRightChild()

            a = self.getRootVal()

            maximum = sous_arbre_gauche.remove_maximum()
            sous_arbre_gauche_1 = self.getLeftChild()

            self.setRootVal(maximum)
            self.setRightChild(sous_arbre_gauche_1)

            self.setRightChild(BinaryTree(a))
            self.getRightChild().setRightChild(sous_arbre_droite)

        return None

    def rotate_simple_left(self):
        """
        Effectue une rotation simple gauche sur l’arbre courant ou ne modifie pas l’arbre si celle- ci est impossible.
        :return:
        """
        if self.getRightChild() == None:
            return
            """
        elif self.getLeftChild() is None:
            root = self.getRootVal()                # -->8
            sous_arbre_droite = self.getRightChild() # --> 13
            self.setLeftChild(BinaryTree(root))
            self.setRootVal(sous_arbre_droite.getRootVal())
            self.setRightChild(None)

        """
        elif self.getRightChild() is not None:
            sous_arbre_droite = self.getRightChild()
            sous_arbre_gauche = self.getLeftChild()
            a = self.getRootVal()

            minimum = sous_arbre_droite.remove_minimum()
            sous_arbre_droite_1 = self.getRightChild()

            self.setRootVal(minimum)
            if self.getRightChild() == self.getRootVal():
                self.setRightChild(None)
            else:
                self.setRightChild(sous_arbre_droite_1)

            self.setLeftChild(BinaryTree(a))
            self.getLeftChild().setLeftChild(sous_arbre_gauche)

        return None

    def left_size(self):
        """
        fonction qui permet d'avoir la taille du fils gauche
        :return:
        """
        left_size = 0
        if self.getLeftChild():
            left_size = self.getLeftChild().size()
        return left_size

    def right_size(self):
        """
        fonction qui permet d'avoir la taille du fils droit
        :return:
        """
        right_size = 0
        if self.getRightChild():
            right_size = self.getRightChild().size()
        return right_size

    def left_right_diff(self):
        """
        foncion qui fait une différence entre le noeud gauche et droite
        :return:
        """
        return self.left_size() - self.right_size()

    def balance_tree(self):
        """
        Fonction qui permet de balancer l'arbre.
        Pour une optimisation maximal une rotation de la racine pouvait être effectuée mais dans mon cas j'ai préféré
        laisser uniquement les rotations simples
        :return:
        """
        left_right_diff = self.left_right_diff()
        while left_right_diff < 0 or left_right_diff > 1:       # tant que la différence des noeuds n'est pas entre 0
                                                                # ou 1 on continue
            if left_right_diff < 0:                             # si la différence est inférieur à 0
                self.rotate_simple_left()                       # on fait une rotation simple vers la gauche
                """
                diff_node_current = left_right_diff
                diff_node_after = 0
                if self.getLeftChild() is not None and self.getLeftChild().getRightChild() is not None:
                    diff_node_after = self.getLeftChild().getRightChild().left_right_diff()
                if abs(diff_node_after) < abs(diff_node_current):
                    self.rotate_root_left()
                """
            else:
                """
                diff_node_current = left_right_diff
                diff_node_after = 0
                if self.getRightChild() is not None and self.getRightChild().getLeftChild() is not None:
                    diff_node_after = self.getRightChild().getLeftChild().left_right_diff()
                if abs(diff_node_after) < abs(diff_node_current):
                    self.rotate_root_right()
                """
                self.rotate_simple_right()
            left_right_diff = self.left_right_diff()
        if self.getRightChild():                                # s'il y a encore des sous arbres on continue à balancer
            self.getRightChild().balance_tree()
        if self.getLeftChild():
            self.getLeftChild().balance_tree()

    def __str__(self):
        return str(self.key)

    def __iter__(self):
        return iter([self.getLeftChild(), self.getRightChild()])

    def display(self):
        """
        fonction qui permet d'afficher un arbre
        :return:
        """
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Fonction complémentaire à display pour afficher un arbre"""

        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

