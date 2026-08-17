objSpeed = int(input("Enter the speed of the object:"))

sound_speed = 343.2

mach = objSpeed / sound_speed

if mach >1.0:
    print("The object is moving at supersonic speed.")
else:
    print("The object is moving at subsonic speed.")
