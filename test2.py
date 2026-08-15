# def dict_graph(board):

#     n = len(board)
#     graph = {}

#     for i in range(n-1,-1,-1):
#         for j in range(n-1,-1,-1):

#             elm = board[i][j]

#             # left
#             if elm.isnum() and :

    


# board = ["E23","2X2","12S"]
# print(dict_graph(board))


intervals = [[1,4],[2,3]]

intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
print(intervals)