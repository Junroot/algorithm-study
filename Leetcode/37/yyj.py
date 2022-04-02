class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def box_idx(r: int, c: int) -> int:
            return ((r // 3)) * 3 + c // 3
        
        def is_placeable(r: int, c: int, d: int) -> bool:
            return (d not in rows[r]) and (d not in cols[c]) and (d not in boxes[box_idx(r, c)])
        
        def place_number(r: int, c: int, d: int) -> None:
            rows[r][d] += 1
            cols[c][d] += 1
            boxes[box_idx(r, c)][d] += 1
            board[r][c] = str(d)
        
        def move_next_cells(r: int, c: int) -> None:
            if r == n-1 and c == n-1:
                nonlocal is_solved
                is_solved = True
            else:
                if c == n-1:
                    backtrack(r+1, 0)
                else:
                    backtrack(r, c+1)
                
        def remove_number(r: int, c: int, d: int) -> None:
            del rows[r][d]
            del cols[c][d]
            del boxes[box_idx(r, c)][d]
            board[r][c] = '.'
        
        
        def backtrack(r: int, c: int) -> None:
            if board[r][c] == '.':
                for d in range(1, 10):
                    if is_placeable(r, c, d):
                        place_number(r, c, d)
                        move_next_cells(r, c)
                        if not is_solved:
                            remove_number(r, c, d)
            else:
                move_next_cells(r, c)
        
        
        n = len(board)
        
        rows = [collections.defaultdict(int) for _ in range(n)]
        cols = [collections.defaultdict(int) for _ in range(n)]
        boxes = [collections.defaultdict(int) for _ in range(n)]
        
        is_solved = False
        
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    d = int(board[r][c])
                    place_number(r, c, d)
        
        backtrack(0, 0)
