def count_ips(start: str, end: str) -> int:

    start = start.split('.')
    end = end.split('.')

    count_start = 0
    count_end = 0
    for i in range(len(start)):

        if i == 0:
            count_start += int(start[i]) * (256 ** 3)
            count_end += int(end[i]) * (256 ** 3) 

        if i == 1:
            count_start += int(start[i]) * (256 ** 2)
            count_end += int(end[i]) * (256 ** 2) 

        if i == 2:
            count_start += int(start[i]) * (256)
            count_end += int(end[i]) * (256) 

        if i == 3:
            count_start += int(start[i])
            count_end += int(end[i]) 

    count = count_end - count_start
    return count

def count_ips_v2(start: str, end: str) -> int:

    def ip_to_int(ip):

        a,b,c,d = map(int,ip.split('.'))

        return a * (256 ** 3) + b * (256 ** 2) + c * (256) + d
    
    return ip_to_int(end) - ip_to_int(start)

start = "10.0.0.0"
end = "10.0.0.50"

print(count_ips(start,end))
print(count_ips(start,end))
