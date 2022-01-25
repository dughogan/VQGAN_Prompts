import random

def make_random_prompt():
  styles = open("styles").read().split()
  index = random.randint(0, len(styles) - 1)
  style = styles[index].capitalize()
  prompt = style + " painting"
  r = random.random()

  places = open("places").read().splitlines()
  things = open("things").read().splitlines()
  shapes = open("shapes").read().splitlines()
  colors = open("colors").read().splitlines()
  artist = open("artists").read().splitlines()

  if r < 1.0 / 3.0:
    series = "shapes"
    index = random.randint(0, len(shapes) - 1)
    subject = " with " + shapes[index] + " in " + colors[index]
    prompt += subject
  elif r < 2.0 / 3.0:
    series = "things"
    index = random.randint(0, len(things) - 1)
    subject = things[index]
    prompt += " of " + subject + " in the color " + colors[index]
  elif r < 3.0 / 4.0:
    series = "shapes and colors"
    index = random.randint(0, len(shapes) - 1)
    subject = " of " + things[index] + " with " + shapes[index] + " in " + colors[index]
    prompt += subject
  elif r < 4.0 / 5.0:
    series = "shapes"
    index = random.randint(0, len(shapes) - 1)
    subject = " with " + shapes[index] + " in " + colors[index] + " in the style of " + artist[index]
    prompt += subject
  elif r < 5.0 / 6.0:
    series = "things"
    index = random.randint(0, len(things) - 1)
    subject = things[index]
    prompt += " of " + subject + " in the color " + colors[index] + " in the style of " + artist[index]
  elif r < 6.0 / 7.0:
    series = "shapes and colors"
    index = random.randint(0, len(shapes) - 1)
    subject = " of " + things[index] + " with " + shapes[index] + " in " + colors[index] + " in the style of " + artist[index]
    prompt += subject
  else:
    series = "places"
    index = random.randint(0, len(places) - 1)
    subject = places[index]
    prompt += " of " + subject + " in the color " + colors[index]

  print(prompt)

make_random_prompt()
