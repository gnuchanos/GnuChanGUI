import alsaaudio

# Open the default mixer control
mixer = alsaaudio.Mixer()
mixer.setvolume(70)
new_volume_after_set = mixer.getvolume()
print(f"Volume after setting: {new_volume_after_set[0]}%")





