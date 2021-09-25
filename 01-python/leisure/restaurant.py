def draw_restaurant(height):
    minimumHeight = 4
    if (height <= 4):
        print(
'''
===============================
|           Chipotle          |
|             ====            |
|             |  |            |
|             |  |            |
===============================
''')
    else:
        #print roof
        print(
'''
   ===============================
   |           Chipotle          |'''
        )
        #print variable wall height
        for x in range(height-minimumHeight):
            print("   |                             |")
        #print floor + entrance
        print(
'''   |             ====            |
   |             |  |            |
   |             |  |            |
   ===============================
'''
        )
    return