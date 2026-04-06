class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        n1 = len(t)
        n2 = len(s)

        count_t = {}
        window = {}

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        res, res_len = [-1, -1], float("infinity")
        l = 0
        need, have = len(count_t), 0
        for r in range(n2):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in count_t and count_t[ch] == window[ch]:
                have += 1

            while have == need:
                window_len = r - l + 1
                if window_len < res_len:
                    res = [l, r]
                    res_len = window_len
                
                if s[l] in count_t and window[s[l]] == count_t[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        
        l, r = res
        return s[l: r+1] if res_len != float("infinity") else ""


        