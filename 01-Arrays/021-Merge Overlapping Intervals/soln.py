# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    
    def merge(self, intervals):
        # sorting the array wrt (start, end).
        my_cmp = lambda self: self.start
        intervals = sorted(intervals, key=my_cmp)
        
        node_num = 0
        a, b = intervals[0].start, intervals[0].end
        del_ind =[]
        
        for i in range(1, len(intervals)):
            c, d = intervals[i].start, intervals[i].end
            
            # Condition for overlapping intervals.
            if max(a, c) <= min(b, d):
                e, f = min(a,c), max(b, d)
                a, b = e, f
                intervals[node_num].start = e
                intervals[node_num].end = f
                del_ind.append(i)
                
            else:
                # Non-Overlapping case.
                node_num = i
                a, b = c, d
        
        # Deleting the overlapping intervals.     
        for i in del_ind[::-1]:
            del intervals[i]
            
        return intervals
                
                
                

