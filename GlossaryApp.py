from csinscapp import *
from random import shuffle

class GlossaryApp(CSinSCApp):
  def __init__(self, glossary, width = "100%", height = "100%"):
    self.glossary = glossary

    self.fadeChange = 0.0002
    self.state = 0
    self.term_positions = list(range(0, len(glossary), 2))
    shuffle(self.term_positions)
    self.sentenceNumber = self.term_positions[0]
    self.next_term_position = 1

    super(GlossaryApp, self).__init__(width, height)

    self.container.style['background-color'] = "rgba(0,0,0,1)"

  def getSentence(self):
    if self.sentenceNumber % 2 == 1:
      return f"Answer:\n{self.glossary[self.sentenceNumber]}"
    else:
      return f"What is the meaning of:\n{self.glossary[self.sentenceNumber]}?"

  def readDefinition(self):
    self.sentenceNumber += 1

  def readNextTerm(self):
    self.sentenceNumber = self.term_positions[self.next_term_position]
    self.next_term_position = (self.next_term_position + 1) % len(self.term_positions)

  def fadeOut(self, control):
    done = False
    
    control.bgcolor.a -= self.fadeChange
    if control.bgcolor.a < 0:
      control.bgcolor.a = 0
    control.color.a -= self.fadeChange
    if control.color.a < 0:
      control.color.a = 0
    if control.bgcolor.a == 0 and control.color.a == 0:
      self.fadeChange = -self.fadeChange
      done = True
    return done

  def fadeIn(self, control):
    done = False
    control.bgcolor.a -= self.fadeChange
    if control.bgcolor.a > 1:
      control.bgcolor.a = 1
    control.color.a -= self.fadeChange
    if control.color.a > 1:
      control.color.a = 1
    if control.bgcolor.a == 1 and control.color.a == 1:
      done = True
      self.fadeChange = -self.fadeChange   
    return done    