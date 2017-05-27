import sys

ob= sys.argv[1]
ob = str(ob)
ob_seq=[]

for i in ob:
    ob_seq.append(i)
print ("Observation sequence :" + ob)

#stores states
state_tuple = ('COLD', 'HOT')
#State's start probability
prob_start = {'COLD': 0.2, 'HOT': 0.8}
#emmission Probabilities
prob_em = {'COLD': {'1': 0.5, '2': 0.4, '3': 0.1}, 'HOT': {'1': 0.2, '2': 0.4, '3': 0.4}}
#transmission Probabilities
prob_tr = {'COLD': {'COLD': 0.6, 'HOT': 0.4}, 'HOT': {'COLD': 0.3, 'HOT': 0.7}}

#Define a list to keep track of the maximum probabilities and the state that has the maximum probability
List_back = [{}]
#storing the initial probabilities in the list to be able to backtrack from the final state
for i in state_tuple:
    List_back[0][i] = {"prob": prob_start[i] * prob_em[i][ob_seq[0]], "prev": None}

len_states= len(ob_seq)

#calculating the maximum probabilities of states at each level of sequence
for states in range(1, len_states):
    List_back.append({})


# calculate maximum probability from previous state
    for i in state_tuple:
        prob_max = -1
        for j in state_tuple:
            prob_max = max(List_back[states - 1][j]["prob"] * prob_tr[j][i], prob_max)
        # Storing state with max probability
        for prev_st in state_tuple:
            if List_back[states - 1][prev_st]["prob"] * prob_tr[prev_st][i] == prob_max:
                max_prob = prob_max * prob_em[i][ob_seq[states]]
                List_back[states][i] = {"prob": max_prob, "prev": prev_st}
                break

# The highest probability
max_prob = max(value["prob"] for value in List_back[-1].values())
state_prior = None
final_list = []

for state, probability in List_back[-1].items():
    if probability["prob"] == max_prob:
        final_list.append(state)
        state_prior = state
        break

list_len= len(ob_seq)-2

while list_len >=0:
    for a, b in List_back[list_len].items():
        if a == state_prior:
            final_list.append(a)
            state_prior= b['prev']
    list_len=list_len-1
final_list.reverse()
FSL = " ".join(final_list)
print("Final state list : " + FSL)
