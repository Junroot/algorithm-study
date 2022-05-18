def maximumWhiteTiles(tiles: list[list[int]], carpetLen: int) -> int:
    if len(tiles) == 1:
        return min(tiles[0][1] - tiles[0][0], carpetLen)

    tiles.sort()

    incl = [tiles[0]]
    cur = tiles[0][1] - tiles[0][0] + 1
    start = 1
    while start < len(tiles) and tiles[start][1] - incl[0][0] < carpetLen:
        incl.append(tiles[start])
        cur += tiles[start][1] - tiles[start][0] + 1
        start += 1
    #cur -= incl[-1][1] - carpetLen - incl[0][0] + 1
    ans = cur

    for tile in tiles[start:]:
        while incl and tile[1] - incl[0][1] > carpetLen:
            print(cur, incl)
            cur -= min(incl[0][1] - (incl[-1][1] - carpetLen), incl[0][1] - incl[0][0] + 1)
            incl.pop(0)
        print(cur, incl)
        if incl:
            cur -= max(tile[1] - carpetLen + 1 - incl[0][0], 0)
        print(cur, incl)
        cur += tile[1] - tile[0] + 1
        incl.append(tile)

        if ans < cur:
            ans = cur

    return ans


print(maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], 10))
print(maximumWhiteTiles([[10,11],[1,1]], 2))
