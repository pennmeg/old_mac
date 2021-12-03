def main():
  get_animals = True
  animal = ''
  sound = ''
  farm = []

  while get_animals == True:
    ### Don't provide instructions for song if there are no animals yet
    if len(farm) == 0:
      animal = input("What is an animal on Old MacDonald's Farm? ")
    else:
      animal = input("What is an animal on Old MacDonald's Farm? Type -1 to sing the song. ")
    
    ### Check if ready to sing song
    if animal == '-1':
      ### Loop over animals in farm and pass to song
      for f in farm:
        singSong(f)
      get_animals = False
    ### Ask for sound
    else:
      sound = input("And what sound does that animal make? ")
      farm.append([animal, sound])
      animal = ''
      sound = ''

def singSong(f):
  print('Old MacDonald had a farm. E-I-E-I-O!')
  print('And on that farm, he had a ' + f[0] + '. E-I-E-I-O!')
  print('With a ' + f[1] + '-' + f[1] + ' here and a ' + f[1] + '-' + f[1] + ' there,')
  print('here a ' + f[1] + ' there a ' + f[1] + ' , everywhere a ' + f[1] + '-' + f[1] + '.')
  print('Old MacDonald had a farm. E-I-E-I-O!')

main()