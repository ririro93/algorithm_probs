# # DFS를 돌리는 건데 처음엔 밑으로 쭉 오른쪽으로 쭉 가서 effort를 구해본다
# # 그리고 백트래킹 하면서 effort 가 첨에 구한거 큰 경로로는 안간다
# # checked는 지금 경로에 포함 된 점들은 True 아니면 False 그리고 백트래킹으로 pop 해줄때는 다시 False로 바꿔주기

# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:        
#         # init
#         dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#         h, w = len(heights), len(heights[0])
#         path = [[0, 0]]
#         max_efforts = [0]
         
#         # get max effort of run where path is go down all the way and go right all the way
#         # save path and corresponding max effort along the way
#         global_max_effort = 0
#         i = j = 0
#         while i < h-1:
#             i += 1
#             effort = abs(heights[i][j] - heights[i-1][j])
#             global_max_effort = max(global_max_effort, effort)
#             path.append([i, j])
#             max_efforts.append(global_max_effort)
#         while j < w-1:
#             j += 1
#             effort = abs(heights[i][j] - heights[i][j-1])
#             global_max_effort = max(global_max_effort, effort)
#             path.append([i, j])
#             max_efforts.append(global_max_effort)
# #         print('path: ', path)                   # [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
# #         print('max_efforts: ', max_efforts)            # [0, 2, 2, 2, 2]
# #         print('global_max_effort:', global_max_effort)
        
#         do_not_go = []
#         while path:
#             # print(f'\npath: {path}')
#             # print(f'max_efforts: {max_efforts}')
#             x, y = path[-1]
#             effort = max_efforts[-1]
#             # if goal
#             if x == h-1 and y == w-1:
#                 global_max_effort = min(global_max_effort, effort)
#                 if global_max_effort == 0:
#                     return 0
#                 path.pop()
#                 max_efforts.pop()
                
#             else:
#                 if effort >= global_max_effort:
#                     path.pop()
#                     max_efforts.pop()
#                 else:
#                     # 새 경로 추가 못하면 이 위치도 빼줘야됨
#                     cnt = 0
#                     for d in dirs:
#                         nx = x + d[0]
#                         ny = y + d[1]
#                         if 0 <= nx < h and 0 <= ny < w and [nx, ny] not in path and [x, y, nx, ny] not in do_not_go:
#                             neffort = abs(heights[nx][ny] - heights[x][y])
#                             if neffort >= global_max_effort:
#                                 continue
#                             else:
#                                 # print('d: ', d, 'neffort: ', neffort)
#                                 cnt += 1
#                                 path.append([nx, ny])
#                                 max_efforts.append(max(effort, neffort))
#                     # 추가 못한 경우
#                     if cnt == 0:
#                         if x == 0 and y == 0:
#                             return global_max_effort
#                         path.pop()
#                         max_efforts.pop()
#                         ox, oy = path[-1]
#                         do_not_go.append([ox, oy, x, y])
#         return global_max_effort
