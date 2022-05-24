'''
Delete double space in a string
'''
story = "The quick brown fox jumps over the lazy  dog."
print(story) #print story as it is
print(story.replace("  ", "")) #removes double space
print(story.replace("  ", " ")) #replace double space with single space
