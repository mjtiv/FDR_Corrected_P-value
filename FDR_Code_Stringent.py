#!/usr/bin/python3.6

# Python Code to Create An Adjusted P-Value
# Note with duplicate values this code returns the lowest p-value for both
# duplicate values

#Original Example values for Benjamini-Hochberg 1995 Paper (Added a duplicate value to
# demonstrate issue)
p_values=[0.0001, 0.0004, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344,
          0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.000]

#function performs FDR correction of the p-values
#using Benjamini-Hochberg 1995
#Sort list of p-values
#equation for p-value correction (p-value x NumbTest / p-value_Rank)
#choose cutoff point for significance
def fdr_correction(values):
    p_value_dict={}
    adj_p_values=[]
    #sort list (smallest p-value to highest value)
    p_values.sort();
    #create i value for equation
    i=1
    for x in range(0, len(p_values)):
        #append adjust FDR p-value
        adj_p_values.append(p_values[x] * (len(p_values)) / i)
        i+=1 #increment i value

        # Use more strigent corrected p-value and skip all lower corrected values
        if p_values[x] in p_value_dict:
            continue
        else:
            #create a dictionary of values (key-original value: value-adjust value)
            p_value_dict.update({p_values[x]:adj_p_values[x]})

    return(p_value_dict)


def main():

   p_value_dict=fdr_correction(p_values)
   print (p_value_dict)
   #Note any p-value (values <0.05 are significant)---4 value in dictionary list

main()

#######################################
#######  Explanation of Code ##########
#######################################
#   P-value     Rank    Q-value
#    0.001	1	0.016
#    0.0004	2	0.0032     #FDR Stringent Selects First Value ---Larger
#    0.0004	3	0.002133333
#    0.0019	4	0.0076
#    0.0095	5	0.0304
#    0.0201	6	0.0536
#    0.0278	7	0.063542857
#    0.0298	8	0.0596
#    0.0344	9	0.061155556
#    0.0459	10	0.07344
#    0.324	11	0.471272727
#    0.4262	12	0.568266667
#    0.5719	13	0.703876923
#    0.6528	14	0.746057143
#    0.759	15	0.8096
#    1	16	1

