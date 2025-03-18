class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_len = len(flowerbed)
        for i in range(bed_len):
            if n == 0:
                break
            if flowerbed[i] == 0 and ((i == 0 or flowerbed[i-1] == 0) and (i == bed_len - 1 or flowerbed[i+1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return True if n == 0 else False