def get_middle(s):
        if len(s) > 2:
            if len(s) % 2 == 0:
                x = round(len(s)/2)
                return s[int(x-1):int(x+1)]
            else:
                return s[int(len(s)/2)]
            pass
        else:
            return s
