class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys, sells = [], []
        for price, amount, otype in orders:
            # add to dict
            if otype == 0:
                # buy  
                while amount > 0 and len(sells) > 0:
                    pt = sells[0]
                    if pt[0] > price:
                        break
                    
                    # print(sells[min_sell], amount)
                    deal = min(pt[1], amount)
                    amount -= deal
                    pt[1] -= deal
                    if pt[1] == 0:
                        heapq.heappop(sells)

                if amount != 0:
                    heapq.heappush(buys, [-price, amount]) # -price是为了largest price in heap
                
                
            else:
                # sell 
                while amount > 0 and len(buys) > 0:
                    pt = buys[0]
                    if -pt[0] < price:
                        break
                    
                    # print(sells[min_sell], amount)
                    deal = min(pt[1], amount)
                    amount -= deal
                    pt[1] -= deal
                    if pt[1] == 0:
                        heapq.heappop(buys)

                if amount != 0:
                    heapq.heappush(sells, [price, amount])
        return (sum([t[1] for t in buys]) + sum([t[1] for t in sells])) % (10**9+7)

            