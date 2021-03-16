# Adane Adgo
# Elie Bracha
# GitHub: https://github.com/Numerical-Analysis-Elie-Adane-SCE/Assignement_1
import math


def epsilon():
    """
    :return: the machine precession
    """
    eps = 1.0
    while eps + 1 > 1:
        eps /= 2
    return eps * 2


# Q1:
""" before the Correction """
print("\nQ1:\n\nBefore the Correction: abs(3.0 * (4.0 / 3.0 - 1) - 1) = " + str(abs(3.0 * (4.0 / 3.0 - 1) - 1)) + "\n")


""" after the Correction """
print("After the Correction: (abs(3.0 * (4.0 / 3.0 - 1) - 1) - epsilon()) = " + str((abs(3.0 * (4.0 / 3.0 - 1) - 1) - epsilon())))

#  Q2 - pdf
""" in the pdf file"""
print("\nQ2:\nin the Assignment_1_Adane_Adgo_Elie_Bracha_Numerical_Analysis.pdf file.")

#  Q3 - Machine procession
print("\nQ3: \nThe Machine precision is: " + str(epsilon()))















