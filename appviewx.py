class Solution:
    def extract_ips(self, s):
        start_index = []
        for i in range(len(s)):
            if not s[i-1].isalpha() and s[i].isdigit() and s[i+1] == ":" and s[i+2] == " ":
                print(s[i:i+2])
                start_index.append(i)

        splited_strings = []
        for i in range(len(start_index)):
            if not i == len(start_index)-1:
                splited_strings.append(s[start_index[i]:start_index[i+1]])
            else:
                splited_strings.append(s[start_index[i]:])

        headings = []
        for i in range(len(splited_strings)):
            for j in range(len(splited_strings[i])):
                if splited_strings[i][j]==":":
                    headings.append(splited_strings[i][:j+1])
                    break
        sep_str = []
        for i in range(len(splited_strings)):
            sep_str.append(list(splited_strings[i].split(" ")))
        res_head = []
        for i in range(len(headings)):
            ind = sep_str[i].index(headings[i])
            res_head.append(sep_str[i][ind+1])

        ip_arr = []
        for i in range(len(res_head)):
            if "inet" in sep_str[i]:
                ind = sep_str[i].index("inet")
                ip_arr.append(sep_str[i][ind+1])
            else:
                ip_arr.append(" ")
        for i in range(len(ip_arr)):
            for j in range(len(ip_arr[i])):
                if ip_arr[i][j] == "/":
                    ind = j
                    break
            ip_arr[i] = ip_arr[i][:j]

        result = []
        for i in range(len(ip_arr)):
            result.append(res_head[i] + " " + ip_arr[i])
        print(result)


if __name__ == "__main__":

    s = """
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever 
2: enp1s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 98:e7:f4:50:50:16 brd ff:ff:ff:ff:ff:ff
3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 94:53:30:38:93:69 brd ff:ff:ff:ff:ff:ff
    inet 192.168.138.14/24 brd 192.168.138.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 2585620sec preferred_lft 2585620sec
    inet6 fe80::2c92:6ad9:3b22:cb30/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
    """
    obj = Solution()
    obj.extract_ips(s)
