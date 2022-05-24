'''
Write a program to import an external module and use it as of your interest
'''

from Bio.Seq import Seq

# create a sequence object
my_seq = Seq("CATGTAGACTAG")

# print out some details about it
print("seq %s is %i bases long" % (my_seq, len(my_seq)))
# print("seq",my_seq,"is",len(my_seq),"long")