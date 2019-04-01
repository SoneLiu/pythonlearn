# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-04-01 09:52:04
# @Last Modified by:   Marte
# @Last Modified time: 2019-04-01 09:52:33
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()