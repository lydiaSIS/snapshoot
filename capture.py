import keyboard 
import PIL.ImageGrab

i=1
while True:
    try:
        print('press enter key')
        keyboard.wait("enter")
        snapshot= PIL.ImageGrab.grab()
        print("You took screenshot")
        snapshot.show()
        save_path = "C:/"
        snapshot.save(save_path.format(i))
        i+=1
    except:
        break
