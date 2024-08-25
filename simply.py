import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

while True:
 try:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">Bot: "+response)
 except Exception as e:
        print(f"An error occured:{e}")
        break