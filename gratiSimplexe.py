import numpy as np
import math
np.seterr(divide='ignore', invalid='ignore')


def hasPositiveValue(vector):
    for element in vector:
        if element > 0:
            return True

    return False


def main():
    print("Enter 1 if you want to solve a maximization problem.")
    print("Enter 2 if you want to solve a minimization problem.")
    user_choice = int(input())
    if user_choice == 1:
        maximization()


# todo: complete minimization


def maximization():
    print('Enter variables number:')
    number_of_variables = int(input())
    list = []
    # enter maximization equation
    for i in range(number_of_variables):
        print('enter the value of the variable x',
              i + 1, 'in the maximization equation')
        val = int(input())
        list.append(val)

    # enter the number of inequalities
    print('Enter the number of inequalities: ')
    number_of_inequalities = int(input())
    list.extend(np.zeros(number_of_inequalities).tolist())
    print(list)
    # constructing our matrix
    matrix_list = []
    # e values
    e_values = np.zeros(number_of_inequalities)
    e_values[0] = 1
    for i in range(number_of_inequalities):
        values_list = []
        for j in range(number_of_variables):
            print('enter the value of the variable x',
                  j + 1, 'in the inequality ', i + 1)
            value = float(input())
            values_list.append(value)

        # avoid regenerating another np zeros
        if i != 0:
            e_values[i - 1] = 0
            e_values[i] = 1

        for e_value in e_values:
            values_list.append(e_value)
        print('Enter the result of the inequality ', i + 1)
        res = float(input())
        # construct our list
        values_list.append(res)
        # append our list to the matrix
        matrix_list.append(values_list)
    print(matrix_list)

    coeff_z_array = np.array(list)
    matrix = np.array(matrix_list, dtype=float)
    vr_coeff_array = np.zeros(number_of_inequalities, dtype=float)
    zj = np.zeros(number_of_variables + number_of_inequalities, dtype=float)
    cj_minus_zj = coeff_z_array - zj

    # first iteration
    while hasPositiveValue(cj_minus_zj):
        # find the index of the max element in the array
        max_index = int(np.where(cj_minus_zj == max(cj_minus_zj))[0])
        print('MAX INDEX : ', max_index)
        # extract the pivot fector and flatten it
        pivot_vector = matrix[:, max_index:max_index + 1]
        pivot_vector = pivot_vector.flatten()
        # extract bj values
        bj = matrix[:, -1]
        # extract sorted values by dividing bj by pivot vector
        vs = np.divide(bj, pivot_vector)
        vs[vs < 0] = math.nan
        # extract the index of the min element in the array so we know the pivot element
        min_index = int(np.where(vs == min(vs))[0])
        matrix[min_index] = matrix[min_index] / matrix[min_index, max_index]
        vr_coeff_array[min_index] = coeff_z_array[max_index]
        for index in range(len(matrix)):
            if index != min_index:
                coeff = matrix[index, max_index]
                if coeff != 0:
                    matrix[index] = matrix[index] - matrix[min_index] * coeff
        # loop through each variable
        for index in range(len(matrix[0, :-1])):
            # scalar product
            n = np.dot(matrix[:, index], vr_coeff_array)
            zj[index] = n
        cj_minus_zj = coeff_z_array - zj

    print("The maximum gain is: ", np.dot(vr_coeff_array, bj))


main()
