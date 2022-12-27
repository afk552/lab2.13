#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numdel_module

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numdel_module.num_del(lst)())
    print(numdel_module.num_del(lst)("even"))
    print(numdel_module.num_del(lst)("odd"))
