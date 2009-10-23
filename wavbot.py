from waveapi import events
from waveapi import model
from waveapi import robot

import cgi

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    Notify(context)

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("I'm alive!")

def Notify(context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hi everybody!")
  
def OnBlipAdded(properties, context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("waveId = " + root_wavelet.waveId)    

if __name__ == '__main__':
  myRobot = robot.Robot('wavbot', 
      image_url='http://wavbot.appspot.com/assets/icon.jpg',
      version='5',
      profile_url='http://wavbot.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED, OnParticipantsChanged)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.WAVELET_BLIP_CREATED, OnBlipAdded)
  myRobot.Run()