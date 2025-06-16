distance = 1.23
height = 2.34



print("Height: " +  str(height) + ", Distance: " + str(height))

print(f"Height:  {height:.1f}, Distance: {distance}" )

print("Height: {1:.1f}, Distance:{0}".format(distance, height))

#En java seria System.out.println(String.format("Height: %.1f, Distance: %f", height, distance));
print("Height: %.1f, Distance: %f" %(height, distance))

print("one\ntwo") 
print(r"one\ntwo")
