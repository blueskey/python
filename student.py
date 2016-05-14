#!/user/bin/python
#coding=utf-8

from _future_ import division
import random

score=[random.randint(0,100) for i in range(40)]
print score

num=len(score)

sum_score=sum(score)
ave_num=sum_score/num
less_ave=len([i for i in score if i<ave_num])
print "平均分：: %.1f " % ave_num

print "低于平均分的人数：%d " % less_ave

sorted_socre=sorted(score,reverse=True)

print sorted_score
