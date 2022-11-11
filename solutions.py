def shop(N, sizes, M, requests):
    
    for i in range(len(sizes)):
        for j in range(len(requests)):
            if sizes[i] == requests[j]:
                continue
            if 'S' in requests[j].split():
                if 'M' or 'L' in sizes[i].split():
                    continue
            if requests[j]=='M':
                if 'L' in sizes[i].split():
                    continue
            if requests[j] == 'L':
                if 'XL' in sizes[i].split():
                    continue
        return 'yes'



sizes = ['XL','XXXXXXXXXL', 'XXS', 'M', 'XXS']
N = len(sizes)
requests = ['L','M','L','XXS']
M = len(requests)

shop(N, sizes, M, requests)