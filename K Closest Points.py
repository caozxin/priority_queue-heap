from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k or not points:
            return None

        def distance(x, y):
            return sqrt(x**2 + y**2)

        n = len(points)
        # print(n)

        dis_dict = {}
        heap = []
        for each in points:
            each_distance = distance(each[0], each[1])
            heap.append(each_distance)
            # dis_dict[(each[0], each[1])] = each_distance
            if each_distance not in dis_dict.keys():
                dis_dict[each_distance] = [each]
            else:
                dis_dict[each_distance].append(each)
        # print(dis_dict)
        
        heapify(heap)
        # print("heap",  heap)
        res_list = []
        res = []

        for i in range(k):
            valu_dist = heappop(heap)
            # print(" ", valu_dist, dis_dict[valu_dist])
            if dis_dict[valu_dist] not in res_list:
                res_list.append(dis_dict[valu_dist])
                
                for each_pair in dis_dict[valu_dist]:
                    res.append(each_pair)

        # print(res)
        return res
