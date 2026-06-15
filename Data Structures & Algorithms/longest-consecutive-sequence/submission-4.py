class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lista_ordenada = sorted(set(nums))
        print(lista_ordenada)
        todos_os_valores = list()
        count = 0

        for n in range(len(lista_ordenada)):
            try:
                if lista_ordenada[n + 1] == lista_ordenada[n] + 1:
                    count += 1
                    todos_os_valores.append(count)
                else:
                    count += 1
                    todos_os_valores.append(count)
                    count = 0
            except:
                count += 1
                todos_os_valores.append(count)

        if todos_os_valores:
            return max(todos_os_valores)
        else:
            return 0