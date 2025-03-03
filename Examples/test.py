"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""














# import speech_recognition as sr
# import os

# rec = sr.Recognizer()
# rec.energy_threshold = 400
# rec.dynamic_energy_threshold = False
# rec.pause_threshold = 2

# with sr.Microphone() as source:
#     rec.adjust_for_ambient_noise(source, duration=1)
#     while True:
#         print("Konuşabilirsiniz...")
#         text = ""
#         try:
#             audio = rec.listen(source)
#             text = rec.recognize_google(audio, language="tr-TR")
#             print(f"Söylediğiniz: {text}")
#         except sr.UnknownValueError:
#             print("Ses anlaşılamadı, tekrar deneyin.")
#         except sr.RequestError:
#             print("API'ye bağlanılamadı.")

#         # Komutları çalıştırma
#         if text.lower() == "tarayıcıyı aç":
#             os.popen("qutebrowser")
#         elif text.lower() == "sistemi kapat":
#             print("Sistem kapatılıyor...")
#             break  # Döngüyü sonlandırır.