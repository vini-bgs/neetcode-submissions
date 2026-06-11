class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        linhas = collections.defaultdict(set)
        colunas = collections.defaultdict(set)
        blocos = collections.defaultdict(set)

        for l in range(9):
            for c in range(9):
                if board[l][c] == ".":
                    continue

                if board[l][c] in linhas[l] or board[l][c] in colunas[c] or board[l][c] in blocos[(l // 3, c // 3)]:
                    return False
                
                linhas[l].add(board[l][c])
                colunas[c].add(board[l][c])
                blocos[(l // 3, c // 3)].add(board[l][c])
        return True