import pandas as pd
import statistics
import csv

df=pd.read_csv("data.csv")

math_score_list=df["math score"].tolist()
reading_score_list=df["reading score"].tolist()
writing_score_list=df["writing score"].tolist()

math_score_mean=statistics.mean(math_score_list)
reading_score_mean=statistics.mean(reading_score_list)
writing_score_mean=statistics.mean(writing_score_list)

math_score_median=statistics.median(math_score_list)
reading_score_median=statistics.median(reading_score_list)
writing_score_median=statistics.median(writing_score_list)

math_score_mode=statistics.mode(math_score_list)
reading_score_mode=statistics.mode(reading_score_list)
writing_score_mode=statistics.mode(writing_score_list)

std_deviation1=statistics.stdev(math_score_list)
std_deviation2=statistics.stdev(reading_score_list)
std_deviation3=statistics.stdev(writing_score_list)

print("The mean of math score is: ",math_score_mean)
print("The mean of reading score is: ",reading_score_mean)
print("The mean of writing score is: ",writing_score_mean)

print("The median of math score is: ",math_score_median)
print("The median of reading score is: ",reading_score_median)
print("The median of writing score is: ",writing_score_median)

print("The mode of math score is: ",math_score_mode)
print("The mode of reading score is: ",reading_score_mode)
print("The mode of reading score is: ",writing_score_mode)

math_score_first_std_deviation_start, math_score_first_std_deviation_end = math_score_mean-std_deviation1, math_score_mean+std_deviation1
reading_score_first_std_deviation_start, reading_score_first_std_deviation_end = reading_score_mean-std_deviation2, reading_score_mean+std_deviation2
writing_score_first_std_deviation_start, writing_score_first_std_deviation_end = writing_score_mean-std_deviation3, writing_score_mean+std_deviation3

math_score_second_std_deviation_start, math_score_second_std_deviation_end = math_score_mean-(2*std_deviation1), math_score_mean+(2*std_deviation1)
reading_score_second_std_deviation_start, reading_score_second_std_deviation_end = reading_score_mean-(2*std_deviation2), reading_score_mean+(2*std_deviation2)
writing_score_second_std_deviation_start, writing_score_second_std_deviation_end = writing_score_mean-(2*std_deviation3), writing_score_mean+(2*std_deviation3)

math_score_third_std_deviation_start, math_score_third_std_deviation_end = math_score_mean-(3*std_deviation1), math_score_mean+(2*std_deviation1)
reading_score_third_std_deviation_start, reading_score_third_std_deviation_end = reading_score_mean-(3*std_deviation2), reading_score_mean+(3*std_deviation2)
writing_score_third_std_deviation_start, writing_score_third_std_deviation_end = writing_score_mean-(3*std_deviation3), writing_score_mean+(3*std_deviation3)


math_score_list_of_data_within_1_std_deviation = [result for result in math_score_list if result > math_score_first_std_deviation_start and result < math_score_first_std_deviation_end]
reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
writing_score_list_of_data_within_1_std_deviation = [result for result in writing_score_list if result > writing_score_first_std_deviation_start and result < writing_score_first_std_deviation_end]

math_score_list_of_data_within_2_std_deviation = [result for result in math_score_list if result > math_score_first_std_deviation_start and result < math_score_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
writing_score_list_of_data_within_2_std_deviation = [result for result in writing_score_list if result > writing_score_first_std_deviation_start and result < writing_score_first_std_deviation_end]

math_score_list_of_data_within_3_std_deviation = [result for result in math_score_list if result > math_score_first_std_deviation_start and result < math_score_first_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
writing_score_list_of_data_within_3_std_deviation = [result for result in writing_score_list if result > writing_score_first_std_deviation_start and result < writing_score_first_std_deviation_end]

print("{}% of data for math score lies within 1 standard deviation".format(len(math_score_list_of_data_within_1_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for writing score lies within 1 standard deviation".format(len(writing_score_list_of_data_within_1_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for reading score lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))

print("{}% of data for math score lies within 2 standard deviation".format(len(math_score_list_of_data_within_2_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for writing score lies within 2 standard deviation".format(len(writing_score_list_of_data_within_2_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for reading score lies within 2 standard deviation".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))

print("{}% of data for math score lies within 3 standard deviation".format(len(math_score_list_of_data_within_3_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for writing score lies within 3 standard deviation".format(len(writing_score_list_of_data_within_3_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for reading score lies within 3 standard deviation".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))