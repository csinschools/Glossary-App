glossary = [
  "Variable", "A named piece of memory that holds data.",
  "Assignment", "The operation of storing data in a variable.",
  "Initialisation", "When a variable is created and assigned a starting value.",
]

from GlossaryApp import *
app = GlossaryApp(glossary)

text = Label("GLOSSARY FLASH CARDS", x = 0, y = 0, width = 600, height = 88)
text.bgcolor = [179, 0, 147]
text.color = [255, 255, 255]
text.padding = [20, 20, 20, 20]
text.fontSize = 18
text.fontFamily = "arial"
text.center()
app.add(text)

app.run()

state = 0

while True: 
  event = app.get_next_event()
  if state == 0:    
    if event.control == text:
      state = 1
  elif state == 1:
    if app.fadeOut(text) == True:
      state = 2
      app.readDefinition()
  elif state == 2:
    if app.fadeIn(text) == True:
      state = 3
  elif state == 3:    
    if event.control == text:
      state = 4
  elif state == 4:
    if app.fadeOut(text) == True:
      state = 5
      app.readNextTerm()
  elif state == 5:
    if app.fadeIn(text) == True:
      state = 0
  
  text.data = app.getSentence()
  app.refresh()    