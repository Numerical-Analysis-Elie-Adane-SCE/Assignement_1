# Adane Adgo
# Elie Bracha

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
print("\nQ1:\nBefore the Correction:", end=" ")
print((abs(3.0 * (4.0 / 3.0 - 1) - 1)))

""" after the Correction """
print("After the Correction:", end=" ")
print((abs(3.0 * (4.0 / 3.0 - 1) - 1) - epsilon()))

#  Q2 - pdf
""" in the pdf file"""
print("\nQ2 in the pdf file")

#  Q3 - Machine procession
print("\nQ3: \nthe Machine procession is: " + str(epsilon()))




#  Q3:








