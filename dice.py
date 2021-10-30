import random 
import statistics as s
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result =[]
for i in range(0,1000):
     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     dice_result.append(dice1 + dice2)

mean = s.mean(dice_result)
median = s.median(dice_result)
mode = s.mode(dice_result)
std = s.stdev(dice_result)

print("Mean of this data is ----> {}".format(mean))
print("Median of the data is ----> {}".format(median))
print("Mode of the data is ----> {}".format(mode))
print("std of the data is ----> {}".format(std))

first_std_start,first_std_end =  mean - std, mean + std
sec_std_start,sec_std_end =  mean - (2*std), mean + (2*std)
third_std_start,third_std_end =  mean - (3*std), mean + (3*std)

fig = ff.create_distplot([dice_result],["THIS IS THE RESULT"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))

#1st std 
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines + markers",name = "STD1 strt"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines + markers",name = "STD1 end"))

#2nd std
fig.add_trace(go.Scatter(x = [sec_std_start,sec_std_start],y = [0,0.17],mode = "lines + markers",name = "STD2 strt"))
fig.add_trace(go.Scatter(x = [sec_std_end,sec_std_end],y = [0,0.17],mode = "lines + markers",name = "STD2 end"))

#3rd std
fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines + markers",name = "STD3 strt"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines + markers",name = "STD3 end"))
#fig.show()


data_within_1_std = [i for result in dice_result if result > first_std_start and result < first_std_end]
data_within_2_std = [i for result in dice_result if result > sec_std_start and result < sec_std_end]
data_within_3_std = [i for result in dice_result if result > third_std_start and result < third_std_end]

print("{}% of data lies within first std".format(len(data_within_1_std)*100.0/len(dice_result)))
print("{}% of data lies within second std".format(len(data_within_2_std)*100.0/len(dice_result)))
print("{}% of data lies within third std".format(len(data_within_3_std)*100.0/len(dice_result)))




