# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2781

    level1["cough"] = - 1.0
    level1["cough_info_gain"] = 0.2365

    level1["radon"] = - 1.0
    level1["radon_info_gain"] = 0.0350

    level1["weight_loss"] = - 1.0
    level1["weight_loss_info_gain"] = 0.0291

    level2_left["smoking"] = - 1.0
    level2_left["smoking_info_gain"] = 0.
    level2_right["smoking"] = - 1.0
    level2_right["smoking_info_gain"] = 0.

    level2_left["radon"] = - 1.0
    level2_left["radon_info_gain"] = 0.0729

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219

    level2_left["weight_loss"] = - 1.0
    level2_left["weight_loss_info_gain"] = 0.1710

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = - 1.0
    level2_right["cough_info_gain"] = 0.3219

    level2_right["weight_loss"] = - 1.0
    level2_right["weight_loss_info_gain"] = 0.1711

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}


    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

     ''' (a) class_co = 10
             class_c1 = 10
            tot = class_co + class_c1
            p_co = class_co/tot
            p_c1 = class_c1/tot
            gini_index = 1 - (p_co**2 + p_c1**2)
            print(gini_index)
    '''

    ''' (b) For each Customer ID there is no impurity , So Gini index is 0 '''

    ''' (c) n_instances = 20
        n_male = 10
        n_female = 10
        p_male = n_male / n_instances
        p_female = n_female / n_instances
        p_male_co = 6/n_male
        p_male_c1 = 4/n_male
        p_female_co = 4/n_female
        p_female_c1 = 6/n_female
        gini_male = 1 - (p_male_co ** 2  + p_male_c1 ** 2)
        gini_female = 1 - (p_female_co ** 2 + p_female_c1 ** 2)
        gender_gini_index = (p_male * gini_male) + (p_female * gini_female)
        print(gender_gini_index)
    '''


    ''' (d) num_instances = 20
        num_family = 4
        num_sports = 8
        num_luxury = 8
        prob_family = num_family / num_instances
        prob_sports = num_sports / num_instances
        prob_luxury = num_luxury / num_instances
        p_family_co = 1/num_family
        p_family_c1 = 3/num_family
        p_sports_co = 8/num_sports
        p_sports_c1 = 0/num_sports
        p_luxury_co = 1/num_luxury
        p_luxury_c1 = 7/num_luxury
        gini_family = 1 - (p_family_co ** 2  + p_family_c1 ** 2)
        gini_sports = 1 - (p_sports_co ** 2  + p_sports_c1 ** 2)
        gini_luxury = 1 - (p_luxury_co ** 2  + p_luxury_c1 ** 2)
        overall_gini_index = prob_family * gini_family + prob_sports * gini_sports + prob_luxury * gini_luxury
        print("Overall Gini index for Car Type (multiway split):", overall_gini_index)
    '''

    ''' (e)
    num_instances = 20
    num_small = 5
    num_medium = 7
    num_large = 4
    num_extra_large = 4
    
    prob_small = num_small / num_instances
    prob_medium = num_medium/ num_instances
    prob_large = num_large / num_instances
    prob_extra_large = num_extra_large/ num_instances
    
    p_small_co = 3/num_small
    p_small_c1 = 2/num_small
    
    p_medium_co = 3/num_medium 
    p_medium_c1 = 4/num_medium 
    
    p_large_co = 2/num_large
    p_large_c1 = 2/num_large
    
    p_extra_large_co = 2/num_extra_large
    p_extra_large_c1 = 2/num_extra_large
    
    gini_small = 1 - (p_small_co ** 2  + p_small_c1 ** 2)
    gini_medium = 1 - (p_medium_co ** 2  + p_medium_c1 ** 2)
    gini_large = 1 - (p_large_co ** 2  + p_large_c1 ** 2)
    gini_extra_large = 1 - (p_extra_large_co ** 2  + p_extra_large_c1 ** 2)

    overall_gini_index = prob_small * gini_small + prob_medium * gini_medium + prob_large * gini_large + prob_extra_large * gini_extra_large

    print(overall_gini_index)
    '''

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.163
    answer["(e) Gini, Shirt type"] = 0.4915

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car type has the lowest Gini index"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = ""

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous','quantitative','interval']
    answer["f: explain"] = "It can be ratio attribute as well if sea level is not considered as an arbitrary origin"

    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = "It can be interval attribute as well if distance of 0 from the center of campus is considered as an arbitrary origin"

    answer["l"] = ['discrete','quantitative','ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 1 has high accuracy on A but accuracy drops on B which indicates overfitting, But for Model 2 accuracy on both Dataset A and B are almost same indicating better generalization to new data. "

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Though accuracy drops slightly Model 2 is still preferable due to better generalization observed earlier and it is less likely to overfit."

    explain["c similarity"] = "Regularization"
    explain["c similarity explain"] = "Both techniques aims to reduce overfitting by penalizing models for complexity."

    explain["c difference"] = "Specificity"
    explain["c difference explain"] = "MDL aims for a model that requires fewer bits to describe,whereas pessimistic error aims to adjust tree error to avoid complex decision tree."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    ''' a) import math

        total_instances = 20
        positive_instances = 10
        negative_instances = 10
        
        p_positive_before = positive_instances / total_instances
        p_negative_before = negative_instances / total_instances
        
        entropy_before = -((p_positive_before * math.log2(p_positive_before)) + (p_negative_before * math.log2(p_negative_before)))
        
        entropy_after = 0
        
        information_gain = entropy_before - entropy_after
        
        print(information_gain)
     '''
     ''' b)
     import math
        total_instances = 20
        positive_left = 9
        negative_left = 1
        positive_right = 1
        negative_right = 9
        
        p_positive_before = (positive_left + positive_right) / total_instances
        p_negative_before = (negative_left + negative_right) / total_instances
        
        entropy_before = -((p_positive_before * math.log2(p_positive_before)) + (p_negative_before * math.log2(p_negative_before)))
        
        n_left = positive_left + negative_left
        n_right = positive_right + negative_right
        p_left = n_left / total_instances
        p_right = n_right / total_instances
        
        entropy_left = -((positive_left / n_left * math.log2(positive_left / n_left)) + (negative_left / n_left * math.log2(negative_left / n_left)))
        entropy_right = -((positive_right / n_right * math.log2(positive_right / n_right)) + (negative_right / n_right * math.log2(negative_right / n_right)))
        
        information_gain = entropy_before - (p_left * entropy_left + p_right * entropy_right)
        
        print(information_gain)
    '''
    '''
    d. import math

    total_instances = 20
    positive_instances = 10
    negative_instances = 10
    num_unique_ids = 20  
    
    p_positive = positive_instances / total_instances
    p_negative = negative_instances / total_instances
    entropy_before_split = - (p_positive * math.log2(p_positive) + p_negative * math.log2(p_negative))
    
    
    entropy_after_split_weighted_avg = 0
    
    information_gain = entropy_before_split - entropy_after_split_weighted_avg
    
    split_information = - sum([(1 / num_unique_ids) * math.log2(1 / num_unique_ids) for _ in range(num_unique_ids)])
    
    gain_ratio = information_gain / split_information
    
    print("Gain Ratio:", gain_ratio)
    '''
    '''
    e. import math

    total_instances = 20
    positive_left = 9
    negative_left = 1
    positive_right = 1
    negative_right = 9
    
    p_positive = (positive_left + positive_right) / total_instances
    p_negative = (negative_left + negative_right) / total_instances
    entropy_before_split = - (p_positive * math.log2(p_positive) + p_negative * math.log2(p_negative))
    
    p_positive_left = positive_left / (positive_left + negative_left)
    p_negative_left = negative_left / (positive_left + negative_left)
    entropy_left = - (p_positive_left * math.log2(p_positive_left) + p_negative_left * math.log2(p_negative_left))
    
    p_positive_right = positive_right / (positive_right + negative_right)
    p_negative_right = negative_right / (positive_right + negative_right)
    entropy_right = - (p_positive_right * math.log2(p_positive_right) + p_negative_right * math.log2(p_negative_right))
    
    entropy_after_split_weighted_avg = (positive_left + negative_left) / total_instances * entropy_left + (positive_right + negative_right) / total_instances * entropy_right
    
    split_information = - ((10 / 20) * math.log2(10 / 20) + (10 / 20) * math.log2(10 / 20))
    
    information_gain = entropy_before_split - entropy_after_split_weighted_avg
    gain_ratio = information_gain / split_information
    
    print("Gain Ratio for Handedness:", gain_ratio)
    '''
    
    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Handedness"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

