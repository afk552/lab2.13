def num_del(num_lst):
    def num_del_by_type(a="even"):
        if a == "even":
            a = [x for x in num_lst if x % 2]
        else:
            a = [x for x in num_lst if not x % 2]
        return a
    return num_del_by_type
